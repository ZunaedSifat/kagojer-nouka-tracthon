<template>
    <v-app id="#app">
        <navigation-bar></navigation-bar>
        <navigation-drawer></navigation-drawer>
        <v-main>
            <router-view></router-view>
        </v-main>
    </v-app>
</template>

<script>
export default {
    name: "App",
    components: {
        "navigation-bar": () =>
            import(
                /* webpackChunkName: "navigation" */ "@/components/navigation/NavigationBar"
            ),
        "navigation-drawer": () =>
            import(
                /* webpackChunkName: "navigation" */ "@/components/navigation/NavigationDrawer"
            ),
    },
};
</script>
