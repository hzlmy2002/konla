/* KONLA DEMO */
/* AUTHOR: Suraj Kothari */

function initialise() {
    // Add event listeners for window to prevent default opening of a file
    window.addEventListener("dragover",function(e) { e.preventDefault(); }, false);
    window.addEventListener("drop",function(e) { e.preventDefault(); }, false);
}

function uploadFile() {
    // Click the file input
    document.getElementById("fileInput").click();

    // When a user has selected a file, update the file input area
    $('#fileInput').change(function(e) {
        updateUploadSection();
    });

}

function updateUploadSection() {
    var filename = document.getElementById("fileInput").files[0].name;
    var extension = filename.split('.').pop().toLowerCase();

    // Check extension is valid
    if (["pdf", "jpg", "png"].includes(extension)) {
        document.getElementById("uploadError").style.display = "none";
        document.getElementById("analysisSelectionSection").style.display = "block";
        var fileUploadedText = "File uploaded: <span class='filename'>" + filename + "</span>";
        document.getElementById("fileUploadedText").innerHTML = fileUploadedText;
    } else {
        document.getElementById("uploadError").style.display = "block";
        document.getElementById("analysisSelectionSection").style.display = "none";
    }
}

function fileDragHover(ev) {
    ev.preventDefault();
    uploadSection.style.backgroundColor = '#CFD8DC';
    uploadSection.style.outlineOffset = "-20px";
}

function noFileDragHover(ev) {
    ev.preventDefault();
    uploadSection.style.backgroundColor = '#EEEEEE';
    uploadSection.style.outlineOffset = "-10px";
}

function fileDropped(ev) {
    ev.preventDefault();
    uploadSection.style.backgroundColor = '#EEEEEE';
    uploadSection.style.outlineOffset = "-10px";

    // Pass dropped files to file input
    var filename = document.getElementById("fileInput").files = ev.dataTransfer.files;
    updateUploadSection();
}

function checkSelection(numTools) {
    // Check all checkboxes
    for (var i = 1; i<numTools+1; i++) {
        var checkbox = "analysisTool" + i;
        if (document.getElementById(checkbox).checked) {
            // Submit form if any checkbox is ticked
            document.getElementById("uploadForm").submit();
        }
    }
}

function extractTextSectionShow() {
    document.getElementById("extractTextTab").classList.add("active");
    document.getElementById("extractTextSection").classList.remove("hidden");
    document.getElementById("extractKeywordsTab").classList.remove("active");
    document.getElementById("extractKeywordsSection").classList.add("hidden");
}

function extractKeywordsSectionShow() {
    document.getElementById("extractKeywordsTab").classList.add("active");
    document.getElementById("extractKeywordsSection").classList.remove("hidden");
    document.getElementById("extractTextTab").classList.remove("active");
    document.getElementById("extractTextSection").classList.add("hidden");
}
