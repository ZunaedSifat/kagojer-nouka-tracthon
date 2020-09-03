<template>
    <v-row>
        <v-col cols="12" md="8">
            <trend-chart></trend-chart>
            <cluster-card v-for="i in 5" :key="i"></cluster-card>
        </v-col>
        <v-col cols="12" md="4">
            <trending-keywords></trending-keywords>
        </v-col>
    </v-row>
</template>

<script>
export default {
    components: {
        "trend-chart": () => import("@/components/dashboard/TrendChart"),
        "trending-keywords": () =>
            import("@/components/dashboard/TrendingKeywords"),
        "cluster-card": () => import("@/components/dashboard/ClusterCard"),
    },
};
</script>