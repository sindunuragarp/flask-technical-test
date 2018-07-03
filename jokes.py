import requests

url = "http://api.icndb.com/jokes/random/"
max_jokes = 10
max_requests = 20
jokes = []


def get_jokes():
    return jokes


def fill_new_jokes():
    global jokes
    new_jokes = _fetch_jokes(max_jokes)
    jokes = new_jokes


def flush_jokes():
    global jokes
    jokes = []


def _fetch_jokes(num):
    new_jokes = []
    tries = 0

    while len(new_jokes) < num:
        tries += 1
        if tries > max_requests:
            break

        res = requests.get(url)
        if res.status_code != 200:
            continue

        data = res.json()
        if data['type'] != 'success':
            continue

        joke = data['value']
        joke_id = joke['id']
        if joke_id in [x['id'] for x in jokes]:
            continue

        new_jokes.append(joke)

    return new_jokes
