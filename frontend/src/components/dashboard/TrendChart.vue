<template>
    <v-card class="ma-4">
        <v-sheet
            class="v-sheet--offset mx-auto"
            color="cyan"
            elevation="12"
            max-width="calc(100% - 32px)"
        >
            <bar-chart v-if="!loading" :chart_data="chart_data" :height="150"></bar-chart>
        </v-sheet>

        <v-card-title class="pt-0" style="color: var(--v-primary-base)">Trending Clusters</v-card-title>
    </v-card>
</template>

<script>
import { getKeywordsByTimePeriod } from "@/api/keywords.api.js";

export default {
    components: {
        "bar-chart": () => import("@/components/common/BarChart"),
    },
    data() {
        return {
            loading: false,
            chart_data: null,
        };
    },
    methods: {
        async fetchChartData() {
            this.loading = true;
            try {
                const response = await getKeywordsByTimePeriod("days", 3);
                console.log(response);
                this.chart_data = response.data;
            } catch (error) {
                console.log(error);
                this.chart_data = {
                    labels: [
                        "2020-07-05",
                        "2020-07-06",
                        "2020-07-08",
                        "2020-07-09",
                        "2020-07-10",
                        "2020-07-12",
                        "2020-07-15",
                        "2020-07-16",
                        "2020-07-18",
                        "2020-07-21",
                        "2020-07-24",
                        "2020-07-25",
                    ],
                    datasets: [
                        {
                            label: "Trump",
                            borderColor: "white",
                            fill: false,
                            pointRadius: 0,
                            data: [
                                40,
                                20,
                                192,
                                391,
                                128,
                                40,
                                39,
                                102,
                                45,
                                180,
                                121,
                                50,
                            ],
                        },
                        {
                            label: "Election",
                            borderColor: "purple",
                            fill: false,
                            pointRadius: 0,
                            data: [
                                40,
                                120,
                                212,
                                79,
                                105,
                                40,
                                32,
                                380,
                                30,
                                220,
                                152,
                                101,
                            ],
                        },
                    ],
                };
            } finally {
                this.loading = false;
            }
        },
    },
    created() {
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