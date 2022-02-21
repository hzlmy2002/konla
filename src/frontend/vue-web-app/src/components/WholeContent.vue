<template>
    <p>{{ wholeSummarisation }}</p>
</template>

<script>
export default {
    name: "WholeContent",

    props: {
        content: Object
    },

    data() {
        return {
            wholeSummarisation: this.content.summarisation
        }
    }
};
</script>

<style scoped>
</style>
