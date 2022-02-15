<template>
    <PageHeader />
    <div class="container-fluid mt-4">
        <div class="row mb-5 px-5">
            <div class="col-lg-3 col-md-4 col-sm-12 mb-md-0 mb-5 px-4 py-3 sidebar">
                <div v-for="(isSelected, feature) in analysisFeatures" :key="feature">
                    <!-- If feature is selected (its value is 1) -->
                    <div :ref="feature + 'AnalysisTab'"
                         class="row mb-md-4 mb-3 px-2 py-3 align-items-center analysis-tab"
                         :class="{'completed': analysisFeaturesCompleted.includes(feature), 'active': analysisTabSelected == feature  }"
                         v-if="isSelected" @click="
                            analysisFeaturesCompleted.includes(feature)
                            ? analysisTabSelected = feature : null">
                        <h6 class="col-9 analysis-feature-label" @click="extractTextSectionShow">{{ this.analysisFeaturesMap[feature] }}</h6>
                        <LoadingIcon :ref="feature + 'LoadingIcon'" class="col" />
                    </div>
                </div>
            </div>

            <div class="col-lg-9 col-md-8 col-sm-12 px-5 py-3 content-section">
                <WholeContent v-if="analysisTabSelected == 'whole'" :content="analysisFeaturesContent.whole" />
                <PartialContent v-if="analysisTabSelected == 'partial'" :content="analysisFeaturesContent.partial" />
                <KeywordContent v-if="analysisTabSelected == 'keywords'" :content="analysisFeaturesContent.keywords" />
                <ReferencesContent v-if="analysisTabSelected == 'refs'" :content="analysisFeaturesContent.refs" />
                <MetadataContent v-if="analysisTabSelected == 'metadata'" :content="analysisFeaturesContent.metadata" />
                <MetricsContent v-if="analysisTabSelected == 'metrics'" :content="analysisFeaturesContent.metrics" />
            </div>
        </div>
    </div>
    <PageFooter :footer-style="footerStyle" />
</template>

<script>
    import PageHeader from "@/components/Header.vue";
    import PageFooter from "@/components/Footer.vue";
    import LoadingIcon from "@/components/LoadingIcon.vue";

    import WholeContent from "@/components/WholeContent.vue";
    import PartialContent from "@/components/PartialContent.vue";
    import KeywordContent from "@/components/KeywordContent.vue";
    import ReferencesContent from "@/components/ReferencesContent.vue";
    import MetadataContent from "@/components/MetadataContent.vue";
    import MetricsContent from "@/components/MetricsContent.vue";

    export default {
        components: {
            PageHeader,
            PageFooter,
            LoadingIcon,

            WholeContent,
            PartialContent,
            KeywordContent,
            ReferencesContent,
            MetadataContent,
            MetricsContent
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

                // Stores the analysis features that were chosen
                analysisFeatures: {},

                analysisFeaturesMap: {
                    "whole": "Whole Paper Summarisation",
                    "partial": "Partial Paper Summarisation",
                    "keywords": "Keyword Extraction",
                    "refs": "References Extraction",
                    "metadata": "Metadata Extraction",
                    "metrics": "Calculate Metrics",
                },

                analysisTabSelected: "",

                // List of features not yet completed. Continually request for
                // content from these features
                analysisFeaturesNotCompleted: [],

                analysisFeaturesCompleted: ["whole", "partial", "keywords",
                    "refs", "metadata", "metrics"],

                analysisFeaturesContent: {
                    "whole": "Whole summarised content",
                    "partial": "Partial summarised content",
                    "keywords": {"A": 10, "B": 6, "C": 3},
                    "refs": ["Mitchell, J.A. ‘How citation changed the research \
                             world’, The Mendeley, 62(9), p70-81",

                             "Mitchell, J.A. (2017) ‘Changes to citation formats \
                             shake the research world’, The Mendeley Telegraph \
                             (Weekend edition), 6 July, pp.9-12 pp.9-12 pp.9-12",

                             "Troy B.N. (2015) ‘Harvard citation rules’ in \
                             Williams, S.T. (ed.) A guide to citation rules. \
                             New York: NY Publishers, pp. 34-89",

                             "Mitchell, J.A. ‘How citation changed the research \
                                      world’, The Mendeley, 62(9), p70-81",

                                      "Mitchell, J.A. (2017) ‘Changes to citation formats \
                                      shake the research world’, The Mendeley Telegraph \
                                      (Weekend edition), 6 July, pp.9-12 pp.9-12 pp.9-12",

                                      "Troy B.N. (2015) ‘Harvard citation rules’ in \
                                      Williams, S.T. (ed.) A guide to citation rules. \
                                      New York: NY Publishers, pp. 34-89"],

                    "metadata": {
                        "Author": "Alice A, Bob B, David D",
                        "Creator": "",
                        "Producer": "",
                        "Subject": "Subheading of research paper",
                        "Title": "Title Of Research Paper"
                    },

                    "metrics": {
                        "wordcount": 1920,
                        "readingtime": "120",
                        "speakingtime": "243"
                    },
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

        mounted() {
            this.getAnalysisFeatureData();
        },

        methods: {
            redirectToUpload() {
               this.$router.push('/');
            },

            getAnalysisFeatureData() {
                this.markAnalysisFeatureCompleted("whole");
                this.markAnalysisFeatureCompleted("metadata");
                this.markAnalysisFeatureCompleted("metrics");
                this.markAnalysisFeatureCompleted("keywords");
                this.markAnalysisFeatureCompleted("partial");
                this.markAnalysisFeatureCompleted("refs");
            },

            markAnalysisFeatureCompleted(analysisFeature) {
                // Marks the analysis tab as completed and puts the data in the
                // corresponding content section
                const analysisTab = analysisFeature + "AnalysisTab"
                const loadingIcon = analysisFeature + "LoadingIcon"

                this.$refs[analysisTab][0].classList.add("completed");
                this.$refs[loadingIcon][0].$el.classList.add("d-none");
            }
        }
    }
</script>

<style scoped>
    .content-section {
        height: 65vh;
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

    .completed {
        background-color: #66BB6A;
        cursor: pointer;
    }

    .completed:hover {
        background-color: #4CAF50;
    }

    .active {
        border: 4px solid #000000;
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
