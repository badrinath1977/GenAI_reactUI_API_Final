import React from "react";
import { Message } from "../../models/MessageModels";

interface Props {
  messages: Message[];
}

const ChatMessages: React.FC<Props> = ({ messages }) => {

  return (
    <div className="chat-area">
      {messages.map((msg, index) => (
        <div
          key={index}
          className={
            msg.type === "user" ? "user-msg" : "bot-msg"
          }
        >
          {msg.text}
        </div>
      ))}
    </div>
  );
};

export default ChatMessages;
