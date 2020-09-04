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
                    :labels="chart_data.labels"
                    :value="chart_data.counts"
                ></v-sparkline>
            </v-container>
        </v-sheet>

        <v-card-title class="pt-0" style="color: var(--v-primary-base)">Cluster History</v-card-title>
    </v-card>
</template>

<script>
export default {
    props: {
        chart_data: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            loading: false,
        };
    },
};
</script>

<style scoped>
.v-sheet--offset {
    top: -24px;
    position: relative;
}
</style>