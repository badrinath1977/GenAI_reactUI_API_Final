// src/api/apiClient.ts

import { config } from "../config";


const BASE_URL = "http://127.0.0.1:8002";
console.log("DEBUG URL:", BASE_URL);
/**
 * -----------------------------
 * Chat API
 * -----------------------------
 */
export async function sendChatMessage(
  userId: string,
  question: string,
  department: string
) {
  const response = await fetch(`${config.apiBaseUrl}/chat/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      user_id: userId,
      question,
      department,
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || "Chat API failed");
  }

  return data;
}

/**
 * -----------------------------
 * Upload API
 * -----------------------------
 */
export async function uploadDocument(
  file: File,
  department: string
) {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("department", department);

  const response = await fetch(
    `${config.apiBaseUrl}/upload/document`,
    {
      method: "POST",
      body: formData,
    }
  );

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || "Upload failed");
  }

  return data;
}
