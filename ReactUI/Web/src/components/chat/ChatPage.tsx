import React, { useState } from "react";
import Header from "../layout/Header";
import Footer from "../layout/Footer";
import ChatMessages from "./ChatMessages";
import ChatInput from "./ChatInput";
import UploadModal from "./UploadModal";
import { Message } from "../../models/MessageModels";
import { ChatRequest } from "../../models/ChatModels";
import { sendChatAPI } from "../../api/apiClient";

const ChatPage: React.FC = () => {

  const [department, setDepartment] =
    useState<string>("IT");

  const [question, setQuestion] =
    useState<string>("");

  const [messages, setMessages] =
    useState<Message[]>([]);

  const [showModal, setShowModal] =
    useState<boolean>(false);

  const handleSend = async (): Promise<void> => {

    if (!question.trim()) return;

    const payload: ChatRequest = {
      user_id: "Badri_User",
      question,
      department,
      provider: null,
      model_name: null,
    };

    try {
      const response = await sendChatAPI(payload);

      setMessages((prev) => [
        ...prev,
        { type: "user", text: question },
        { type: "bot", text: response.answer },
      ]);

      setQuestion("");

    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="chat-container">

      <Header
        department={department}
        setDepartment={setDepartment}
      />

      <ChatMessages messages={messages} />

      <ChatInput
        question={question}
        setQuestion={setQuestion}
        onSend={handleSend}
        onUploadClick={() => setShowModal(true)}
      />

      {showModal && (
        <UploadModal
          department={department}
          onClose={() => setShowModal(false)}
        />
      )}

      <Footer />
    </div>
  );
};

export default ChatPage;
