import React, { useState } from "react";

interface Props {
  onSend: (q: string) => void;
  disabled?: boolean;
}

const ChatInput: React.FC<Props> = ({
  onSend,
  disabled,
}) => {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim() || disabled) return;
    onSend(input);
    setInput("");
  };

  return (
        <div className="chat-input">
          <input
            type="text"
            value={input}
            disabled={disabled}
            autoFocus
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) =>
              e.key === "Enter" && handleSend()
            }
        />

      <button
        disabled={disabled}
        onClick={handleSend}
      >
        Send
      </button>
    </div>
  );
};

export default ChatInput;
