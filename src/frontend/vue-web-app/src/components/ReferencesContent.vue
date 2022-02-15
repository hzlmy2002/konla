<template>
    <h2>References</h2>
    <div v-for="(reference, index) in content" :key="reference" class="ref-section mb-3">
        <!-- Index + 1 to start counting from 1 -->
        <h5 class="ref-index">[{{ index+1 }}]</h5>
        <p class="ref-content">{{ reference }}</p>
    </div>
</template>

<script>
export default {
    name: "ReferencesContent",
    props: {
        content: Object
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
