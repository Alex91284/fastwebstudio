export const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export const api = async (url, { method="GET", body, token } = {}) => {
  const res = await fetch(`${API_URL}${url}`, {
    method,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
};
