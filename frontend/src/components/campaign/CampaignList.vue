<template>
    <v-container class="mr-4">
        <div class="title text-center">Previous Campaigns</div>

        <v-list color="transparent">
            <v-list-item v-for="(cluster, index) in clusters" :key="index" class="mb-4">
                <v-card width="100%">
                    <v-card-title>{{ cluster.name }}</v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text>
                        <v-row>
                            <v-col cols="7">
                                <v-chip
                                    class="ma-2"
                                    :color="colors[index]"
                                    text-color="white"
                                    label
                                    v-for="(media, index) in cluster.media"
                                    :key="index"
                                >{{ media }}</v-chip>
                            </v-col>
                            <v-col cols="5" class="text-end">
                                <v-icon color="primary" class="mr-1">$up</v-icon>
                                <span>{{ upward_trend }}%</span>

                                <v-icon color="secondary" class="mr-1">$down</v-icon>
                                <span>{{ downward_trend }}%</span>

                                <v-btn text color="secondary" small>{{ cluster.article }} articles</v-btn>

                                <v-btn text color="primary" small>{{ cluster.flag }} flags</v-btn>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-list-item>
        </v-list>
    </v-container>
</template>

<script>
import clusters from "@/data/clusters";

export default {
    data() {
        return {
            clusters,
            colors: ["primary", "secondary", "pink"],
        };
    },
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

<style>
</style>