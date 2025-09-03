import { api } from "../api/client";

export const listProjects = (token) => api("/projects", { token });
export const createProject = (token, name) => api("/projects", { method:"POST", body:{ name }, token });
export const getFullProject = (token, projectId) => api(`/projects/${projectId}/full`, { token });
