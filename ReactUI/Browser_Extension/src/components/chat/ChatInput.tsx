import React, { useState } from "react";
import { SendMessageHandler } from "../../models/ChatTypes";

interface Props {
  onSend: SendMessageHandler;
}

const ChatInput: React.FC<Props> = ({ onSend }) => {
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    try {
      setSending(true);
      await onSend(input.trim());
      setInput("");
    } finally {
      setSending(false);
    }
  };

  const handleKeyDown = (
    e: React.KeyboardEvent<HTMLInputElement>
  ) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="chat-input">
      <input
        type="text"
        placeholder="Ask something..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={sending}
      />

      <button onClick={handleSend} disabled={sending}>
        {sending ? "Sending..." : "Send"}
      </button>
    </div>
  );
};

export default ChatInput;
