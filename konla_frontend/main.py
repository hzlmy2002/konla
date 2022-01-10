""" Konla App """
from flask import Flask, render_template, request, Markup
import os

app = Flask(__name__)
UPLOAD_PATH = "static/uploads"
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
    return render_template("upload.html")
