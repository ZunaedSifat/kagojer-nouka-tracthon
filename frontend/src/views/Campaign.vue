<template>
    <v-row>
        <v-col cols="7">
            <campaign-form></campaign-form>
        </v-col>
        <v-col cols="5">
            <campaign-list></campaign-list>
        </v-col>
    </v-row>
</template>

<script>
export default {
    components: {
        "campaign-form": () => import("@/components/campaign/CampaignForm"),
        "campaign-list": () => import("@/components/campaign/CampaignList"),
    },
};
</script>

<style>
</style>