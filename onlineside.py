from random import randint
import math
from time import sleep
import os.path

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
    from vlc import MediaPlayer as playsoundfromdisk
    # from playsound import playsound as playsoundfromdisk
except:
    install("python-vlc")
    from vlc import MediaPlayer as playsoundfromdisk

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

def change_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    randint(0,1)
    volume.SetMasterVolumeLevel(randint(-30,0), None)
    sleep(1)

def altf4():
    keyboard = Controller()
    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt)
    keyboard.release(Key.f4)

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

while True:
    playsound("https://raw.githubusercontent.com/tonioliii/jkiller/main/fortnite.mp3")
    sleep(5)