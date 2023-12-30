import axios from "axios";

const BASE_URL = `http://${window.location.hostname}:8081/api/`;

export const loginUser = async (formData) => {
  try {
    const response = await axios.post(`${BASE_URL}login/`, formData);
    return response.data;
  } catch (error) {
    console.error("Error logging in:", error);
    throw error;
  }
};

export const logoutUser = async (token) => {
  try {
    await axios.post(
      `${BASE_URL}logout/`,
      {},
      {
        headers: { Authorization: `Token ${token}` },
      }
    );
  } catch (error) {
    console.error("Error logging out:", error);
    throw error;
  }
};
