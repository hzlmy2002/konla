<!-- AUTHOR: Suraj Kothari -->
<template>
    <div v-if="errors">
        <ErrorContent  :errors-content="errors" />
    </div>
    <div v-else>
        <div v-for="(summaryContent, summaryHeading) in summariesList" :key="summaryHeading" class="partial-summary-section">
            <div class="px-3 summary-heading">
                <h3>{{ summaryHeading }}</h3>
            </div>
            <p>{{ summaryContent }}</p>
        </div>
    </div>
</template>

<script>
import ErrorContent from "@/components/ErrorContent.vue";
export default {
    name: "PartialContent",

    components: {
        ErrorContent
    },

    props: {
        content: Object
    },

    data() {
        return {
            summariesList: this.content.partial_summarisation,
            errors: this.content.errors
        }
    }
};
</script>

<style scoped>
    .partial-summary-section {
        border-bottom: 3px solid #BDBDBD;
        margin-bottom: 2rem;
    }

    .summary-heading {
        border-left: 10px solid #263238;
    }
</style>
