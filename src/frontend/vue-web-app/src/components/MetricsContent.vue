<template>
    <div v-if="errors">
        <ErrorContent  :errors-content="errors" />
    </div>
    <div v-else>
        <p><strong>Words:</strong> {{ wordCount }}</p>
        <p><strong>Reading Time:</strong> {{ readingTimeFormatted }}</p>
        <p><strong>Speaking Time:</strong> {{ speakingTimeFormatted }}</p>
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
</style>
