import React, { useState } from "react";

interface Props {
  onLogin: (userId: string) => void;
}

const LoginPage: React.FC<Props> = ({ onLogin }) => {
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = () => {
    if (userId === "IPCUser" && password === "ipcuser") {
      onLogin(userId);
    } else {
      setError("Invalid credentials");
    }
  };

  return (
    <div className="login-container">
      <div className="login-title">
        🔐 IPC Enterprise Login
      </div>

      <input
        type="text"
        placeholder="User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      {error && <div className="login-error">{error}</div>}

      <button onClick={handleLogin}>
        Sign In
      </button>
    </div>
  );
};

export default LoginPage;
