
<script>
import { Line } from "vue-chartjs";

export default {
    extends: Line,
    props: {
        chart_data: {
            type: Object,
            default: null,
        },
    },
    mounted() {
        // Overwriting base render method with actual data.
        this.renderChart(this.chart_data, {
            legend: {
                labels: {
                    fontColor: "white",
                    fontStyle: "bold",
                },
            },
            tooltips: {
                enabled: false,
            },
            layout: {
                padding: 20,
            },
            animation: {
                duration: 2000,
            },
            scales: {
                xAxes: [
                    {
                        gridLines: {
                            display: false,
                            drawBorder: false,
                        },
                        ticks: {
                            maxRotation: 0,
                            minRotation: 0,
                            fontColor: "white",
                        },
                    },
                ],
                yAxes: [
                    {
                        gridLines: {
                            color: "white",
                            lineWidth: 0.5,
                            drawBorder: false,
                            borderDash: [2, 2],
                        },
                        ticks: {
                            fontColor: "white",
                        },
                    },
                ],
            },
        });
    },
};
</script>

<style>
</style>