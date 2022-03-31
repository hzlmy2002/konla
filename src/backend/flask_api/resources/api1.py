"""
AUTHOR:
"""
from cgitb import text
import os, sys
PARENT_DIR = os.path.dirname(__file__)
API_DIR = os.path.dirname(PARENT_DIR)
BACKEND_DIR = os.path.dirname(API_DIR)
sys.path.append(os.path.abspath(BACKEND_DIR))
from flask_api.settings import UPLOAD_PATH
from flask import request, jsonify
from flask_restful import Resource
from werkzeug.utils import secure_filename
from apps.pdf_extraction.PDFHelper import PDFHelper


class Home(Resource):
    """ Index page for the API """

    def get(self):
        return '<h1> KONLA API (0.1) </h1>'


class FileUpload(Resource):
    """File upload request"""

    def post(self):
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_PATH, filename)
        file.save(filepath)
        text = PDFHelper().pdf2text(filepath) # TODO: delete file after
        resp = jsonify({'message' : text})
        resp.status_code = 201
        return resp
