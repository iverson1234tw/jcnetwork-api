from werkzeug.exceptions import HTTPException
from flask import request, send_file, json
from __init__ import *

@app.route('/try-jcnetwork-api', methods=['GET', 'POST', 'DELETE'])
def try_jcnetwork_api():
    if request.method == 'GET':
        return json.dumps({
            'code': 200,
            'message': 'Success to call the get method!'
            })
    elif request.method == 'POST':
        # print(json.loads(request.get_data()).get('text'))
        # text_message = json.loads(request.get_data())
        return json.dumps({
            'code': 200,
            'message': 'Hello, welcome to JCNetworkKit'
            })
    elif request.method == 'DELETE':
        return json.dumps({
            'code': 200,
            'message': 'Success to call the delete method!'
            })

if __name__ == '__main__':  
    app.run(
        host = '127.0.0.1',
        port = 5000
    )