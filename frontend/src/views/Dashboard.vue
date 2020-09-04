<template>
    <v-row>
        <v-col cols="12" md="8">
            <trend-chart></trend-chart>
            <cluster-card
                v-for="(cluster, index) in clusters"
                :key="index"
                :cluster="cluster.name"
                :keywords="cluster.keywords"
                :article="cluster.article"
                :flag="cluster.flag"
            ></cluster-card>
        </v-col>
        <v-col cols="12" md="4">
            <trending-keywords></trending-keywords>
        </v-col>
    </v-row>
</template>

<script>
import clusters from "@/data/clusters";

export default {
    components: {
        "trend-chart": () => import("@/components/dashboard/TrendChart"),
        "trending-keywords": () =>
            import("@/components/dashboard/TrendingKeywords"),
        "cluster-card": () => import("@/components/dashboard/ClusterCard"),
    },
    data() {
        return {
            clusters,
        };
    },
};
</script>