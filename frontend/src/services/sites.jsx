import { api } from "../api/client"
export const upsertSite = (token, projectId, payload) => api(`/sites/${projectId}`, { method:"POST", body:payload, token })
export const publishSite = (token, projectId) => api(`/sites/${projectId}/publish`, { method:"POST", token })
export const getPublicSite = (slug) => api(`/sites/public/${slug}`)
