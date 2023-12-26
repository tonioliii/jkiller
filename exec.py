from lib.main import *
from lib.geometry import *

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
# varicelle(True/False/"toogle") argument optionelle : delay(seconde) et color(hex)
# add_key_press_event([key list],[nom de la fonction,argument optionelle])


# add_key_press_event([Key.caps_lock],[alt_f4])
# add_key_press_event([Key.esc],[playsound,"https://raw.githubusercontent.com/tonioliii/jkiller/main/fortnite.mp3"])
# add_key_press_event(['\\x03'],[mute])

add_key_press_event(['\\x03'],[sourire])

while True:
    if actions != []:
        action = actions[0]
        if len(action) == 2:
            action[0](action[1])
        else:
            action[0]()
        actions = actions[1:]