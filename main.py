import pyautogui
from pynput.keyboard import Key, Listener


def on_press(key):
    if key == Key.f1:
        screenWidth, screenHeight = pyautogui.size()
        pyautogui.press('b')
        # pyautogui.click()
        pyautogui.click(screenWidth/2, screenHeight/2)       #phantom
        pyautogui.click(screenWidth/2, 3*screenHeight/4)     #ability2
        pyautogui.click(screenWidth/2, 3*screenHeight/4)
        pyautogui.click(screenWidth/2, 3*screenHeight/4)
        pyautogui.click(screenWidth/4, 3*screenHeight/4)    #ability1
        pyautogui.click(screenWidth/4, 3*screenHeight/4)
        pyautogui.click(screenWidth/4, 3*screenHeight/4)
        pyautogui.click(3*screenWidth/4, 2*screenHeight/3)  #shield
        pyautogui.click(screenWidth/4, screenHeight/2)      #ghost
        pyautogui.press('b')
        print(key)
    # if str(key) == "'\'":
    #     print('DOR')


def on_release(key):
    if key == Key.f12:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
