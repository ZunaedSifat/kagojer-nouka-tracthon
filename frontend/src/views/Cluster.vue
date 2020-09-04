<template>
    <v-row>
        <v-col cols="7" class="pl-5">
            <v-textarea
                class="mx-4 mb-2"
                solo
                dense
                rows="3"
                hide-details
                placeholder="Send a message to notify concerned users about the validity of related news..."
            ></v-textarea>
            <v-row justify="end" class="mx-4 mb-4">
                <v-btn class="mr-2" color="primary">
                    <v-icon small color="white" class="mr-2">$flag</v-icon>Flag
                </v-btn>
                <v-btn color="secondary">
                    <v-icon small color="white" class="mr-2">$message</v-icon>Message
                </v-btn>
            </v-row>
            <cluster-articles :cluster="cluster" :articles="articles"></cluster-articles>
        </v-col>
        <v-col cols="5">
            <cluster-trend-chart :chart_data="chart_data"></cluster-trend-chart>
            <cluster-stats :flag="flag" :article="article"></cluster-stats>
        </v-col>
    </v-row>
</template>

<script>
import clusters from "@/data/clusters";

export default {
    props: {
        cluster: {
            type: String,
            required: true,
        },
    },
    components: {
        "cluster-trend-chart": () =>
            import("@/components/clusters/ClusterTrendChart"),
        "cluster-stats": () => import("@/components/clusters/ClusterStats"),
        "cluster-articles": () =>
            import("@/components/clusters/ClusterArticles"),
    },
    data() {
        return {
            clusters,
            articles: [],
            flag: 0,
            article: 0,
        };
    },
    computed: {
        chart_data() {
            let labels = [];
            let counts = [];
            this.articles.forEach(function (article) {
                const date = article.date;
                const index = labels.findIndex((label) => label == date);
                if (index === -1) {
                    labels.push(date);
                    counts.push(1);
                } else {
                    counts[index]++;
                }
            });
            return {
                labels,
                counts,
            };
        },
    },
    created() {
        const name = this.cluster;
        const cluster_data = this.clusters.find(
            (cluster) => cluster.name == name
        );
        this.articles = cluster_data.articles;
        this.flag = cluster_data.flag;
        this.article = cluster_data.article;
    },
};
</script>

<style>
</style>