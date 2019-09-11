# services/users/projects/__init__.py

import os
from flask import Flask, jsonify
from flask_restful import Resource, Api

# instance of the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

class UserPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(UserPing, '/users/ping')