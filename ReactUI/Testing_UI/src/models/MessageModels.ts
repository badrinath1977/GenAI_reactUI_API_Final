export interface Message {
  id: string;
  type: "user" | "bot";
  text: string;
  timestamp: string;
  department: string;
}
