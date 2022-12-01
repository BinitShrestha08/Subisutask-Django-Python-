import requests

api_url = "https://stat.ripe.net/data/announced-prefixes/data.json?resource=4007"
response = requests.get(api_url)
print(response.json())

