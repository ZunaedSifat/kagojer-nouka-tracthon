import httpClient from './httpClient';

const END_POINT = 'api/trending/keywords';

const getTopKeywords = (count) => httpClient.get(`${END_POINT}/`, {
    params: {
        count
    }
});

const getKeywordsByTimePeriod = (period, count) => httpClient.get(`${END_POINT}/top/`, {
    params: {
        period,
        count
    }
});

const getKeywordHistory = (word) => httpClient.get(`${END_POINT}/history/`, {
    params: {
        word
    }
});

export {
    getTopKeywords,
    getKeywordsByTimePeriod,
    getKeywordHistory
};