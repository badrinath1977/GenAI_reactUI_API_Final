import React from "react";
import ReactDOM from "react-dom/client";
import ChatPage from "./components/chat/ChatPage";
import "./styles/popup.css";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);

root.render(<ChatPage />);
