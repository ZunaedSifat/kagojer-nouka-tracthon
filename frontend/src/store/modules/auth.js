import { convertToken, getNewToken } from '@/api/auth.api';

const interval_time = 30 * 60 * 1000; // 30 minutes

const initial_state = () => ({
    access_token: null,
    refresh_token: null,
    interval_id: null
});

const state = initial_state();

const getters = {
    isLoggedIn(state) {
        return state.access_token !== null;
    }
};

const actions = {
    async exchangeSocialToken({ commit, dispatch }, params) {
        try {
            const response = await convertToken(params);
            const data = response.data;
            console.log(data);

            commit('SET_ACCESS_TOKEN', data['access_token']);
            commit('SET_REFRESH_TOKEN', data['refresh_token']);

            const id = setInterval(() => dispatch('refreshAccessToken'), interval_time);
            commit('SET_INTERVAL_ID', id);
        } catch (error) {
            return Promise.reject(error);
        }
    },
    async loginWithCredentials({ commit, dispatch }, params) {
        try {
            const response = await getNewToken(params);
            const data = response.data;
            console.log(data);

            commit('SET_ACCESS_TOKEN', data['access_token']);
            commit('SET_REFRESH_TOKEN', data['refresh_token']);

            const id = setInterval(() => dispatch('refreshAccessToken'), interval_time);
            commit('SET_INTERVAL_ID', id);
        } catch (error) {
            return Promise.reject(error);
        }
    },
    async autoLogin({ commit, dispatch }) {
        const token = localStorage.getItem('token');
        const params = {
            grant_type: 'refresh_token',
            client_id: process.env.VUE_APP_CLIENT_ID,
            client_secret: process.env.VUE_APP_CLIENT_SECRET,
            refresh_token: token
        };

        try {
            const response = await getNewToken(params);
            const data = response.data;
            console.log(data);

            commit('SET_ACCESS_TOKEN', data['access_token']);
            commit('SET_REFRESH_TOKEN', data['refresh_token']);

            const id = setInterval(() => dispatch('refreshAccessToken'), interval_time);
            commit('SET_INTERVAL_ID', id);
        } catch (error) {
            return Promise.reject(error);
        }
    },
    async refreshAccessToken({ state, commit }) {
        const params = {
            grant_type: 'refresh_token',
            client_id: process.env.VUE_APP_CLIENT_ID,
            client_secret: process.env.VUE_APP_CLIENT_SECRET,
            refresh_token: state.refresh_token
        };
        try {
            const response = await getNewToken(params);
            const data = response.data;
            console.log(data);

            commit('SET_ACCESS_TOKEN', data['access_token']);
            commit('SET_REFRESH_TOKEN', data['refresh_token']);

            // dispatch('profile/fetchCurrentUserProfile', null, { root: true });
        } catch (error) {
            return Promise.reject(error);
        }
    },
    logOut({ state, commit }) {
        clearInterval(state.interval_id);
        commit('RESET');
        // commit(`profile/${RESET}`, null, { root: true });
    }
};

const mutations = {
    SET_ACCESS_TOKEN(state, token) {
        state.access_token = token;
    },
    SET_REFRESH_TOKEN(state, token) {
        state.refresh_token = token;
        localStorage.setItem('token', token);
    },
    SET_INTERVAL_ID(state, id) {
        state.interval_id = id;
    },
    RESET(state) {
        localStorage.removeItem('token');
        const new_state = initial_state();
        Object.keys(new_state).forEach(key => {
            state[key] = new_state[key];
        });
    }
};

export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
};