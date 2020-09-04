<template>
    <v-container class>
        <span class="title">
            Articles with keyword
            <span style="color: var(--v-primary-base)">#{{ word }}</span>
        </span>

        <v-list color="transparent">
            <v-list-item v-for="(article, index) in articles" :key="index" class="mb-4 px-0">
                <v-card>
                    <v-card-subtitle>{{ article.date }}</v-card-subtitle>
                    <v-card-text>{{ article.text }}</v-card-text>
                </v-card>
            </v-list-item>
        </v-list>
    </v-container>
</template>

<script>
export default {
    props: {
        word: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            articles: [
                {
                    date: "2020-09-01",
                    text: `That’s because those running older iterations of the wallet can no longer use this feature to mix their coins with users who have the newest version.

The Wasabi Wallet team hard-forked the wallet Thursday to address a vulnerability discovered by a team member at Trezor, a leading maker of hardware wallets. A hard fork is a code change that makes older versions of a software incompatible with newer ones.

The flaw’s discovery is another example of the open-source community’s camaraderie and cooperation. Developers are constantly tinkering to improve their peers’ software, and many vulnerabilities have been responsibly disclosed during these processes to patch flaws before they can be exploited by bad actors. (Sometimes, however, the disclosures by rival teams are less-than-cordial, as evidenced by the long-running tensions between Wasabi and rival Samourai Wallet.)`,
                },
                {
                    date: "2020-09-02",
                    text: `The result would be an incongruity between the total value of inputs made to the CoinJoin and the value of expected outputs. As a result, the coordinator would unwittingly “build a transaction that can’t be valid, since the sum of all inputs is less than the sum of all outputs,” according to Vejpustek’s analysis.

If the attack were pulled off, it would foil the CoinJoin, though it would not have given the attacker the ability to steal any coins nor could they deanonymize any peers in the mix.`,
                },
                {
                    date: "2020-08-30",
                    text: `Square stock has sold off some to start September, and investors do have lingering concerns. Specifically, there's concern about the health of the small and medium-sized business Square serves. And there are also questions about the company's Bitcoin-driven top-line growth.`,
                },
                {
                    date: "2020-08-31",
                    text: `Portnoy's tune toward crypto has been quite temperamental in recent weeks. He first said he knew little of Bitcoin and its related asset class. An educational meeting with crypto exchange co-founders Tyler and Cameron Winklevoss followed, leading to Portnoy allocating hundreds of thousands of dollars to crypto trading. He subsequently exited the industry after losing a small portion of his money.`,
                },
            ],
        };
    },
};
</script>

<style>
</style>