if (!document.getElementById("enterprise-copilot-panel")) {

  const panel = document.createElement("div");
  panel.id = "enterprise-copilot-panel";

  panel.style.position = "fixed";
  panel.style.top = "0";
  panel.style.right = "0";
  panel.style.width = "420px";
  panel.style.height = "100vh";
  panel.style.background = "#ffffff";
  panel.style.boxShadow = "-2px 0 8px rgba(0,0,0,0.1)";
  panel.style.zIndex = "999999";

  const iframe = document.createElement("iframe");
  iframe.src = chrome.runtime.getURL("index.html");
  iframe.style.width = "100%";
  iframe.style.height = "100%";
  iframe.style.border = "none";

  panel.appendChild(iframe);
  document.body.appendChild(panel);
}
