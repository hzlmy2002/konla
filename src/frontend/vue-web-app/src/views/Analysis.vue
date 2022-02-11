<template>
    <PageHeader />
    <div class="container-fluid">
        <div class="row mb-5 px-5">
            <div class="col-lg-3 col-md-4 col-sm-12 mb-md-0 mb-5 p-5 px-4 sidebar">
                <div v-for="(isSelected, feature) in analysisFeatures" :key="feature">
                    <!-- If feature is selected (its value is 1) -->
                    <div class="mb-md-4 mb-3 analysis-tab" v-if="isSelected">
                        <h6 class="analysis-feature-label text-center" @click="extractTextSectionShow">{{ this.analysisFeaturesMap[feature] }}</h6>
                    </div>
                </div>
                <!-- <div id="extractTextTab" class="mb-5 analysis-tab active">
                    <h5 class="analysis-feature-label text-center" @click="extractTextSectionShow">Extracted text</h5>
                </div>
                <div id="extractKeywordsTab" class="mb-5 analysis-tab">
                    <h5 class="analysis-feature-label text-center" @click="extractKeywordsSectionShow">Keyword extraction</h5>
                </div> -->
            </div>

            <div class="col-lg-9 col-md-8 col-sm-12 px-5 content-section">
                <h1>Hello</h1>
                <div class="extracted-text-section">
                    <p v-for="(n, index) in 15" :key="index">Lorem ipsum...</p>
                </div>
            </div>
        </div>
    </div>
    <PageFooter :footer-style="footerStyle" />
</template>

<script>
    import PageHeader from "@/components/Header.vue";
    import PageFooter from "@/components/Footer.vue";

    export default {
        components: {
            PageHeader,
            PageFooter
        },

        props: {
            analysisFeaturesJSONString: String
        },

        data() {
            return {
                footerStyle: {
                    position: "absolute",
                    bottom: 0,
                    right: 0,
                    left: 0,
                },

                analysisFeatures: {},

                analysisFeaturesMap: {
                    "whole": "Whole paper summarisation",
                    "partial": "Partial paper summarisation",
                    "keyword": "Keyword extraction",
                    "refs": "References extraction",
                    "meta": "Metadata extraction",
                    "metrics": "Calculate metrics",
                }
            }
        },

        created() {
            // If user is on analysis page without having selected the analysis
            // features, redirect them to the main site
            if (this.analysisFeaturesJSONString === undefined) {
                this.$router.push('/');
            } else {
                // Parse the string passed as a prop
                this.analysisFeatures = JSON.parse(this.analysisFeaturesJSONString);
            }
        },

        methods: {
            redirectToUpload(){
               this.$router.push('/');
           },

           // extractTextSectionShow() {
           //     document.getElementById("extractTextTab").classList.add("active");
           //     document.getElementById("extractTextSection").classList.remove("hidden");
           //     document.getElementById("extractKeywordsTab").classList.remove("active");
           //     document.getElementById("extractKeywordsSection").classList.add("hidden");
           // },
           //
           // extractKeywordsSectionShow() {
           //     document.getElementById("extractKeywordsTab").classList.add("active");
           //     document.getElementById("extractKeywordsSection").classList.remove("hidden");
           //     document.getElementById("extractTextTab").classList.remove("active");
           //     document.getElementById("extractTextSection").classList.add("hidden");
           // }
        }
    }
</script>

<style scoped>
    .content-section {
        height: 65vh;
        overflow-y: auto;
    }
    .sidebar {
        background-color: #263238;
        border-radius: 16px;
    }

    .analysis-tab {
        padding: 8px 4px;
        cursor: pointer;
        border-radius: 8px;
        background-color: #B0BEC5;
    }

    .analysis-tab:hover:not(.active) {
        background-color: #CFD8DC;
    }

    .analysis-tab a {
        text-decoration: none;
        color: #000;
    }

    .active {
        background-color: #FFCA28;
    }

    .analysis-feature-label {
        font-weight: bold;
        margin: 0;
        user-select: none;
    }

    .frequence-val {
        font-family: 'Oswald', sans-serif;
    }
</style>
