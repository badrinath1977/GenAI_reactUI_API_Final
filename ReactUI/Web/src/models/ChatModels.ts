export interface ChatRequest {
  user_id: string;
  question: string;
  department: string;
  provider?: string | null;
  model_name?: string | null;
}

export interface ChatResponse {
  answer: string;
  department: string;
}
