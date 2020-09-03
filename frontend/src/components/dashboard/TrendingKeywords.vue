<template>
    <v-card flat class="mr-4">
        <v-card-title
            class="font-weight-black"
            style="color: var(--v-primary-base)"
        >Trending Keywords</v-card-title>
        <v-card-text>
            <v-divider></v-divider>

            <v-list>
                <v-list-item v-for="keyword in keywords" :key="keyword.title" class="px-0">
                    <v-list-item-content>
                        <v-list-item-title class="font-weight-bold">{{ keyword.title }}</v-list-item-title>
                        <v-list-item-subtitle>{{ keyword.articles }} Articles</v-list-item-subtitle>
                        <v-divider class="mt-4"></v-divider>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    data() {
        return {
            keywords: [
                {
                    title: "Donald",
                    articles: 500,
                },
                {
                    title: "Trump",
                    articles: 413,
                },
                {
                    title: "Joe",
                    articles: 378,
                },
                {
                    title: "Biden",
                    articles: 215,
                },
                {
                    title: "Dynamite",
                    articles: 110,
                },
                {
                    title: "Bangladesh",
                    articles: 55,
                },
            ],
        };
    },
};
</script>

<style>
</style>