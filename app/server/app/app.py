from bottle import Bottle, request, response, run
from json import dumps


app = Bottle()


@app.hook('after_request')
def enable_cors():
    """CORS ENABLE"""
    cors_allow = '*'
    methods = 'PUT, GET, POST, DELETE, OPTIONS'
    headers = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    response.headers['Access-Control-Allow-Origin'] = cors_allow
    response.headers['Access-Control-Allow-Methods'] = methods
    response.headers['Access-Control-Allow-Headers'] = headers


@app.route('/user', method=['OPTIONS', 'GET'])
def examples():
    response.content_type = 'application/json'
    """USER DATA SERVICE EXAMPLE"""
    if request.method == 'GET':
        return dumps({'examples': [{'id': 1, 'name': 'Foo'},
                             {'id': 2, 'name': 'Bar'}]})


if __name__ == '__main__':

    run(app, host='localhost', port=5001, reloader=True)
