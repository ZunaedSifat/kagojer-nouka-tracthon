<template>
    <v-card class="ma-4">
        <v-card-title class="pb-0">Cluster#1</v-card-title>
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
                    <v-card-actions class="pl-0 text-end">
                        <v-icon color="primary" class="mr-1">$up</v-icon>
                        <span>56%</span>

                        <v-icon color="secondary" class="mr-1">$down</v-icon>
                        <span>11%</span>

                        <v-divider vertical class="mx-4"></v-divider>

                        <v-chip outlined label color="secondary">120 articles</v-chip>

                        <v-divider vertical class="mx-4"></v-divider>

                        <span>text</span>
                    </v-card-actions>
                </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    data() {
        return {
            keywords: ["Donald", "Trump", "Election", "Covid", "Corruption"],
            colors: ["primary", "secondary", "pink", "blue", "purple"],
        };
    },
};
</script>

