<template>
    <v-card class="ma-4 ml-0">
        <v-sheet
            class="v-sheet--offset mx-auto"
            color="cyan"
            elevation="12"
            max-width="calc(100% - 32px)"
        >
            <v-container>
                <v-sparkline
                    v-if="!loading"
                    type="trend"
                    color="white"
                    smooth="10"
                    padding="16"
                    line-width="3"
                    auto-draw
                    height="150"
                    :labels="labels"
                    :value="value"
                ></v-sparkline>
            </v-container>
            <!-- <line-chart v-if="!loading" :chart_data="chart_data" :height="250"></line-chart> -->
        </v-sheet>

        <v-card-title class="pt-0" style="color: var(--v-primary-base)">Keyword History</v-card-title>
    </v-card>
</template>

<script>
import { getKeywordHistory } from "@/api/keywords.api.js";

export default {
    props: {
        word: {
            type: String,
            required: true,
        },
    },
    components: {
        // "line-chart": () => import("@/components/common/LineChart"),
    },
    data() {
        return {
            loading: false,
            chart_data: null,
            labels: null,
            value: null,
        };
    },
    methods: {
        async fetchChartData() {
            this.loading = true;
            try {
                const response = await getKeywordHistory(this.word);
                let labels = [];
                let values = [];
                console.log(response);
                const entries = response.data;
                entries.forEach(function (entry) {
                    labels.push(entry.content__upload_date);
                    values.push(entry.count);
                });
                // this.chart_data = {
                //     labels,
                //     datasets: [
                //         {
                //             label: this.word,
                //             borderColor: "white",
                //             fill: false,
                //             pointRadius: 0,
                //             data: values,
                //         },
                //     ],
                // };
            } catch (error) {
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
    },
    created() {
        this.labels = [
            "2020-07-10",
            "2020-07-12",
            "2020-07-15",
            "2020-07-16",
            "2020-07-18",
            "2020-07-21",
            "2020-07-24",
            "2020-07-25",
        ];
        this.value = [128, 40, 39, 102, 45, 180, 121, 50];
        this.chart_data = {
            labels: this.labels,
            datasets: [
                {
                    label: this.word,
                    borderColor: "white",
                    fill: false,
                    pointRadius: 0,
                    data: this.value,
                },
            ],
        };
        this.fetchChartData();
    },
};
</script>

<style scoped>
.v-sheet--offset {
    top: -24px;
    position: relative;
}
</style>