<template>
    <v-card flat class="mr-4">
        <v-card-title
            class="font-weight-black"
            style="color: var(--v-primary-base)"
        >Trending Keywords</v-card-title>
        <v-card-text>
            <v-divider></v-divider>

            <v-list v-if="loading">
                <v-skeleton-loader type="list-item-two-line" v-for="i in 5" :key="i"></v-skeleton-loader>
            </v-list>
            <v-list v-else>
                <v-list-item
                    v-for="keyword in keywords"
                    :key="keyword.word"
                    class="px-0"
                    :to="`/keywords/${keyword.word}`"
                >
                    <v-list-item-content>
                        <v-list-item-title class="font-weight-bold">{{ keyword.word }}</v-list-item-title>
                        <v-list-item-subtitle>{{ keyword.count }} Articles</v-list-item-subtitle>
                        <v-divider class="mt-4"></v-divider>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-card-text>
    </v-card>
</template>

<script>
import { getTopKeywords } from "@/api/keywords.api.js";
import static_keywords from "@/data/keywords";

export default {
    data() {
        return {
            loading: false,
            keywords: [],
        };
    },
    methods: {
        async fetchKeywords() {
            this.loading = true;
            try {
                const response = await getTopKeywords(10);
                console.log(response);
                // this.keywords = response.data;
            } catch (error) {
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
    },
    created() {
        this.keywords = static_keywords;
        this.fetchKeywords();
    },
};
</script>

<style>
</style>