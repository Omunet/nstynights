(function () {
  var button = document.querySelector("[data-nav-toggle]");
  var panel = document.querySelector("[data-nav-panel]");
  if (!button || !panel) {
    return;
  }

  var media = window.matchMedia("(max-width: 1120px)");

  function place() {
    panel.style.top = button.getBoundingClientRect().bottom + "px";
  }

  function setOpen(open) {
    if (open) {
      place();
    }
    button.setAttribute("aria-expanded", open ? "true" : "false");
    panel.classList.toggle("is-open", open);
    document.body.classList.toggle("nav-open", open);
  }

  button.addEventListener("click", function () {
    setOpen(button.getAttribute("aria-expanded") !== "true");
  });

  window.addEventListener("resize", function () {
    if (button.getAttribute("aria-expanded") === "true") {
      place();
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && button.getAttribute("aria-expanded") === "true") {
      setOpen(false);
      button.focus();
    }
  });

  panel.addEventListener("click", function (event) {
    if (event.target.closest("a")) {
      setOpen(false);
    }
  });

  function onViewport() {
    if (!media.matches) {
      setOpen(false);
    }
  }

  if (media.addEventListener) {
    media.addEventListener("change", onViewport);
  } else if (media.addListener) {
    media.addListener(onViewport);
  }
})();
