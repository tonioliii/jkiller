from random import randint
import math
from time import sleep
import os.path
import os

# POPUP -> powershell (New-Object -ComObject Wscript.Shell).Popup("""Operation Completed""",0,"""Done""",0x0)
# ETEINDRE ????
# EVENT QUAND TOUCHE CERTAINE TOUCHES DU CLAVIER

try:
    from pynput.keyboard import Key, Controller
except:
    install("pynput")
    from pynput.keyboard import Key, Controller

try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except:
    install("pycaw")
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    import math


try:
    os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")
except:
    pass
try:
    from vlc import MediaPlayer as playsoundfromdisk
except:
    install("python-vlc")
    from vlc import MediaPlayer as playsoundfromdisk

try:
    from webbrowser import open as webopen
except:
    install("webbrowser")
    from webbrowser import open as webopen

def unmute():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)
    sleep(1)

def mute():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1, None)
    sleep(1)

def random_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    randint(0,1)
    volume.SetMasterVolumeLevel(randint(-30,0), None)
    sleep(1)

def alt_f4():
    keyboard = Controller()
    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt)
    keyboard.release(Key.f4)

def win_d():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press("d")
    keyboard.release(Key.cmd)
    keyboard.release("d")

def ctrl_win_d():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press(Key.ctrl)
    keyboard.press("d")
    keyboard.release(Key.cmd)
    keyboard.release(Key.ctrl)
    keyboard.release("d")

def ctrl_win_right():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press(Key.ctrl)
    keyboard.press(Key.right)
    keyboard.release(Key.cmd)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.right)

def ctrl_win_left():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press(Key.ctrl)
    keyboard.press(Key.left)
    keyboard.release(Key.cmd)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.left)

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
    name = url.split('/')[-1]
    check_file = os.path.isfile(name)
    if check_file == False:
        download_file(url)
    sleep(1)
    try:
        playsoundfromdisk(name).play()
    except:
        pass

# Feature list:
# playsound(url)
# ctrl_win_left()
# ctrl_win_right()
# ctrl_win_d()
# win_d()
# alt_f4()
# random_volume()
# mute()
# unmute()
# webopen(url)

webopen("https://www.google.com")