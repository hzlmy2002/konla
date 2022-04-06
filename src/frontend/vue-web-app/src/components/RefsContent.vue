<!-- COMP0016-Team6-Suraj Kothari -->
<template>
    <div v-if="errors">
        <ErrorContent  :errors-content="errors" />
    </div>
    <div v-else>
        <div v-for="(reference, index) in referencesList" :key="reference" class="ref-section mb-3">
            <!-- Index + 1 to start counting from 1 -->
            <h5 class="ref-index">[{{ index+1 }}]</h5>
            <p class="ref-content lead">{{ reference }}</p>
        </div>
    </div>
</template>

<script>
import ErrorContent from "@/components/ErrorContent.vue";
export default {
    name: "ReferencesContent",

    components: {
        ErrorContent
    },

    props: {
        content: Object
    },

    data() {
        return {
            referencesList: this.content.refs,
            errors: this.content.errors
        }
    }
};
</script>

<style scoped>
    .ref-section {
        border-bottom: 3px solid #BDBDBD;
    }

    .ref-index {
        font-weight: bold;
        font-family: serif;
    }

    .ref-content {
        font-family: serif;
    }
</style>
