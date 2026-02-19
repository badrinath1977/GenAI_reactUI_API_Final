// src/models/ChatTypes.ts

// -----------------------------
// Chat Message Type
// -----------------------------
export interface Message {
  id: string;
  type: "user" | "bot";
  text: string;
  timestamp: string;
  department: string;
}

// -----------------------------
// Handler Types
// -----------------------------
export type SendMessageHandler = (
  question: string
) => Promise<void> | void;
