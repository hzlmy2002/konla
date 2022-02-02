# Run API
# API Structure inspired by post
# https://dev.to/paurakhsharma/flask-rest-api-part-2-better-structure-with-blueprint-and-flask-restful-2n93

from flask import Flask
from flask_restful import Api
from resources.routes import initialize_routes
from settings import UPLOAD_PATH
# from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['UPLOAD_PATH'] = UPLOAD_PATH
api = Api(app)

initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
