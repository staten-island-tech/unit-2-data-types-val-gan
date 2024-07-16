import requests as r

data = r.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0').json()

## url has to api
## get api = google public API github               MUST: can't be authkey?

for x in data['results']:
    print(x['name'])