"""
AUTHOR: Suraj Kothari
API Structure inspired by post
https://dev.to/paurakhsharma/flask-rest-api-part-2-better-structure-with-blueprint-and-flask-restful-2n93
"""

from flask import Flask, render_template, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from werkzeug.utils import secure_filename
from settings import UPLOAD_PATH

class VueFlask(Flask):
    """ Flask application with jinja syntax changed """
    jinja_options = Flask.jinja_options.copy()
    # Changed to '%%' because Vue.js uses '{%', '%}'
    jinja_options.update(dict(
        variable_start_string='%%',
        variable_end_string='%%',
    ))

app = VueFlask(__name__)
app.config['UPLOAD_PATH'] = UPLOAD_PATH
CORS(app)

@app.route("/api/v1/upload/binary", methods=["GET", "POST"])
def upload():
    file = request.files["fileInput"]
    filename = secure_filename(file.filename)
    if filename:
        print(filename)
        response = {
            "current_status": 1,
            "errors": [],
            "messages": [],
            "result": {
                "sha256": hash(filename),
	            "text": "Content of paper... Hello World!"
            }
        }
    else:
        response = {
            "current_status": 0,
            "errors": [],
            "messages": [],
            "result": {}
        }

    return response


@app.route("/api/v1/upload/url", methods=["GET"])
def upload_url():
    url = request.args
    print(url)
    response = {
        "current_status": 1,
        "errors": [],
        "messages": [],
        "result": {
            "sha256": '',
            "text": "Content of paper... Hello World!"
        }
    }

    return response


@app.route("/api/v1/upload/start", methods=["GET", "POST"])
def analysisStart():
    url_parameters = request.get_data()

    response = {
        "current_status": 1,
        "errors": [],
        "messages": [],
        "result": {}
    }

    return response

@app.route("/api/v1/summarisation/whole", methods=["GET"])
def whole_summarisation():
    response = {
    	"current_status": 1,
        "errors": ["Error 1", "Error 2", "Error 3"],
        "messages": [],
        "result": {
        	"summarisation":
                "Whole summarised content... Lorem ipsum dolor sit amet, \
                consectetur adipisicing elit, sed do eiusmod tempor incididunt \
                ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis \
                nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo \
                consequat. Duis aute irure dolor in reprehenderit in voluptate velit \
                esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat \
                cupidatat non proident, sunt in culpa qui officia deserunt mollit \
                anim id est laborum."
        }
    }

    return response

@app.route("/api/v1/summarisation/partial", methods=["GET"])
def partial_summarisation():
    response = {
    	"current_status": 1,
        "errors": ["Error A", "Error B", "Error C"],
        "messages": [],
        "result": {
        	"summarisation":
                "Partial summarised content... Lorem ipsum dolor sit amet, \
                consectetur adipisicing elit, sed do eiusmod tempor incididunt \
                ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis \
                nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo \
                consequat. Duis aute irure dolor in reprehenderit in voluptate velit \
                esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat \
                cupidatat non proident, sunt in culpa qui officia deserunt mollit \
                anim id est laborum."
        }
    }

    return response

@app.route("/api/v1/keywords", methods=["GET"])
def keywords():
    parameters = request.args
    if parameters['ignorecase'] == 'true':
        response = {
        	"current_status": 1,
            "errors": ["Error 10", "Error 20", "Error 30"],
            "messages": [],
            "result": {
            	"keywords": {"Hello": 10, "TRUE": 6, "KONLA": 3}
            }
        }
    else:
        response = {
        	"current_status": 1,
            "errors": ["Error 10", "Error 20", "Error 30"],
            "messages": [],
            "result": {
            	"keywords": {"Hello": 10, "FALSE": 6, "KONLA": 3}
            }
        }

    return response

@app.route("/api/v1/info/refs", methods=["GET"])
def refs():
    response = {
    	"current_status": 1,
        "errors": ["Error 100", "Error 200", "Error 300"],
        "messages": [],
        "result": {
        	"refs": [
                "Mitchell, J.A. ‘How citation changed the research \
                world’, The Mendeley, 62(9), p70-81",

                 "Mitchell, J.A. (2017) ‘Changes to citation formats \
                 shake the research world’, The Mendeley Telegraph \
                 (Weekend edition), 6 July, pp.9-12 pp.9-12 pp.9-12",

                 "Troy B.N. (2015) ‘Harvard citation rules’ in \
                 Williams, S.T. (ed.) A guide to citation rules. \
                 New York: NY Publishers, pp. 34-89",

                 "Mitchell, J.A. ‘How citation changed the research \
                  world’, The Mendeley, 62(9), p70-81",

                  "Mitchell, J.A. (2017) ‘Changes to citation formats \
                  shake the research world’, The Mendeley Telegraph \
                  (Weekend edition), 6 July, pp.9-12 pp.9-12 pp.9-12",

                  "Troy B.N. (2015) ‘Harvard citation rules’ in \
                  Williams, S.T. (ed.) A guide to citation rules. \
                  New York: NY Publishers, pp. 34-89"
            ]
        }
    }

    return response

@app.route("/api/v1/info/metadata", methods=["GET"])
def metadata():
    response = {
    	"current_status": 1,
        "errors": ["Error 1K", "Error 2K", "Error 3K"],
        "messages": [],
        "result": {
        	"metadata": {
                "authors": ["Bob B", "Alice A", "Bob B", "Elly E", "David D"],
        		"creator": "Appligent AppendPDF Pro 5.5",
        		"producer": "Adobe PDF Library 15.00",
        		"subject": "Subject of research paper",
        		"title": "Title Of Research Paper"
        	}
        }
    }

    return response

@app.route("/api/v1/info/metrics", methods=["GET"])
def metrics():
    response = {
    	"current_status": 1,
        "errors": ["Error 1M", "Error 2M", "Error 3M"],
        "messages": [],
        "result": {
        	"metrics": {
        		"wordCount": 1920,
        		"readingTime": 120,
        		"speakingTime": 243
        	}
        }
    }

    return response

if __name__ == "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0")
