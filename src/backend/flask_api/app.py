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
        print(request.get_json())
        return ("Success", 200)
    #return {"analysis": "Hello from Flask!"}

# @app.route("/analysis", methods=("GET", "POST"))
# def analysis():
#     return {"hello_message": "Hello from Flask!"}


if __name__ == "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0")
