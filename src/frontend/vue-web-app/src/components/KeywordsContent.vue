<template>
    <div v-if="errors">
        <ErrorContent  :errors-content="errors" />
    </div>
    <div v-else>
        <table class="table w-50">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Keyword</th>
              <th scope="col">Frequency</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(frequency, keyword, index) in keywordsData" :key="keyword">
                <!-- Index + 1 to start counting from 1 -->
                <th scope="row">{{ index+1 }}</th>
                <td>{{ keyword }}</td>
                <td class="frequence-val">{{ frequency }}</td>
            </tr>
          </tbody>
        </table>
    </div>

</template>

<script>
import ErrorContent from "@/components/ErrorContent.vue";
export default {
    name: "KeywordContent",

    components: {
        ErrorContent
    },

    props: {
        content: Object
    },

    data() {
        return {
            keywordsData: this.content.keywords,
            errors: this.content.errors
        }
    }
};
</script>

<style scoped>
    .frequence-val {
        font-family: 'Oswald', sans-serif;
    }
</style>
