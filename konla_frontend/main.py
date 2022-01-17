""" Konla App - 2022 """
from flask import Flask, render_template, request, Markup
from werkzeug.utils import secure_filename
import os
from analysis import Analyser

app = Flask(__name__)
UPLOAD_PATH = os.path.join(os.getcwd(),"static/uploads")
app.config['UPLOAD_PATH'] = UPLOAD_PATH


def clear_files():
    """ Clear all files from the uploads directory """
    for filename in os.listdir(UPLOAD_PATH):
        os.remove(os.path.join(UPLOAD_PATH, filename))


@app.route('/', methods=['POST', 'GET'])
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    clear_files()  # Remove files stored in uploads

    # Initial template when site is started up
    return render_template("upload.html", error_msg="")


@app.route('/analysis', methods=['POST', 'GET'])
def analysis():
    if request.method == "POST":
        file = request.files["fileInput"]
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_PATH'], filename)
        # Save the file in the upload folder
        file.save(filepath)

        # Analyser object
        analyser = Analyser(filepath)
        # Check paper is processed successfully
        error = analyser.get_error()
        if error is None:
            extracted_text = analyser.get_extracted_text()
            keywords_html = analyser.get_keywords_html()
            return render_template(
                "analysis.html", 
                extracted_text=extracted_text,
                keywords_table=keywords_html)
        else:
            return render_template(
                "upload.html", 
                error_msg=error)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
