<template>
    <v-card class="mr-4">
        <v-card-title style="color: var(--v-primary-base)">Statistics</v-card-title>
        <v-divider class="mx-4"></v-divider>

        <v-card-subtitle>
            Trend
            <v-icon small color="secondary" class="ml-2">$trend</v-icon>
        </v-card-subtitle>
        <v-card-text>
            <v-icon color="primary" class="mr-1">$up</v-icon>
            <span>{{ upward_trend }}%</span>

            <v-icon color="secondary" class="mr-1">$down</v-icon>
            <span>{{ downward_trend }}%</span>
            <v-divider class="mt-4"></v-divider>
        </v-card-text>

        <v-card-subtitle class="pt-0">
            Articles
            <v-icon small color="secondary" class="ml-2">$article</v-icon>
        </v-card-subtitle>
        <v-card-text>
            <span>202</span>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    computed: {
        upward_trend() {
            return Math.round(Math.random() * 100);
        },
        downward_trend() {
            return Math.round(Math.random() * 100);
        },
    },
};
</script>

<style scoped>
.v-card__subtitle {
    color: var(--v-secondary-base) !important;
    font-weight: 500;
    display: flex;
    align-items: center;
}
</style>