<template>
    <p>{{ paritalSummarisation }}</p>
</template>

<script>
export default {
    name: "PartialContent",

    props: {
        content: Object
    },

    data() {
        return {
            paritalSummarisation: this.content.summarisation
        }
    }
};
</script>

<style scoped>
</style>
