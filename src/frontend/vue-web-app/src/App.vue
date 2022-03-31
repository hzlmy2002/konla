<!-- AUTHOR: Suraj Kothari -->
<template>
    <router-view />
</template>

<script>
export default {
    mounted() {
        // Add event listeners for window to prevent default opening of a file
        window.addEventListener("dragover", function(e) { e.preventDefault(); }, false);
        window.addEventListener("drop", function(e) { e.preventDefault(); }, false);
    }
}
</script>

<style>
/* Fonts: Poppins, Roboto */
@import url('https://fonts.googleapis.com/css2?family=Oswald&family=Poppins&family=Roboto&display=swap');

body {
    background-color: #ECEFF1;
    font-family: 'Roboto', sans-serif;
}

.error-text {
    color: #F44336;
    font-weight: bold;
    font-size: 20px;
}
</style>
