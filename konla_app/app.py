import os
import sys
sys.path.append(os.path.abspath('.'))

# Flask
from flask import Flask
from flask import render_template, url_for, request, redirect
from flask import flash
# NLP
import spacy
import en_core_web_lg
import pandas as pd

# PDF upload
from werkzeug.utils import secure_filename
# Text extraction
from tika import parser


# Configuration
nlp = spacy.load('en_core_web_lg')

ALLOWED_EXTENSIONS = {'pdf'}
app = Flask(__name__)
app.config['SECRET_KEY'] = 'konla'
# app.config['UPLOAD_FOLDER'] = uploads_dir
uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

# Views
@app.route('/')
def index():
    return render_template("upload.html")


@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        file = request.files['file']
        try:
            if file:
                filename = secure_filename(file.filename)
                filepath = os.path.join(uploads_dir, filename)
                file.save(filepath)
                flash("FILE UPLOADED SUCCESSFULLY")
                print("FILE UPLOADED SUCCESSFULLY")
                pdf_output = parser.from_file(filepath)  # this takes some time
                content = pdf_output['content']  # raw text
                metadata = pdf_output['metadata']  # raw text
                print("STARTED ANALYSIS...")
                doc = nlp(content)
                d = []
                print(f"NUM OF ENTITIES: {len(list(doc.ents))}")
                for entity in doc.ents:
                    d.append((entity.label_, entity.text))
                df = pd.DataFrame(d, columns=('named entity', 'output'))
                ner_table = df.to_html()
                print("FINISHED")
                return render_template("process.html", content=content, metadata=metadata, ner_table=ner_table)
        except Exception as e:
            print(e)
            return redirect('/')
    if request.method == 'GET':
        return render_template('process.html')




if __name__ == '__main__':
    app.run(debug=True)
