<template>
    <div class="container-fluid">
        <h1>Analysis View</h1>
        <button class="btn btn-primary" type="button" name="button" @click="redirectToUpload()">Go to Upload</button>
    </div>
</template>

<script>
export default {
    methods: {
        redirectToUpload(){
           this.$router.push('/');
        }
    }
}
</script>

<style scoped>

</style>
