from lib.main import *
from lib.geometry import *


def on_press(key):
    try:
        if type(key) != type(Key.alt):
            key = str(key).replace("'","")
        last_keys.insert(0,key)
        for x in keypress_event :
            if startswithlist(last_keys,x[0]):        
                actions.append(x[1])
    except Exception as E:
        log(f"Error {E} on_press({key})")

listener = Listener(on_press=on_press)
listener.start()

# add_key_press_event([Key.caps_lock],[alt_f4])
# add_key_press_event([Key.esc],[playsound,"https://raw.githubusercontent.com/tonioliii/jkiller/main/fortnite.mp3"])
# add_key_press_event(['\\x03'],[mute])
# add_key_press_event(['\\x03'],[set_sourire_on_screen])
# add_key_press_event([Key.caps_lock],[set_sourire_on_screen,0xffe838])
# set_background("https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Exampledotcom.png/640px-Exampledotcom.png")

while True:
    if actions != []:
        action = actions[0]
        if len(action) == 2:
            action[0](action[1])
        else:
            action[0]()
        actions = actions[1:]
