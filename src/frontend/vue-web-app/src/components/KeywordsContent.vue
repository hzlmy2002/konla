<template>
    <div v-if="errors">
        <ErrorContent  :errors-content="errors" />
    </div>
    <div v-else>
        <div class="row parameter-selection justify-content-center py-2">
            <!-- Number of keywords -->
            <div class="col-auto my-2">
                <div class="input-group input-group-sm mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text" id="inputGroup-sizing-sm">Number of keywords</span>
                  </div>
                  <input ref="numKeywordsInput" class="form-control" aria-label="Small"
                    aria-describedby="inputGroup-sizing-sm"
                    type="number" min="1" max="100"
                    name="num-keywords"
                    v-model.number="numKeywords">
                </div>
            </div>

            <!-- Ignore Case -->
            <div class="col-auto  my-3">
                <div class="form-check form-switch">
                  <input ref="ignoreCaseInput"
                    class="form-check-input" type="checkbox"
                    role="switch" id="flexSwitchCheckDefault"
                    v-model="ignoreCaseValue"
                    v-on:change="updateKeywordsData()"/>
                  <label class="form-check-label" for="flexSwitchCheckDefault">
                      Ignore Case
                  </label>
                </div>
            </div>

            <!-- Extract Lemma -->
            <div class="col-auto  my-3">
                <div class="form-check form-switch">
                  <input ref="extractLemmaInput"
                    class="form-check-input" type="checkbox"
                    role="switch" id="flexSwitchCheckDefault"
                    v-model="extractLemmaValue"
                    v-on:change="updateKeywordsData()"/>
                  <label class="form-check-label" for="flexSwitchCheckDefault">
                      Extract Lemma
                  </label>
                </div>
            </div>
        </div>
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
                <!-- Check index is less than maximum number of keywords -->
                <template v-if="(index+1) <= numKeywords">
                    <th scope="row">{{ index+1 }}</th>
                    <td>{{ keyword }}</td>
                    <td class="frequence-val">{{ frequency }}</td>
                </template>
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
            numKeywords: 100, // Default num of keywords is 100
            ignoreCaseValue: false,
            extractLemmaValue: false,
            errors: this.content.errors
        }
    },

    methods: {
        async updateKeywordsData() {
            // Parameters for keyword analysis
            const parameters = {
                "max": 100,
                "ignorecase": this.ignoreCaseValue,
                "extractlemma": this.extractLemmaValue,
            }

            const CONFIG = {
                method: "GET",
                mode: "cors",
                credentials: "include",
            };

            const domain = "https://" + window.location.hostname;
            const URL = domain + "/api/v1/keywords?" +
                new URLSearchParams(parameters).toString();

            const GET_Object = await fetch(URL, CONFIG);
            const response = await GET_Object.json();

            // Check response was successful
            if (response.current_status === 1) {
                const result = response.result;

                // Sets the result response as the content for the keywords table
                this.keywordsData = result.keywords;
            }
        },
    }
};
</script>

<style scoped>
    .frequence-val {
        font-family: 'Oswald', sans-serif;
    }

    .form-control {
        box-shadow: none;
        border: 0;
        border-radius: 5px;
    }

    .input-group-text {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
    }

    .parameter-selection {
        background-color: #B0BEC5;
        border-radius: 8px;
    }
</style>
