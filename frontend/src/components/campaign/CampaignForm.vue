<template>
    <v-form class="mx-4 text-center">
        <div class="mb-2 text-h6">Start a new ad campaign</div>
        <v-select
            :items="cluster_items"
            prepend-icon="$cluster"
            solo
            placeholder="Select target cluster"
        ></v-select>
        <v-file-input solo placeholder="Upload an image/video file" prepend-icon="$file"></v-file-input>
        <v-textarea
            solo
            rows="3"
            hide-details
            placeholder="Add some text content to the ad"
            prepend-icon="$text"
        ></v-textarea>

        <v-row class="mx-0" align="center">
            <div class="mr-4">Select target platforms</div>
            <v-checkbox class="mr-4" label="Facebook" value="Facebook"></v-checkbox>
            <v-checkbox class="mr-4" label="Twitter" value="Twitter"></v-checkbox>
            <v-checkbox label="YouTube" value="YouTube"></v-checkbox>
        </v-row>

        <v-btn class="mt-5" type="submit" color="secondary">Create Ad</v-btn>
    </v-form>
</template>

<script>
import clusters from "@/data/clusters";

export default {
    data() {
        return {
            clusters,
        };
    },
    computed: {
        cluster_items() {
            let arr = [];
            this.clusters.forEach(function (cluster) {
                arr.push(cluster.name);
            });
            return arr;
        },
    },
};
</script>

<style>
</style>