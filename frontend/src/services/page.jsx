import { api } from "../api/client"
export const createPage = (token, projectId, data) => api(`/pages/${projectId}`, { method:"POST", body:data, token })
export const updatePage = (token, pageId, data) => api(`/pages/${pageId}`, { method:"PUT", body:data, token })
export const deletePage = (token, pageId) => api(`/pages/${pageId}`, { method:"DELETE", token })
