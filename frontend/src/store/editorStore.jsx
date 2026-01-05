import { create } from "zustand"

export const useEditor = create((set, get) => ({
  project: null,
  currentPageId: null,
  setProject: (p) => set({ project: p, currentPageId: p?.pages?.[0]?.id ?? null }),
  setCurrentPage: (id) => set({ currentPageId: id }),
  pageById: (id) => get().project?.pages?.find(p => p.id === id),
  replaceComponents: (pageId, components) => {
    const proj = structuredClone(get().project)
    const page = proj.pages.find(p => p.id === pageId)
    page.components = components
    set({ project: proj })
  },
}))
