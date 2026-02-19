import React, { useState } from "react";
import { sendChatMessage } from "../../api/apiClient";
import { Message } from "../../models/ChatTypes";
import ChatInput from "./ChatInput";
import ChatMessages from "./ChatMessages";
import UploadModal from "./UploadModal";
import Toast from "../Toast";

interface Props {
  userId: string;
  onLogout: () => void;
}

const ChatPage: React.FC<Props> = ({
  userId,
  onLogout,
}) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [department, setDepartment] = useState("");
  const [isSending, setIsSending] = useState(false);
  const [showUpload, setShowUpload] = useState(false);
  const [toast, setToast] = useState("");

  // 🔐 Strict validation
  const isDepartmentValid = () => {
    return department !== "";
  };

  const streamText = async (
    fullText: string,
    messageId: string
  ) => {
    const words = fullText.split(" ");
    let current = "";

    for (let i = 0; i < words.length; i++) {
      current += words[i] + " ";

      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === messageId
            ? { ...msg, text: current }
            : msg
        )
      );

      await new Promise((res) =>
        setTimeout(res, 25)
      );
    }
  };

  const handleSendMessage = async (question: string) => {
    if (!isDepartmentValid()) {
      setToast("Select department first.");
      setTimeout(() => setToast(""), 2500);
      return;
    }

    setIsSending(true);

    const responseId = crypto.randomUUID();

    setMessages((prev) => [
      ...prev,
      {
        id: crypto.randomUUID(),
        type: "user",
        text: question,
        timestamp: new Date().toISOString(),
        department,
      },
      {
        id: responseId,
        type: "bot",
        text: "",
        timestamp: new Date().toISOString(),
        department,
      },
    ]);

    try {
      const response = await sendChatMessage(
        userId,
        question,
        department
      );

      await streamText(response.answer, responseId);
    } catch {
      setToast("Error occurred");
      setTimeout(() => setToast(""), 2500);
    }

    setIsSending(false);
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        🤖 Enterprise AI Assistant
        <button
          className="logout-btn"
          onClick={onLogout}
          title={`Logout (${userId})`}
        >
          ⎋
        </button>
      </div>

      <select
        value={department}
        onChange={(e) =>
          setDepartment(e.target.value)
        }
        className="department-select"
      >
        <option value="">
          Select Department
        </option>
        <option value="HR">HR</option>
        <option value="IT">IT</option>
        <option value="Finance">Finance</option>
        <option value="All">All</option>
      </select>

      <ChatMessages messages={messages} />

      <div className="bottom-section">
        <div className="chat-input-wrapper">

          <button
            className="attach-btn"
            disabled={isSending || !isDepartmentValid()}
            onClick={() => {
              if (!isDepartmentValid()) {
                setToast("Select department first.");
                setTimeout(() => setToast(""), 2500);
                return;
              }
              setShowUpload(true);
            }}
          >
            +
          </button>

          <ChatInput
            onSend={handleSendMessage}
            disabled={isSending || !isDepartmentValid()}
          />
        </div>
      </div>

      {showUpload && (
        <UploadModal
          userId={userId}
          department={department}
          onClose={() => setShowUpload(false)}
          onSummaryGenerated={(msg) =>
            setMessages((prev) => [...prev, msg])
          }
        />
      )}

      {toast && <Toast message={toast} />}
    </div>
  );
};

export default ChatPage;
