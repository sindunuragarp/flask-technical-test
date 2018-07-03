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


@app.route('/getJokes')
def jokes_get():
    data = get_jokes()

    res = {
        'status': 'success',
        'jokes': data
    }
    return Response(json.dumps(res), status=200, mimetype='application/json')


@app.route('/getNewJokes')
def jokes_get_new():
    fill_new_jokes()
    data = get_jokes()

    res = {
        'status': 'success',
        'jokes': data
    }
    return Response(json.dumps(res), status=200, mimetype='application/json')


@app.route('/flushJokes')
def jokes_flush():
    flush_jokes()

    res = {
        'status': 'success'
    }
    return Response(json.dumps(res), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
