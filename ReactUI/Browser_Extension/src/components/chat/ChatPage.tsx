import React, { useState } from "react";
import { sendChatMessage } from "../../api/apiClient";
import { Message } from "../../models/ChatTypes";
import ChatInput from "./ChatInput";
import ChatMessages from "./ChatMessages";
import UploadModal from "./UploadModal";

const ChatPage: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [department, setDepartment] = useState("");
  const [showUpload, setShowUpload] = useState(false);

  const handleSendMessage = async (question: string): Promise<void> => {
    if (!question.trim()) return;

    // 🚨 Department Validation
    if (!department) {
      const warningMessage: Message = {
        id: crypto.randomUUID(),
        type: "bot",
        text: "⚠ Please select a department before searching.",
        timestamp: new Date().toISOString(),
        department: "System",
      };

      setMessages((prev) => [...prev, warningMessage]);
      return;
    }

    const userMessage: Message = {
      id: crypto.randomUUID(),
      type: "user",
      text: question,
      timestamp: new Date().toISOString(),
      department,
    };

    setMessages((prev) => [...prev, userMessage]);

    const typingId = crypto.randomUUID();

    const typingMessage: Message = {
      id: typingId,
      type: "bot",
      text: "Typing...",
      timestamp: new Date().toISOString(),
      department,
    };

    setMessages((prev) => [...prev, typingMessage]);

    try {
      const response = await sendChatMessage(
        "BrowserUser",
        question,
        department
      );

      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === typingId
            ? { ...msg, text: response.answer }
            : msg
        )
      );
    } catch (error: any) {
      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === typingId
            ? {
                ...msg,
                text: error.message || "Search failed",
              }
            : msg
        )
      );
    }
  };

  return (
    <div className="chat-container">

      {/* HEADER */}
      <div className="chat-header">
        🤖 Enterprise AI Assistant
      </div>

      {/* DEPARTMENT SELECT */}
      <select
        value={department}
        onChange={(e) => setDepartment(e.target.value)}
        className="department-select"
      >
        <option value="">Select Department</option>
        <option value="HR">HR</option>
        <option value="IT">IT</option>
        <option value="Finance">Finance</option>
        <option value="All">All</option>
      </select>

      {/* MESSAGE AREA */}
      <ChatMessages messages={messages} />

      {/* BOTTOM FIXED SECTION */}
      <div className="bottom-section">
        <div className="chat-input-wrapper">
          <button
            className="attach-btn"
            onClick={() => setShowUpload(true)}
          >
            +
          </button>

          <ChatInput onSend={handleSendMessage} />
        </div>
      </div>

      {/* UPLOAD POPUP */}
      {showUpload && (
        <UploadModal
          department={department}
          onClose={() => setShowUpload(false)}
        />
      )}

    </div>
  );
};

export default ChatPage;
