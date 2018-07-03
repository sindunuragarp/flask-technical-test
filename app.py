from flask import Flask, Response
from jokes import get_jokes, fill_new_jokes, flush_jokes
import json

app = Flask(__name__)


@app.before_first_request
def startup():
    fill_new_jokes()


@app.route('/')
def hello_world():
    return 'It Works!'


@app.route('/getJokes', methods=['GET'])
def jokes_get():
    data = get_jokes()
    res = {
        'status': 'success',
        'jokes': data
    }
    return Response(json.dumps(res), status=200, mimetype='application/json')


@app.route('/getNewJokes', methods=['GET'])
def jokes_get_new():

    try:
        fill_new_jokes()
    except ValueError as e:
        print("test")
        res = {
            'status': 'error',
            'message': 'Server Error'
        }
        return Response(json.dumps(res), status=400, mimetype='application/json')

    data = get_jokes()
    res = {
        'status': 'success',
        'jokes': data
    }
    return Response(json.dumps(res), status=200, mimetype='application/json')


@app.route('/flushJokes', methods=['GET', 'DELETE'])
def jokes_flush():
    flush_jokes()

    res = {
        'status': 'success'
    }
    return Response(json.dumps(res), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
