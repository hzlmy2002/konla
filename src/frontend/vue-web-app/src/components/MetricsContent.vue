<template>
    <div v-if="errors">
        <ErrorContent  :errors-content="errors" />
    </div>
    <div v-else>
        <div class="row">
            <div class="col metrics-content px-5 pt-5 mx-4 mb-5 d-flex flex-column justify-content-center">
                <h2 class="metrics-data mt-auto mb-5">{{ wordCount }}</h2>
                <h5 class="metrics-label mt-auto">Words</h5>
            </div>
            <div class="col metrics-content px-5 pt-5 mx-4 mb-5 d-flex flex-column justify-content-center">
                <h2 class="metrics-data mt-auto mb-5">{{ readingTimeFormatted }}</h2>
                <h5 class="metrics-label mt-auto">Reading Time</h5>
            </div>
            <div class="col metrics-content px-5 pt-5 mx-4 mb-5 d-flex flex-column justify-content-center">
                <h2 class="metrics-data mt-auto mb-5">{{ speakingTimeFormatted }}</h2>
                <h5 class="metrics-label mt-auto">Speaking Time</h5>
            </div>
        </div>

    </div>
</template>

<script>
import ErrorContent from "@/components/ErrorContent.vue";
export default {
    name: "MetricsContent",

    components: {
        ErrorContent
    },

    props: {
        content: Object
    },

    created() {
        if (this.errors === undefined) {
            this.getWordCount();
            this.formatReadingTime();
            this.formatSpeakingTime();
        }
    },

    data() {
        return {
            metricsData: this.content.metrics,
            readingTimeFormatted: 0,
            speakingTimeFormatted: 0,
            wordCount: 0,
            errors: this.content.errors
        }
    },

    methods: {
        getWordCount() {
            this.wordCount = this.metricsData.wordCount;
        },

        formatReadingTime() {
            let readingTimeMinutes = Math.floor(this.metricsData.readingTime / 60);
            let readingTimeSeconds = this.metricsData.readingTime % 60;
            this.readingTimeFormatted = readingTimeMinutes + "min " + readingTimeSeconds + "sec";
        },

        formatSpeakingTime() {
            let speakingTimeMinutes = Math.floor(this.metricsData.speakingTime / 60);
            let speakingTimeSeconds = this.metricsData.speakingTime % 60;
            this.speakingTimeFormatted = speakingTimeMinutes + "min " + speakingTimeSeconds + "sec";
        },
    }
};
</script>

<style scoped>
    .metrics-content {
        background-color: #78909C;
        border-radius: 8px;
        text-align: center;
    }

    .metrics-data {
        font-weight: bold;
        color: #CFD8DC;
        font-family: 'Poppins', sans-serif;
        white-space: nowrap;
    }

    .metrics-label {
        font-weight: bold;
        color: #263238;
    }

</style>
