import React, {
  useState,
  useEffect,
} from "react";
import ReactDOM from "react-dom/client";
import ChatPage from "./components/chat/ChatPage";
import LoginPage from "./components/LoginPage";
import { storage } from "./utils/storage";
import "./styles/popup.css";

const App: React.FC = () => {
  const [userId, setUserId] =
    useState<string | null>(null);
  const [ready, setReady] =
    useState(false);

  useEffect(() => {
    storage.get("userId").then(
      (id) => {
        if (id) setUserId(id);
        setReady(true);
      }
    );
  }, []);

  const handleLogin = (id: string) => {
    storage.set("userId", id);
    setUserId(id);
  };

  const handleLogout = () => {
    storage.remove("userId");
    setUserId(null);
  };

  if (!ready) return null;

  if (!userId) {
    return (
      <LoginPage
        onLogin={handleLogin}
      />
    );
  }

  return (
    <ChatPage
      userId={userId}
      onLogout={handleLogout}
    />
  );
};

ReactDOM.createRoot(
  document.getElementById("root")!
).render(<App />);
