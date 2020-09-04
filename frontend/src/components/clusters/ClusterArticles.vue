<template>
    <v-container class>
        <span class="title">
            Articles in cluster
            <span style="color: var(--v-primary-base)">#{{ cluster }}</span>
        </span>

        <v-list color="transparent">
            <v-list-item v-for="(article, index) in articles" :key="index" class="mb-4 px-0">
                <v-card width="100%">
                    <v-card-subtitle>{{ article.date }}</v-card-subtitle>
                    <v-card-text>{{ article.text }}</v-card-text>
                </v-card>
            </v-list-item>
        </v-list>
    </v-container>
</template>

<script>
export default {
    props: {
        cluster: {
            type: String,
            required: true,
        },
        articles: {
            type: Array,
            required: true,
        },
    },
};
</script>

<style>
</style>