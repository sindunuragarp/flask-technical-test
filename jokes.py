import requests
import config
from json.decoder import JSONDecodeError

jokes = []


def get_jokes():
    return jokes


def fill_new_jokes():
    global jokes

    try:
        new_jokes = _fetch_jokes(config.max_jokes)
        jokes = new_jokes
    except ValueError as e:
        # I failed in re-raising the exception so that the routing function
        # can catch it and return an error message to the user
        raise


def flush_jokes():
    global jokes
    jokes = []


def _fetch_jokes(num):
    new_jokes = []
    tries = 0

    while len(new_jokes) < num:
        tries += 1
        if tries > config.max_requests:
            break

        res = requests.get(config.api_url)
        if res.status_code != 200:
            continue

        try:
            data = res.json()
            if data['type'] != 'success':
                continue

            joke = data['value']
            joke_id = joke['id']
            if joke_id in [x['id'] for x in jokes]:
                continue

            new_jokes.append(joke)

        except JSONDecodeError:
            raise ValueError('API did not return json data.')

    if len(new_jokes) < num:
        raise ValueError('Failed to fetch new jokes.')

    return new_jokes
