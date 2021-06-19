import pyautogui
from pynput.keyboard import Key, Listener

weapon_list = ['big_shield', 'vandal', 'sheriff']


def buy_weapon(wpn):
    screenWidth, screenHeight = pyautogui.size()
    if wpn == 'small_shield':
        pyautogui.click(3*screenWidth/4, 1*screenHeight/3)
    elif wpn == 'big_shield':
        pyautogui.click(3*screenWidth/4, 2*screenHeight/3)
    elif wpn == 'shorty':
        pyautogui.click(screenWidth/4, screenHeight/4)
    elif wpn == 'frenzy':
        pyautogui.click(screenWidth/4, 3*screenHeight/8)
    elif wpn == 'sheriff':
        pyautogui.click(screenWidth/4, 5*screenHeight/8)
    elif wpn == 'stinger':
        pyautogui.click(3*screenWidth/8, 3*screenHeight/16)
    elif wpn == 'spectre':
        pyautogui.click(3*screenWidth/8, 5*screenHeight/16)
    elif wpn == 'bucky':
        pyautogui.click(3*screenWidth/8, screenHeight/2)
    elif wpn == 'judge':
        pyautogui.click(3*screenWidth/8, 5*screenHeight/8)
    elif wpn == 'bulldog':
        pyautogui.click(screenWidth/2, screenHeight/4)
    elif wpn == 'guardian':
        pyautogui.click(screenWidth/2, 3*screenHeight/8)
    elif wpn == 'phantom':
        pyautogui.click(screenWidth/2, screenHeight/2)
    elif wpn == 'vandal':
        pyautogui.click(screenWidth/2, 5*screenHeight/8)
    elif wpn == 'marshall':
        pyautogui.click(5*screenWidth/8, screenHeight/4)
    elif wpn == 'operator':
        pyautogui.click(5*screenWidth/8, 3*screenHeight/8)
    elif wpn == 'ares':
        pyautogui.click(5*screenWidth/8, screenHeight/2)
    elif wpn == 'odin':
        pyautogui.click(5*screenWidth/8, 5*screenHeight/8)
    elif wpn == 'ability_signature':
        pyautogui.click(5*screenWidth/8, 3*screenHeight/4)
        pyautogui.click(5*screenWidth/8, 3*screenHeight/4)
        pyautogui.click(5*screenWidth/8, 3*screenHeight/4)
    elif wpn == 'ability_1':
        pyautogui.click(screenWidth/4, 3*screenHeight/4)
        pyautogui.click(screenWidth/4, 3*screenHeight/4)
        pyautogui.click(screenWidth/4, 3*screenHeight/4)
    elif wpn == 'ability_2':
        pyautogui.click(screenWidth/2, 3*screenHeight/4)
        pyautogui.click(screenWidth/2, 3*screenHeight/4)
        pyautogui.click(screenWidth/2, 3*screenHeight/4)
    else:
        pass
    print("bought " + str(wpn) + "!")


def read_config_file():
    filtered_wpnlist = []
    with open('config.txt', 'r') as config:
        unfiltered_wpnlist = config.readlines()
        for wpn in unfiltered_wpnlist:
            fwpn = wpn.replace('\n', '')
            filtered_wpnlist.append(fwpn)
    return filtered_wpnlist


def on_press(key):
    if key == Key.f1:
        pyautogui.press('b')
        wpnlist = read_config_file()
        for wpn in wpnlist:
            buy_weapon(wpn)
        pyautogui.press('b')


def on_release(key):
    if key == Key.f12:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
