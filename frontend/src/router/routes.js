const routes = [{
        path: "/",
        name: "Home",
        component: () =>
            import ('@/views/Dashboard.vue')
    },
    {
        path: "/login",
        name: "Login",
        component: () =>
            import ('@/views/Login.vue')
    },
    {
        path: "/dashboard",
        name: "Dashboard",
        component: () =>
            import ('@/views/Dashboard.vue')
    },
    {
        path: "/keywords/:word",
        props: true,
        component: () =>
            import ('@/views/Keyword.vue')
    },
    {
        path: "/clusters/:cluster",
        props: true,
        component: () =>
            import ('@/views/Cluster.vue')
    },
    {
        path: "/ad-campaign",
        name: "Ad Campaign",
        component: () =>
            import ('@/views/Campaign.vue')
    },
    {
        path: "/profile",
        name: "Profile",
        component: () =>
            import ('@/views/Dashboard.vue')
    }
];

export default routes;