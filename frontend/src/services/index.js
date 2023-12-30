import axios from "axios";
import { useAuthStore } from "@/stores/authStore";
import { createPinia } from "pinia";
import { createApp } from "vue";
import App from "../App.vue";

const pinia = createPinia();
const app = createApp(App);
app.use(pinia);

const windowLocation = window.location;
const BASE_URL = `http://${windowLocation.hostname}:8081/api/`;

const authStore = useAuthStore();
const user = authStore.user;
const token = user ? user.token : null;
const author = user ? user.username : null;

const AUTH_HEADER = `Token ${token}`;

const makeRequest = async (method, url, data = {}) => {
    try {
        const { data: responseData } = await axios({
            method,
            url: `${BASE_URL}${url}`,
            data,
            headers: { Authorization: AUTH_HEADER },
        });
        return responseData;
    } catch (error) {
        console.error("Error:", error);
        throw error;
    }
};

const fetchAllItems = async (url) => {
    return makeRequest("get", url);
};

const fetchItem = async (url, id) => {
    return makeRequest("get", `${url}${id}`);
};

const addItem = async (url, data) => {
    data.author = author;
    return makeRequest("post", url, data);
};

const editItem = async (url, id, data) => {
    return makeRequest("put", `${url}${id}/`, data);
};

const deleteItem = async (url, id) => {
    return makeRequest("get", `${url}delete/${id}`);
};

const filterItems = async (url, data) => {
    return makeRequest("post", `${url}filter/`, data);
};

const saveImage = async (data) => {
    return makeRequest("post", "savefile/", data);
};

export const api = (main, resource) => {
    const URL = `${main}/${resource}/`;
    return {
        fetchAll: async () => fetchAllItems(URL),
        fetchOne: async (id) => fetchItem(URL, id),
        add: async (data) => addItem(URL, data),
        edit: async (id, data) => editItem(URL, id, data),
        delete: async (id) => deleteItem(URL, id),
        filter: async (data) => filterItems(URL, data),
        saveImage: async (data) => saveImage(data),
    };
};
