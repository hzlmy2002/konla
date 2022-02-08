<template>
    <KonlaHeader />
    <div class="container-fluid">
        <h1>Analysis View</h1>
        <button class="btn btn-primary" type="button" name="button" @click="redirectToUpload()">Go to Upload</button>
    </div>
</template>

<script>
import KonlaHeader from "@/components/Header.vue";

export default {
    components: {
        KonlaHeader
    },

    methods: {
        redirectToUpload(){
           this.$router.push('/');
        }
    }
}
</script>

<style scoped>

</style>
