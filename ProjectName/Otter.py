import requests
import os

r = requests.get(os.getenv("Site"))
assert r.status_code == 200

assert 1 == 2