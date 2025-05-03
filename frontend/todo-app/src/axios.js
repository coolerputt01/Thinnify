// src/axios.js

import axios from 'axios';
import router from './router'; // Adjust the path if your router is elsewhere

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000/', // Replace with your Flask backend URL
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to request headers
api.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle expired token
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('access_token');
      router.push({ name: 'login' });
    }
    return Promise.reject(error);
  }
);

export default api;
