<template>
    <PageHeader />

    <div class="container w-75 py-5 px-4 upload-section">
        <h2 class="text-center display-5 mb-3 upload-title">Upload research paper</h2>
        <p class="text-center lead upload-text">Upload a PDF or a scanned image of a paper</p>
        <div ref="dragDropSection" class="p-5 drag-drop-section" v-bind:style="{ backgroundColor: dragDropBackgroundColor, outlineOffset: dragDropOutlineOffset }" @drop="fileDropped" @dragover="fileDragHover" @dragleave="noFileDragHover">
            <div class="text-center"><span class="material-icons upload-icon">description</span></div>
            <p class="text-center lead" style="color: #9E9E9E;">Drag and drop or <a class="upload-link" @click="this.$refs['fileInput'].click()">browse</a> your files</p>
            <p ref="uploadError" class="text-center lead error-text" v-bind:class="{ hidden: isHiddenError }">File uploaded is not a PDF or an image</p>
        </div>

        <form ref="uploadForm" action="/" method="post" enctype="multipart/form-data">
            <input ref="fileInput" type="file" name="fileInput" class="hidden" @change="updateUploadSection" />
            <div ref="analysisSelectionSection" class="mt-5 py-4 px-5 analysis-selection-section" v-bind:class="{ hidden: isHiddenAnalysis }">
                <p ref="fileUploadedText" class="text-center file-uploaded-text"><span v-html="fileUploadedText"></span></p>
                <h5><strong>Select analysis tools for the paper:</strong></h5>
                <!-- Analysis tools checkboxes -->
                <div class="form-check">
                    <!-- Set selectAllCheckboxes(num) argument to the number of tools -->
                    <input ref="selectAll" class="form-check-input" type="checkbox" @click="selectAllCheckboxes(6)" />
                    <label class="form-check-label" for="selectAll"><strong>Select all analysis tools</strong></label>
                </div>
                <!-- Analysis tools checkboxes -->
                <div class="form-check">
                    <input ref="analysisTool1" class="form-check-input" type="checkbox" value="whole_paper_summarisation" />
                    <label class="form-check-label" for="analysisTool1">Whole paper summarisation</label>
                </div>
                <div class="form-check">
                    <input ref="analysisTool2" class="form-check-input" type="checkbox" value="partial_paper_summarisation" />
                    <label class="form-check-label" for="analysisTool2">Partial paper summarisation</label>
                </div>
                <div class="form-check">
                    <input ref="analysisTool3" class="form-check-input" type="checkbox" value="keyword_extraction" />
                    <label class="form-check-label" for="analysisTool3">Keyword extraction</label>
                </div>
                <div class="form-check">
                    <input ref="analysisTool4" class="form-check-input" type="checkbox" value="extract_references" />
                    <label class="form-check-label" for="analysisTool4">Extract references</label>
                </div>
                <div class="form-check">
                    <input ref="analysisTool5" class="form-check-input" type="checkbox" value="extract_metadata" />
                    <label class="form-check-label" for="analysisTool5">Extract metadata</label>
                </div>
                <div class="form-check">
                    <input ref="analysisTool6" class="form-check-input" type="checkbox" value="calculate_metrics" />
                    <label class="form-check-label" for="analysisTool6">Calculate metrics</label>
                </div>

                <!-- Set checkSelection(num) argument to the number of tools -->
                <button class="btn btn-success mt-3 analysis-btn" type="button" name="analyseBtn" @click="checkSelection(6)">
                    <strong>Analyse Paper</strong>
                </button>
            </div>
        </form>
    </div>

    <PageFooter />
</template>

<script>
    import PageHeader from "@/components/Header.vue";
    import PageFooter from "@/components/Footer.vue";

    export default {
        data() {
            return {
                dragDropBackgroundColor: "#EEEEEE",
                dragDropOutlineOffset: "-10px",

                isHiddenError: true,
                isHiddenAnalysis: true,
                fileUploadedText: ""
             }
        },

        components: {
            PageHeader,
            PageFooter
        },

        methods: {
            redirectToAnalysis() {
               this.$router.push('/analysis');
            },

            // File drag/drop methods
            fileDragHover(ev) {
                ev.preventDefault();
                this.dragDropBackgroundColor = "#CFD8DC";
                this.dragDropOutlineOffset = "-20px";
            },

            noFileDragHover(ev) {
                ev.preventDefault();
                this.dragDropBackgroundColor = "#EEEEEE";
                this.dragDropOutlineOffset = "-10px";
            },

            fileDropped(ev) {
                ev.preventDefault();
                this.dragDropBackgroundColor = "#EEEEEE";
                this.dragDropOutlineOffset = "-10px";

                // Pass dropped files to file input
                this.$refs['fileInput'].files = ev.dataTransfer.files;
                this.updateUploadSection();
            },

            updateUploadSection() {
                //const filename = this.fileInput.files[0].name;
                const filename = this.$refs['fileInput'].files[0].name;
                const extension = filename.split('.').pop().toLowerCase();

                // Check extension is valid
                if (["pdf", "jpg", "png"].includes(extension)) {
                    // Hide error and show analysis selection section
                    this.isHiddenError = true;
                    this.isHiddenAnalysis = false;

                    this.fileUploadedText = "File uploaded: \
                        <span class='filename'>"
                        + filename + "</span>";
                } else {
                    // Show error and hide analysis selection section
                    this.isHiddenError = false;
                    this.isHiddenAnalysis = true;
                }
            },

            selectAllCheckboxes(numTools) {
                // If select all is checked
                if(this.$refs['selectAll'].checked) {
                    // Check all checkboxes
                    for (let i = 1; i < numTools + 1; i++) {
                        const checkbox = "analysisTool" + i;
                        this.$refs[checkbox].checked = true;
                    }
                } else {
                    // Uncheck all checkboxes
                    for (let i = 1; i < numTools + 1; i++) {
                        const checkbox = "analysisTool" + i;
                        this.$refs[checkbox].checked = false;
                    }
                }
            },

            checkSelection(numTools) {
                // Check that at least one checkboxe is checked
                for (let i = 1; i < numTools + 1; i++) {
                    const checkbox = "analysisTool" + i;
                    if (this.$refs[checkbox].checked) {
                        // Submit form
                        this.$refs['uploadForm'].submit();
                    }
                }
            }
        }
    }
</script>

<style scoped>
    .upload-section {
        background-color: #FFF;
        border-radius: 8px;
    }

    .upload-title {
        font-family: 'Poppins', sans-serif;
        font-weight: bold;
    }

    .upload-text {
        color: #616161;
        font-weight: bold;
    }

    .error-text {
        color: #F44336;
        font-weight: bold;
        font-size: 20px;
    }

    .drag-drop-section {
        background-color: #EEEEEE;
        border-radius: 8px;
        outline: 2px dashed #BDBDBD;
        outline-offset: -10px;
        transition: outline-offset .15s ease-in-out, background-color .15s linear;
    }

    .upload-icon {
        color: #90A4AE;
        font-size: 100px;
    }

    .upload-link {
        cursor: pointer;
        color: #2196F3;
    }

    .analysis-selection-section {
        background-color: #EEEEEE;
        border-radius: 8px;
    }

    .file-uploaded-text {
        color: #66BB6A;
        font-size: 20px;
    }

    .filename {
        font-size: 18px;
        font-weight: bold;
        font-family: 'Poppins', sans-serif;
    }
</style>
