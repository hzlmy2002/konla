<!-- COMP0016-Team6-Suraj Kothari -->
<template>
    <h4>Errors</h4>
    <div v-for="(error, index) in errorsContent" :key="error">
        <p>{{ index+1 }}. {{ error }}</p>
    </div>
</template>

<script>
export default {
    name: "ErrorContent",

    props: {
        errorsContent: Object
    }
};
</script>

<style scoped>
    h4 {
        color: #D32F2F;
    }
</style>
