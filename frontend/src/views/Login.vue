<template>
    <v-card>
        <v-form ref="form" v-model="valid">
            <v-col cols="12" class="py-0">
                <v-subheader>E-mail</v-subheader>
                <v-text-field v-model="email" :rules="rules.required" filled dense></v-text-field>
            </v-col>

            <v-col cols="12" class="py-0">
                <v-subheader>Password</v-subheader>
                <v-text-field
                    filled
                    dense
                    v-model="password"
                    :rules="rules.required"
                    type="password"
                ></v-text-field>
            </v-col>

            <v-col cols="12">
                <loading-button text="LOG IN" :loading="loading" @click="login"></loading-button>
            </v-col>
        </v-form>
    </v-card>
</template>

<script>
export default {
    components: {
        "loading-button": () =>
            import(
                /* webpackChunkName: "common" */ "@/components/common/LoadingButton"
            ),
    },
    data() {
        return {
            email: null,
            password: null,
            valid: false,
            loading: false,
            rules: {
                required: [(v) => !!v || "This field is required"],
            },
        };
    },
    methods: {
        async login() {
            if (this.$refs.form.validate()) {
                this.loading = true;
                const params = {
                    grant_type: "password",
                    client_id: process.env.VUE_APP_CLIENT_ID,
                    client_secret: process.env.VUE_APP_CLIENT_SECRET,
                    username: this.email,
                    password: this.password,
                };
                try {
                    await this.$store.dispatch(
                        "auth/loginWithCredentials",
                        params
                    );
                    // await this.$store.dispatch(
                    //     "profile/fetchCurrentUserProfile"
                    // );
                    // this.changeRoute();
                } catch (error) {
                    this.loading = false;
                }
            }
        },
    },
};
</script>