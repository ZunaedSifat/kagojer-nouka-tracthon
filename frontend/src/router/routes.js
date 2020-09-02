const routes = [{
        path: "/",
        name: "Home",
        component: () =>
            import ('@/views/Home.vue')
    },
    {
        path: "/dashboard",
        name: "Dashboard",
        component: () =>
            import ('@/views/Dashboard.vue')
    },
    {
        path: "/profile",
        name: "Profile",
        component: () =>
            import ('@/views/Dashboard.vue')
    }
];

export default routes;