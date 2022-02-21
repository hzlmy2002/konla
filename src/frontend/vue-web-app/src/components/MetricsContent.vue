<template>
    <p><strong>Words:</strong> {{ wordCount }}</p>
    <p><strong>Reading Time:</strong> {{ readingTimeFormatted }}</p>
    <p><strong>Speaking Time:</strong> {{ speakingTimeFormatted }}</p>
</template>

<script>
export default {
    name: "MetricsContent",

    props: {
        content: Object
    },

    created() {
        this.formatReadingTime();
        this.formatSpeakingTime();
    },

    data() {
        return {
            metricsData: this.content.metrics,
            readingTimeFormatted: 0,
            speakingTimeFormatted: 0,
            wordCount: this.content.metrics.wordCount

            //readingTimeFormatted: this.formatReadingTime(),
            //speakingTimeFormatted: this.formatSpeakingTime(),
        }
    },

    methods: {
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
