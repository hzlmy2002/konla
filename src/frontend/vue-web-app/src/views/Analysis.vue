<template>
    <PageHeader />
    <div class="container-fluid mt-4">
        <p class="text-center error-text" :class="{'d-none': hideAnalysisError}">Error: Analysis process failed to start</p>
        <div class="row mb-5 px-5">
            <div class="col-lg-3 col-md-4 col-sm-12 mb-md-0 mb-5 px-4 py-3 sidebar">
                <div v-for="(isSelected, feature) in analysisFeaturesSelected" :key="feature">
                    <!-- If feature is selected (its value is 1) -->
                    <div :ref="feature + 'AnalysisTab'"
                         class="row d-flex justify-content-between mb-md-4 mb-3 px-2 py-3 align-items-center analysis-tab"
                         :class="{
                             'completed-tab': analysisFeaturesCompleted.includes(feature),
                             'error-tab': analysisFeaturesError.includes(feature),
                             'active': analysisTabSelected === feature  }"

                         v-if="isSelected" @click="
                            analysisFeaturesCompleted.includes(feature) ||
                            analysisFeaturesError.includes(feature)
                            ? analysisTabSelected = feature : null">

                        <h6 class="col-auto analysis-feature-label" @click="extractTextSectionShow">
                            {{ this.analysisFeaturesMap[feature] }}
                        </h6>

                        <!-- Hide loading icon if feature is completed or has errors -->
                        <LoadingIcon :ref="feature + 'LoadingIcon'" class="col-auto"
                            :class="{
                                'd-none': analysisFeaturesCompleted.includes(feature) ||
                                analysisFeaturesError.includes(feature)}" />

                        <!-- Hide error icon if feature is not in error list -->
                        <span :ref="feature + 'ErrorIcon'" class="col-auto material-icons"
                            :class="{'d-none': !analysisFeaturesError.includes(feature)}">
                            error
                        </span>
                    </div>
                </div>
            </div>

            <div class="col-lg-9 col-md-8 col-sm-12 px-5 py-3 content-section">
                <WholeContent v-if="analysisTabSelected === 'whole'" :content="analysisFeaturesContent.whole" />
                <PartialContent v-if="analysisTabSelected === 'partial'" :content="analysisFeaturesContent.partial" />
                <KeywordsContent v-if="analysisTabSelected === 'keywords'" :content="analysisFeaturesContent.keywords" />
                <RefsContent v-if="analysisTabSelected === 'refs'" :content="analysisFeaturesContent.refs" />
                <MetadataContent v-if="analysisTabSelected === 'metadata'" :content="analysisFeaturesContent.metadata" />
                <MetricsContent v-if="analysisTabSelected === 'metrics'" :content="analysisFeaturesContent.metrics" />
            </div>
        </div>
    </div>
    <PageFooter />
</template>

<script>
    import PageHeader from "@/components/Header.vue";
    import PageFooter from "@/components/Footer.vue";
    import LoadingIcon from "@/components/LoadingIcon.vue";

    import WholeContent from "@/components/WholeContent.vue";
    import PartialContent from "@/components/PartialContent.vue";
    import KeywordsContent from "@/components/KeywordsContent.vue";
    import RefsContent from "@/components/RefsContent.vue";
    import MetadataContent from "@/components/MetadataContent.vue";
    import MetricsContent from "@/components/MetricsContent.vue";

    export default {
        components: {
            PageHeader,
            PageFooter,
            LoadingIcon,

            WholeContent,
            PartialContent,
            KeywordsContent,
            RefsContent,
            MetadataContent,
            MetricsContent
        },

        props: {
            analysisFeaturesJSONString: String
        },

        data() {
            return {
                mainloop: null,

                hideAnalysisError: true,

                analysisFeaturesMap: {
                    "whole": "Whole Paper Summarisation",
                    "partial": "Partial Paper Summarisation",
                    "keywords": "Keyword Extraction",
                    "refs": "References Extraction",
                    "metadata": "Metadata Extraction",
                    "metrics": "Calculate Metrics",
                },

                // The set of features selected during upload
                analysisFeaturesSelected: {},

                // The current tab that is active
                analysisTabSelected: "",

                // The features that haven't returned data yet
                analysisFeaturesNotCompleted: [],

                // The features where data has been received
                analysisFeaturesCompleted: [],

                // The features which returned an error
                analysisFeaturesError: [],

                // The data from each feature
                analysisFeaturesContent: {},

                analysisFeaturesErrors: {}
            }
        },

        created() {
            // If user is on analysis page without having selected the analysis
            // features, redirect them to the main site
            if (this.analysisFeaturesJSONString === undefined) {
                this.$router.push('/');
            } else {
                // Parse the string passed as a prop
                const analysisFeaturesObject = JSON.parse(this.analysisFeaturesJSONString);
                this.analysisFeaturesSelected = analysisFeaturesObject;

                // Initialise list of not completed features
                for (const [feature, value] of Object.entries(analysisFeaturesObject)) {
                    // Check if analysis feature is selected
                    if (value === 1) {
                        this.analysisFeaturesNotCompleted.push(feature);
                    }
                }

                this.startAnalysis();
            }
        },

        mounted() {
            // Call function continuously
            this.mainloop = window.setInterval(() => {
                console.log("Fetching data...");
                this.getAnalysisFeaturesData();
            }, 1000);
        },

        watch: {
            // Watch for changes to the array
            analysisFeaturesNotCompleted: {
                handler: function(array) {
                    if (array.length === 0) {
                        // Stop main loop
                        clearInterval(this.mainloop);
                    }
                },

                deep: true  // Checks changes to array element s
            }
        },

        methods: {
            async startAnalysis() {
                /* Starts the analysis process on the backend */

                const CONFIG = {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                    },
                    mode: "cors",
                    credentials: "include",
                    // URL encode the analysis features object
                    body: new URLSearchParams(this.analysisFeaturesSelected)
                };

                const URL = "http://localhost:5000/api/v1/upload/start";
                const getObject = await fetch(URL, CONFIG);
                const response = await getObject.json();

                // Check if analysis process start failed
                if (response.current_status === 0) {
                    // Show analysis error message
                    this.hideAnalysisError = false;
                    // Stop main loop
                    clearInterval(this.mainloop);
                }
            },

            async getAnalysisFeaturesData() {
                /* Fetches the data from each analysis feature process */

                const URL_MAP = {
                    "whole": "http://localhost:5000/api/v1/summarisation/whole",
                    "partial": "http://localhost:5000/api/v1/summarisation/partial",
                    "keywords": "http://localhost:5000/api/v1/keywords",
                    "refs": "http://localhost:5000/api/v1/info/refs",
                    "metadata": "http://localhost:5000/api/v1/info/metadata",
                    "metrics": "http://localhost:5000/api/v1/info/metrics",
                }

                for (const feature of this.analysisFeaturesNotCompleted) {
                    const CONFIG = {
                        method: "GET",
                        credentials: "include",
                    };
                    const URL = URL_MAP[feature];
                    const getObject = await fetch(URL, CONFIG);
                    const response = await getObject.json();

                    switch (response.current_status) {
                        // Feature completed with errors
                        case 0: {
                            const errors = response.errors;
                            // Mark the analysis feature tab to indicate an error
                            this.markAnalysisFeatureAsError(feature);
                            // Sets the content to be an object containing the errors
                            this.analysisFeaturesContent[feature] = {"errors": errors};
                            break;
                        }

                        // Feature completed successfully
                        case 1: {
                            const result = response.result;
                            // Mark the analysis feature tab as completed
                            this.markAnalysisFeatureAsCompleted(feature);
                            // Sets the result response as the content for that feature
                            this.analysisFeaturesContent[feature] = result;
                            break;
                        }
                    }
                }
            },

            markAnalysisFeatureAsCompleted(feature) {
                const indexOfFeature = this.analysisFeaturesNotCompleted.indexOf(feature);
                if (indexOfFeature > -1) {
                    // Remove feature from not completed array
                    this.analysisFeaturesNotCompleted.splice(indexOfFeature, 1);
                    this.analysisFeaturesCompleted.push(feature);
                }
            },

            markAnalysisFeatureAsError(feature) {
                const indexOfFeature = this.analysisFeaturesNotCompleted.indexOf(feature);
                if (indexOfFeature > -1) {
                    // Remove feature from not completed array
                    this.analysisFeaturesNotCompleted.splice(indexOfFeature, 1);
                    this.analysisFeaturesError.push(feature);
                }
            }
        }
    }
</script>

<style scoped>
    .content-section {
        height: 75vh;
        overflow-y: auto;
    }

    .sidebar {
        background-color: #eceff1;
        border-radius: 16px;
        box-shadow: 0px 0px 20px -4px #263238;
    }

    .analysis-tab {
        cursor: progress;
        border-radius: 8px;
        background-color: #FFD54F;
    }

    .analysis-tab a {
        text-decoration: none;
        color: #000;
    }

    .analysis-icon {
        font-size: 16px;
    }

    .completed-tab {
        background-color: #8BC34A;
        cursor: pointer;
    }

    .completed-tab:hover {
        background-color: #7CB342;
    }

    .error-tab {
        background-color: #F44336;
        cursor: pointer;
    }

    .error-tab:hover {
        background-color: #E53935;
    }

    .active {
        border: 4px solid #212121;
    }

    .analysis-feature-label {
        max-width: 50%;
        font-weight: bold;
        margin: 0;
        user-select: none;
    }

    .frequence-val {
        font-family: 'Oswald', sans-serif;
    }
</style>
