// store.js
import { defineStore } from "pinia";

// Utility function to load persisted state
function loadState(key) {
    const cookieValue = document.cookie.match(`(^|;)\\s*${key}\\s*=\\s*([^;]+)`);
    return cookieValue ? JSON.parse(cookieValue.pop()) : null;
}

// Utility function to save state to cookie
function saveState(key, state) {
    const expiration = new Date(Date.now() + 2592000 * 1000); // Set expiration time to 30 days from now
    const cookie = `${key}=${JSON.stringify(
        state
    )}; path=/; expires=${expiration.toUTCString()};`;
    document.cookie = cookie;
}

export const useSidebarStore = defineStore('sidebar', {
    state: () => ({
        menu: loadState("menu") || 0,
        activeLink: null,
    }),
    getters: {
        token(state) {
            return !!state.menu;
        },
    },
    actions: {
        setActiveLink(linkId) {
            this.activeLink = linkId;
            saveState("menu", linkId);
        }
    }
});
