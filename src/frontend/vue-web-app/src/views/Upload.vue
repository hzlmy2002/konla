<template>
    <KonlaHeader />
    <div class="container-fluid">
        <h1>Upload View</h1>
        <button class="btn btn-primary" type="button" name="button" @click="redirectToAnalysis()">Go to Analysis</button>
    </div>
</template>

<script>
import KonlaHeader from "@/components/Header.vue";

export default {
    components: {
        KonlaHeader
    },

    methods: {
        redirectToAnalysis(){
           this.$router.push('/analysis');
        }
    }
}
</script>

<style scoped>

</style>
