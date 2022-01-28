""" PDF text extracter using Tika """
from tika import parser as tikaParser

class PDFToText():
    def __init__(self):
        pass

    def get_content(self, filepath:str):
        pdf_data_dict = tikaParser.from_file(filepath)

        content = pdf_data_dict['content']

        return self.encode_content(content)

    def encode_content(self, raw_content:str):
        encoded_content = b""
        content_split = raw_content.split("\n")
        for line in content_split:
            # Check line has content
            if len(line) > 0:
                try:
                    encoded_line = (line + "\n").encode("utf8")
                    encoded_content += encoded_line
                except Exception as e:
                    pass

        return encoded_content
