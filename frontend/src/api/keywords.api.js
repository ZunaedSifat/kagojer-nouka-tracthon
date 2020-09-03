import httpClient from './httpClient';

const END_POINT = 'api/trending/keywords';

const getTopKeywords = (count) => httpClient.get(`${END_POINT}/top/`, {
    query: {
        count
    }
});

const getKeywordsByTimePeriod = (period, count) => httpClient.get(`${END_POINT}/`, {
    query: {
        period,
        count
    }
});

const getKeywordHistory = (word) => httpClient.get(`${END_POINT}/history/`, {
    query: {
        word
    }
});

export {
    getTopKeywords,
    getKeywordsByTimePeriod,
    getKeywordHistory
};