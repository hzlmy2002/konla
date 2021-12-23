""" PDF text extracter using tika """
from tika import parser as tikaParser

def getReferences(content):
    print("### References ###")
    ref_section_index = content.lower().find("references")
    if ref_section_index != -1:
        print(content[ref_section_index:])


def saveContent(content):
    # Open in WB to write UTF8 encoded text
    with open("pdf_text_output.txt", "wb") as file:
        content_split = content.split("\n")
        for line in content_split:
            # Check line has content
            if len(line) > 0:
                try:
                    encoded_line = (line + "\n").encode("utf8")
                    file.write(encoded_line)
                except Exception as e:
                    pass


def displayMetaData(metadata):
    print("### METADATA ###")
    for meta in metadata:
        print(f"{meta}\t{metadata[meta]}")


paper_filename = "../shapes.pdf"

pdf_obj = tikaParser.from_file(paper_filename)
metadata = pdf_obj['metadata']
content = pdf_obj['content']
saveContent(content)

displayMetaData(metadata)
print("-"*30)
getReferences(content)
