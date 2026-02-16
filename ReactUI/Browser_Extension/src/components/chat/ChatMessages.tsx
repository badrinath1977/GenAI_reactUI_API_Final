import React, { useEffect, useRef } from "react";
import { Message } from "../../models/MessageModels";

interface Props {
  messages: Message[];
}

const ChatMessages: React.FC<Props> = ({ messages }) => {

  const bottomRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="chat-area">
      {messages.map((msg, index) => (
        <div
          key={index}
          className={msg.type === "user" ? "user-msg" : "bot-msg"}
        >
          {msg.text}
        </div>
      ))}

      <div ref={bottomRef} />
    </div>
  );
};

export default ChatMessages;
