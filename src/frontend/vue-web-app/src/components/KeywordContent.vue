<template>
    <table class="table w-50">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Keyword</th>
          <th scope="col">Frequency</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(frequency, keyword, index) in content" :key="keyword">
            <!-- Index + 1 to start counting from 1 -->
            <th scope="row">{{ index+1 }}</th>
            <td>{{ keyword }}</td>
            <td class="frequence-val">{{ frequency }}</td>
        </tr>
      </tbody>
    </table>
</template>

<script>
export default {
    name: "KeywordContent",

    props: {
        content: Object
    }
};
</script>

<style scoped>
    .frequence-val {
        font-family: 'Oswald', sans-serif;
    }
</style>
