# -*- coding: utf8 -*-
# coding: utf8

from flask_restful import Resource, Api
from werkzeug.exceptions import HTTPException
from flask import request, send_file, json, Response
from __init__ import *

api = Api(app)

class JcNetwork(Resource):
    def get(self):
        return {
            'code': 200,
            'message': 'Success to call the get method!'
        }
    def post(self):
        name = json.loads(request.get_data()).get('name')
        return {
            'code': 200,
            'message': 'Hello {name}, welcome to JCNetworkKit'.format(name=name)
        }
    def delete(self):
        thing = json.loads(request.get_data()).get('object')
        return {
            'code': 200,
            'message': 'Deleted {obj} successfully!'.format(obj=thing)
        }

api.add_resource(JcNetwork, '/try-jcnetwork-api')

if __name__ == '__main__':  
    app.run(
        host = '127.0.0.1',
        port = 5000
    )