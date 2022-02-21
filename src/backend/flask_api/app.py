# Run API
# API Structure inspired by post
# https://dev.to/paurakhsharma/flask-rest-api-part-2-better-structure-with-blueprint-and-flask-restful-2n93

from flask import Flask, render_template, request
from flask_restful import Api
from settings import UPLOAD_PATH
from flask_cors import CORS

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

#api = Api(app)

@app.route("/analysis", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        #print(request.get_json())
        return ("Success", 200)

@app.route("/api/v1/summarisation/whole", methods=["GET"])
def whole_summarisation():
    response = {
    	"success": True,
        "errors": [],
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
    	"success": True,
        "errors": [],
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
    response = {
    	"success": True,
        "errors": [],
        "messages": [],
        "result": {
        	"keywords": {"Hello": 10, "World": 6, "KONLA": 3}
        }
    }

    return response

@app.route("/api/v1/info/refs", methods=["GET"])
def refs():
    response = {
    	"success": True,
        "errors": [],
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
    	"success": True,
        "errors": [],
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
    	"success": True,
        "errors": [],
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

@app.route("/api/v1/status/process", methods=["GET"])
def process_status():
    response = {
    	"success": True,
        "errors": [],
        "messages": [],
        "result": {
        	"whole": 1,
        	"partial": 1,
        	"keywords": 1,
        	"refs": 1,
        	"metadata": 1,
        	"metrics": 1,
        }
    }

    return response

if __name__ == "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0")
