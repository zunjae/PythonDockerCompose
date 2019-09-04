import requests

r = requests.get("https://google.com")
assert r.status_code == 1337