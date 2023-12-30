import { defineStore } from "pinia";
import { loginUser, logoutUser } from "@/services/authServices";

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

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    user: loadState("user"), // Load the persisted user state
  }),
  getters: {
    isAuthenticated(state) {
      return !!state.user;
    },
    token(state) {
      return state.token;
    },
  },
  actions: {
    setUser(userData) {
      this.user = userData;
      saveState("user", userData); // Save the user state to cookie
    },
    async login(formData) {
      try {
        const { user, token } = await loginUser(formData);
        this.setUser({ ...user, token: token });
        return true;
      } catch (error) {
        this.error = error.message;
      } finally {
        this.isLoading = false;
      }
    },
    async logout(token) {
      try {
        await logoutUser(token);
        // Perform any necessary cleanup or state changes after logout
        this.user = null;
        saveState("user", null); // Remove the user state from cookie
      } catch (error) {
        // Handle error
      }
    },
  },
});
