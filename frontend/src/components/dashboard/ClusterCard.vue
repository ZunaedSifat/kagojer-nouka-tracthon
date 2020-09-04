<template>
    <v-card class="ma-4" :to="`/clusters/${cluster}`">
        <v-card-title class="pb-0">
            {{ cluster }}
            <v-btn icon>
                <v-icon small>$edit</v-icon>
            </v-btn>
        </v-card-title>
        <v-card-text class="py-0">
            <v-row>
                <v-col cols="5">
                    <v-chip
                        v-for="(keyword, index) in keywords"
                        :key="index"
                        :color="colors[index]"
                        label
                        text-color="white"
                        class="ma-1"
                    >{{ keyword }}</v-chip>
                </v-col>
                <v-col cols="7">
                    <v-card-actions class="pl-0 pt-0 justify-end">
                        <v-icon color="primary" class="mr-1">$up</v-icon>
                        <span>{{ upward_trend }}%</span>

                        <v-icon color="secondary" class="mr-1">$down</v-icon>
                        <span>{{ downward_trend }}%</span>

                        <v-divider vertical class="ml-4 mr-2"></v-divider>

                        <v-btn text color="secondary" small>{{ article }} articles</v-btn>

                        <v-divider vertical class="mx-2"></v-divider>

                        <v-btn text color="primary" small>{{ flag }} flags</v-btn>
                    </v-card-actions>
                    <v-card-actions class="justify-end">
                        <v-btn color="primary" small>
                            <v-icon small color="white" class="mr-2">$flag</v-icon>Flag this cluster
                        </v-btn>
                    </v-card-actions>
                </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    props: {
        cluster: {
            type: String,
            required: true,
        },
        keywords: {
            type: Array,
            required: true,
        },
        article: {
            type: Number,
            required: true,
        },
        flag: {
            type: Number,
            required: true,
        },
    },
    data() {
        return {
            colors: ["primary", "secondary", "pink", "blue", "purple"],
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

