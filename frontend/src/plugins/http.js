import axios from 'axios'

const http = axios.create({
    baseURL: process.env.VUE_APP_BACKEND_URL,
    timeout: 1000,
    headers: { /* TODO: append credentials once authentication working api-side */ }
});

export default http
