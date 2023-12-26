import requests
import json

r = json.loads(requests.get("https://api.github.com/repos/tonioliii/jkiller/git/trees/main?recursive=1").text)

