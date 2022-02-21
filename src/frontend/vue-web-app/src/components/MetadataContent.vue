<!-- Reference: https://loading.io/css/ -->
<template>
    <div class="metadata-section">
        <div class="px-3 section-heading">
            <h3>Title and Subject</h3>
        </div>
        <h4><strong>{{ this.metadata.title }}</strong></h4>
        <h5 class="text-secondary">{{ this.metadata.subject }}</h5>
    </div>

    <div class="metadata-section">
        <div class="px-3 section-heading">
            <h3>Additional metadata</h3>
        </div>
        <p><strong>Creator: </strong>{{ this.metadata.creator }}</p>
        <p><strong>Producer: </strong>{{ this.metadata.producer }}</p>
    </div>

    <div class="metadata-section">
        <div class="d-flex px-3 section-heading">
            <h3>Authors</h3>
            <div class="dropdown mx-3">
                <button class="btn dropdown-toggle order-btn" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Order authors
                </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <button class="dropdown-item" href="#" @click="getAuthorsOriginal()">Original</button>
                    <button class="dropdown-item" href="#" @click="getAuthorsAscending()">Alphabetical (A-Z)</button>
                    <button class="dropdown-item" href="#" @click="getAuthorsDescending()">Alphabetical (Z-A)</button>
                </div>
            </div>
        </div>
        <p class="authors lead my-3">{{ authors }}</p>
    </div>

</template>

<script>
export default {
    name: "MetadataContent",

    props: {
        content: Object
    },

    created() {
        // Default: no sorting
        this.getAuthorsOriginal();
    },

    data() {
        return {
            metadata: this.content.metadata,
            authors: []
        }
    },

    methods: {
        getAuthorsOriginal() {
            this.authors = Array.from(this.metadata.authors).join(", ");
        },

        getAuthorsAscending() {
            const copy = Array.from(this.metadata.authors);
            this.authors = copy.sort().join(", ");
        },

        getAuthorsDescending() {
            const copy = Array.from(this.metadata.authors);
            this.authors = copy.sort().reverse().join(", ");
        }
    }
};
</script>

<style scoped>
    .metadata-section {
        border-bottom: 3px solid #BDBDBD;
        margin-bottom: 2rem;
    }
    .section-heading {
        border-left: 10px solid #263238;
    }

    .order-btn {
        color: #ECEFF1;
        background-color: #607D8B;
    }
</style>
