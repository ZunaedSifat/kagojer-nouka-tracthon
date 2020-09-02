<template>
    <v-btn :loading="loading" block color="primary" @click="$emit('click')">
        {{ text }}
        <template #loader>
            {{ text }}
            <v-progress-linear absolute bottom color="accent" indeterminate></v-progress-linear>
        </template>
    </v-btn>
</template>

<script>
export default {
    props: {
        text: {
            type: String,
            default: "SUBMIT",
        },
        loading: {
            type: Boolean,
            default: false,
        },
    },
};
</script>
