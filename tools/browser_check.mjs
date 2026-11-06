import { spawn } from "node:child_process";

const chrome = spawn(
  "google-chrome",
  [
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--user-data-dir=/tmp/chrome-nsty-qa",
    "--remote-debugging-port=9223",
    "about:blank",
  ],
  { stdio: "ignore" }
);

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function json(url, method = "GET") {
  const response = await fetch(url, { method });
  const text = await response.text();
  return JSON.parse(text);
}

async function connect(pageUrl) {
  const created = await json(`http://127.0.0.1:9223/json/new?${encodeURIComponent(pageUrl)}`, "PUT");
  const socket = new WebSocket(created.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    socket.addEventListener("open", resolve);
    socket.addEventListener("error", reject);
  });
  let id = 0;
  const pending = new Map();
  const events = [];
  socket.addEventListener("message", (event) => {
    const message = JSON.parse(event.data);
    if (message.id && pending.has(message.id)) {
      pending.get(message.id)(message);
      pending.delete(message.id);
    } else if (message.method) {
      events.push(message);
    }
  });
  function send(method, params = {}) {
    const next = ++id;
    socket.send(JSON.stringify({ id: next, method, params }));
    return new Promise((resolve) => pending.set(next, resolve));
  }
  return { socket, send, events, id: created.id };
}

const pages = [
  ["/", 1440, 900],
  ["/", 390, 844],
  ["/test/", 1440, 900],
  ["/test/", 390, 844],
  ["/test/faq/", 390, 844],
  ["/test/photos/", 1440, 900],
  ["/test/es/", 1440, 900],
  ["/test/access/", 390, 844],
  ["/test/dress-code/", 390, 844],
  ["/test/contact/", 1280, 900],
  ["/test/aviso-legal/", 1440, 900],
];

const failures = [];

await sleep(400);
for (const [path, width, height] of pages) {
  const url = `http://127.0.0.1:8765${path}`;
  const session = await connect(url);
  await session.send("Page.enable");
  await session.send("Runtime.enable");
  await session.send("Log.enable");
  await session.send("Emulation.setDeviceMetricsOverride", {
    width,
    height,
    deviceScaleFactor: 1,
    mobile: width < 500,
  });
  await session.send("Page.navigate", { url });
  await sleep(700);
  const result = await session.send("Runtime.evaluate", {
    expression: `(() => {
      const doc = document.documentElement;
      const overflow = doc.scrollWidth - doc.clientWidth;
      const errors = [];
      const details = document.querySelector("details");
      if (details) {
        details.querySelector("summary").focus();
        details.open = true;
      }
      const button = document.querySelector("[data-nav-toggle]");
      let expanded = null;
      if (button && ${width} < 500) {
        button.click();
        expanded = button.getAttribute("aria-expanded");
      }
      const lang = document.querySelector("a[hreflang]");
      return {
        overflow,
        title: document.title,
        imgs: document.images.length,
        broken: [...document.images].filter((img) => img.complete && img.naturalWidth === 0).map((img) => img.src),
        inputs: document.querySelectorAll("input, form, textarea").length,
        expanded,
        detailsOpen: details ? details.open : null,
        langHref: lang ? lang.getAttribute("href") : null,
        h1: document.querySelector("h1") ? document.querySelector("h1").textContent : null
      };
    })()`,
    returnByValue: true,
  });
  const value = result.result.result.value;
  const consoleErrors = session.events.filter((event) => {
    const type = event.params && (event.params.type || event.params.level);
    return event.method === "Runtime.exceptionThrown" || type === "error";
  });
  if (value.overflow > 1) failures.push(`${path} ${width} overflow ${value.overflow}`);
  if (value.broken.length) failures.push(`${path} broken images ${value.broken.join(",")}`);
  if (value.inputs) failures.push(`${path} has inputs`);
  if (consoleErrors.length) failures.push(`${path} console errors ${consoleErrors.length}`);
  if (path === "/test/faq/" && value.detailsOpen !== true) failures.push("faq did not open");
  if (path === "/test/" && width === 390 && value.expanded !== "true") failures.push("mobile nav did not open");
  if (path === "/test/" && value.langHref !== "/test/es/") failures.push(`home language link ${value.langHref}`);
  if (path === "/test/es/" && value.langHref !== "/test/") failures.push(`es language link ${value.langHref}`);
  console.log(JSON.stringify({ path, width, ...value, consoleErrors: consoleErrors.length }));
  await session.send("Page.close").catch(() => {});
  session.socket.close();
}

chrome.kill("SIGKILL");
if (failures.length) {
  console.log("BROWSER_FAIL");
  for (const failure of failures) console.log(failure);
  process.exit(1);
}
console.log("BROWSER_PASS");
