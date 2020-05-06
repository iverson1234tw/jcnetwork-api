# -*- coding: utf8 -*-
# coding: utf8

from werkzeug.exceptions import HTTPException
from flask import request, send_file, json, Response
from __init__ import *

@app.route('/try-jcnetwork-api', methods=['GET', 'POST', 'DELETE'])
def try_jcnetwork_api():
    if request.method == 'GET':
        jc_res = {
            'code': 200,
            'message': 'Success to call the get method!'
        }
        return Response(json.dumps(jc_res), mimetype='application/json')
    elif request.method == 'POST':
        name = json.loads(request.get_data()).get('name')
        jc_res = {
            'code': 200,
            'message': 'Hello {name}, welcome to JCNetworkKit'.format(name=name)
        }
        return Response(json.dumps(jc_res), mimetype='application/json')

if __name__ == '__main__':  
    app.run(
        host = '127.0.0.1',
        port = 5000
    )