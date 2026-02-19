// src/config.ts

export const config = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL,
};

if (!config.apiBaseUrl) {
  throw new Error("VITE_API_BASE_URL is not configured in .env");
}
