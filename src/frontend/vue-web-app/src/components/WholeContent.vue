<template>
    <div v-if="errors">
        <ErrorContent  :errors-content="errors" />
    </div>
    <div v-else>
        <p>{{ summary }}</p>
    </div>
</template>

<script>
import ErrorContent from "@/components/ErrorContent.vue";
export default {
    name: "WholeContent",

    components: {
        ErrorContent
    },

    props: {
        content: Object
    },

    data() {
        return {
            summary: this.content.whole_summarisation,
            errors: this.content.errors
        }
    }
};
</script>
