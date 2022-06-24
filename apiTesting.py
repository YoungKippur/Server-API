import requests

S = requests.Session()

URL = "http://127.0.0.1:5000/api"

R = S.get(URL)
DATA = R.json()

print(DATA['message'], DATA['time'])