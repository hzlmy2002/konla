<template>
    <PageHeader />
    <div clas="container">
        <div class="container w-75 py-5 px-4 mb-5 upload-section">
            <h2 class="text-center display-5 mb-3 upload-title">Upload research paper</h2>

            <div class="mt-5 py-4 px-5 analysis-selection-section">
                <h5><strong>Select analysis features</strong></h5>
                <!-- Analysis features checkboxes -->
                <div class="form-check">
                    <!-- Set selectAllCheckboxes(num) argument to the number of featues -->
                    <input ref="selectAll" class="form-check-input" type="checkbox" @click="selectAllCheckboxes(6)" />
                    <label class="form-check-label" for="selectAll"><strong>Select all</strong></label>
                </div>
                <!-- Analysis featues checkboxes -->
                <div class="form-check">
                    <input ref="analysisTool1" class="form-check-input" type="checkbox" name="whole" />
                    <label class="form-check-label" for="analysisTool1">Whole Paper Summarisation</label>
                </div>
                <div class="form-check">
                    <input ref="analysisTool2" class="form-check-input" type="checkbox" name="partial" />
                    <label class="form-check-label" for="analysisTool2">Partial Paper Summarisation</label>
                </div>
                <div class="form-check">
                    <input ref="analysisTool3" class="form-check-input" type="checkbox" name="keywords" />
                    <label class="form-check-label" for="analysisTool3">Keyword Extraction</label>
                </div>
                <div class="form-check">
                    <input ref="analysisTool4" class="form-check-input" type="checkbox" name="refs" />
                    <label class="form-check-label" for="analysisTool4">Extract References</label>
                </div>
                <div class="form-check">
                    <input ref="analysisTool5" class="form-check-input" type="checkbox" name="metadata" />
                    <label class="form-check-label" for="analysisTool5">Extract Metadata</label>
                </div>
                <div class="form-check">
                    <input ref="analysisTool6" class="form-check-input" type="checkbox" name="metrics" />
                    <label class="form-check-label" for="analysisTool6">Calculate Metrics</label>
                </div>
            </div>

            <div class="row d-flex my-4 justify-content-center">
                <p class="text-center lead upload-text">Enter the URL of a paper</p>

                <div class="input-group">
                    <input type="url" class="form-control url-input"
                        placeholder="Search" v-model="paperURL" />
                    <button type="button" class="btn btn-success search-btn" @click="URLUpload">
                        <strong>Analyse URL Paper</strong>
                    </button>
                </div>
            </div>

            <p class="text-center lead upload-text">Upload a PDF or a scanned image of a paper</p>

            <input ref="fileInput" type="file" name="fileInput" class="d-none" @change="updateUploadSection" />

            <div class="p-5 drag-drop-section" :style="{ backgroundColor: dragDropBackgroundColor, outlineOffset: dragDropOutlineOffset }" @drop="fileDropped" @dragover="fileDragHover" @dragleave="noFileDragHover">
                <div class="text-center"><span class="material-icons upload-icon">description</span></div>
                <p class="text-center lead" style="color: #9E9E9E;">Drag and drop or <a class="upload-link" @click="this.$refs['fileInput'].click()">browse</a> your files</p>
                <p class="text-center lead error-text" :class="{ 'd-none': hideFileTypeError }">File uploaded is not a PDF or an image</p>
                <p class="text-center file-uploaded-text"><span v-html="fileUploadedText"></span></p>
                <div class="d-flex justify-content-center">
                    <button class="btn btn-success mt-3 analysis-btn" type="button" name="analyseBtn" @click="fileUpload()">
                        <strong>Analyse Uploaded Paper</strong>
                    </button>
                </div>
            </div>

        </div>
    </div>
    <PageFooter />
</template>

<script>
    import PageHeader from "@/components/Header.vue";
    import PageFooter from "@/components/Footer.vue";

    export default {
        components: {
            PageHeader,
            PageFooter
        },

        data() {
            return {
                NUM_FEATURES: 6,

                paperURL: "",

                dragDropBackgroundColor: "#EEEEEE",
                dragDropOutlineOffset: "-10px",

                hideFileTypeError: true,
                fileUploadedText: "",

                analysisFeatures: {
                    "whole": 0,
                    "partial": 0,
                    "keywords": 0,
                    "refs": 0,
                    "metadata": 0,
                    "metrics": 0,
                }
             }
        },

        methods: {
            async redirectToAnalysis() {
                // Wait before redirecting
                await new Promise(r => setTimeout(r, 1000));

                // Switch to the analysis view
                this.$router.push(
                    {
                        path: "/analysis",
                        name: "Analysis",
                        params: {
                            // Send the analysis features selected to analysis page
                            analysisFeaturesJSONString: JSON.stringify(this.analysisFeatures)
                        }
                    }
                );
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
                this.$refs["fileInput"].files = ev.dataTransfer.files;
                this.updateUploadSection();
            },

            updateUploadSection() {
                //const filename = this.fileInput.files[0].name;
                const filename = this.$refs["fileInput"].files[0].name;
                const extension = filename.split('.').pop().toLowerCase();

                // Check extension is valid
                if (["pdf", "jpg", "png"].includes(extension)) {
                    // Hide error and show analysis feature selection section
                    this.hideFileTypeError = true;

                    this.fileUploadedText = "File uploaded: \
                        <span class='filename'>"
                        + filename + "</span>";
                } else {
                    // Show error and hide analysis feature selection section
                    this.hideFileTypeError = false;
                    this.fileUploadedText = "";
                }
            },

            selectAllCheckboxes(numfeatues) {
                // If select all is checked
                if(this.$refs["selectAll"].checked) {
                    // Check all checkboxes
                    for (let i = 1; i < numfeatues + 1; i++) {
                        const checkbox = "analysisTool" + i;
                        this.$refs[checkbox].checked = true;
                    }
                } else {
                    // Uncheck all checkboxes
                    for (let i = 1; i < numfeatues + 1; i++) {
                        const checkbox = "analysisTool" + i;
                        this.$refs[checkbox].checked = false;
                    }
                }
            },

            checkSelection(numfeatues) {
                // Check that at least one checkbox is checked
                let isSelected = false;
                for (let i = 1; i < numfeatues + 1; i++) {
                    const checkbox = "analysisTool" + i;
                    if (this.$refs[checkbox].checked) {
                        // Set the selection to 1 for the checkboxes that are
                        // selected
                        this.analysisFeatures[this.$refs[checkbox].name] = 1;
                        isSelected = true;
                    }
                }

                // If at least one checkbox is selected, upload paper
                if (isSelected) {
                    return true;
                } else {
                    return false;
                }
            },

            async fileUpload() {
                /* Uploads the file */
                // Check file has been selected and features selected
                if (this.checkSelection(this.NUM_FEATURES)
                    && this.$refs["fileInput"].files[0]) {

                    const fileInput = this.$refs["fileInput"];
                    // Add file uploaded to the form data
                    const formData = new FormData();
                    formData.append('fileInput', fileInput.files[0]);

                    const CONFIG = {
                        method: "POST",
                        mode: "cors",
                        credentials: "include",
                        // URL encode the analysis features object
                        body: formData
                    };

                    const URL = "http://localhost:5000/api/v1/upload/binary";
                    const getObject = await fetch(URL, CONFIG);
                    const response = await getObject.json();

                    // Check if upload is successful
                    if (response.current_status === 1) {
                        this.redirectToAnalysis();
                    }
                }
            },

            async URLUpload() {
                /* Uploads the URL */
                // Check if URL is defined and featues have been selected
                if (this.paperURL && this.checkSelection(this.NUM_FEATURES)) {
                    const CONFIG = {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                        },
                        mode: "cors",
                        credentials: "include",
                        body: new URLSearchParams({"link": this.paperURL})
                    };

                    const URL = "http://localhost:5000/api/v1/upload/url"
                    const getObject = await fetch(URL, CONFIG);
                    const response = await getObject.json();

                    // Check if upload is successful
                    if (response.current_status === 1) {
                        this.redirectToAnalysis();
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
        font-family: "Poppins", sans-serif;
        font-weight: bold;
    }

    .upload-text {
        color: #616161;
        font-weight: bold;
    }

    .url-input {
        border-top-left-radius: 24px;
        border-bottom-left-radius: 24px;
    }

    .search-btn {
        border: none;
        outline: none;
        border-top-right-radius: 24px;
        border-bottom-right-radius: 24px
    }

    .search-btn:focus {
        outline: none;
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
        font-family: "Poppins", sans-serif;
    }
</style>
