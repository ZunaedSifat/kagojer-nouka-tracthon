import axios from 'axios';
import store from '@/store/index';

const httpClient = axios.create({
    baseURL: process.env.VUE_APP_API_BASE_URL,
    timeout: 2000
});

const authInterceptor = (config) => {
    const accessToken = store.state.auth.access_token;

    if (accessToken) {
        config.headers['Authorization'] = `Bearer ${accessToken}`;
    }
    return config;
}

httpClient.interceptors.request.use(authInterceptor);

export default httpClient;