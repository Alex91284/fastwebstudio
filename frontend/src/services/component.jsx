import { api } from "../api/client"
export const addComponent = (token, pageId, data) => api(`/components/${pageId}`, { method:"POST", body:data, token })
export const updateComponent = (token, id, data) => api(`/components/${id}`, { method:"PUT", body:data, token })
export const deleteComponent = (token, id) => api(`/components/${id}`, { method:"DELETE", token })
