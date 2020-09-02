<template>
    <v-navigation-drawer
        v-model="drawer"
        mobile-breakpoint="960"
        app
        dark
        width="260"
        v-bind="$attrs"
    >
        <template v-slot:img="props">
            <v-img gradient="#b993d6, #8ca6db" v-bind="props" />
        </template>

        <v-divider class="mb-1" />

        <v-list dense nav>
            <v-list-item to="/" exact>
                <v-list-item-avatar color="purple">logo</v-list-item-avatar>
                <v-list-item-content>
                    <v-list-item-title class="subtitle-1">Kagojer Nouka</v-list-item-title>
                </v-list-item-content>
            </v-list-item>

            <v-divider class="mb-2"></v-divider>

            <v-list-item v-for="item in nav_items" :key="item.title" :to="item.to" exact>
                <v-list-item-icon>
                    <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
export default {
    data() {
        return {
            nav_items: [
                {
                    icon: "$dashboard",
                    title: "Dashboard",
                    to: "/dashboard",
                },
                {
                    icon: "$profile",
                    title: "My Profile",
                    to: "/profile",
                },
            ],
        };
    },
    computed: {
        drawer: {
            get() {
                return this.$store.state.drawer;
            },
            set(val) {
                this.$store.commit("SET_DRAWER", val);
            },
        },
    },
};
</script>
