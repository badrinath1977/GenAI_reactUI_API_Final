import { ChatRequest, ChatResponse } from "../models/ChatModels";

const BASE_URL = "http://localhost:8001";

export const sendChatAPI = async (
  payload: ChatRequest
): Promise<ChatResponse> => {

  const res = await fetch(`${BASE_URL}/chat/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  if (!res.ok) {
    throw new Error("Chat API failed");
  }

  return res.json();
};

export const uploadDocumentAPI = async (
  formData: FormData
): Promise<void> => {

  const res = await fetch(`${BASE_URL}/upload/document`, {
    method: "POST",
    body: formData
  });

  if (!res.ok) {
    throw new Error("Upload failed");
  }
};
