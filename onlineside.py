import requests
import json

r = json.loads(requests.get("https://api.github.com/repos/tonioliii/jkiller/git/trees/main?recursive=1").text)

for x in r["tree"]:
    if x["path"].startswith("lib/") or x["path"] == "exec.py":
        n = x["path"]
        l = "https://github.com/tonioliii/jkiller/raw/main/" + n
        with open(n,"w") as f:
            f.write(requests.get(l).text)