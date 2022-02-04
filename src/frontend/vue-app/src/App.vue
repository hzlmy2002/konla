<template>
    <div id="test">
        <p>{{  hello_message_vue }}</p>
        <p>{{  hello_message_flask }}</p>
        <button class="btn btn-primary" type="button" name="button" v-on:click="requestFlask">Get data from flask</button>
    </div>
</template>

<script>
export default {
    name: 'Test',
    data: function() {
        return {
            hello_message_vue: 'Hello from Vue!',
            hello_message_flask: ''
        }
    },

    methods: {
        requestFlask: async function(){
            const getResponse = await fetch("http://172.17.0.2:5000/analysis");
            const getObject = await getResponse.json();
            this.hello_message_flask = getObject.hello_message;
        }
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
</style>
