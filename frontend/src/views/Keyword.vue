<template>
    <v-row>
        <v-col cols="7" class="pl-5">
            <keyword-articles :word="word"></keyword-articles>
        </v-col>
        <v-col cols="5">
            <keyword-trend-chart :word="word"></keyword-trend-chart>
            <keyword-stats></keyword-stats>
        </v-col>
    </v-row>
</template>

<script>
export default {
    props: {
        word: {
            type: String,
            required: true,
        },
    },
    components: {
        "keyword-trend-chart": () =>
            import("@/components/keywords/KeywordTrendChart"),
        "keyword-stats": () => import("@/components/keywords/KeywordStats"),
        "keyword-articles": () =>
            import("@/components/keywords/KeywordArticles"),
    },
    created() {
        console.log(this.word);
    },
};
</script>

<style>
</style>