import os
from pickletools import uint8
from time import sleep
import cv2
import numpy as np
import win32gui
from PIL import ImageGrab
import pyautogui
import settings
import importlib


def get_window_info():
    window_info = {}
    win32gui.EnumWindows(set_window_coordinates, window_info)
    return window_info


def set_window_coordinates(hwnd, window_info):
    if win32gui.IsWindowVisible(hwnd):
        if 'Path of Exile' in win32gui.GetWindowText(hwnd):
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            window_info['x'] = x
            window_info['y'] = y
            window_info['width'] = w
            window_info['height'] = h
            window_info['name'] = win32gui.GetWindowText(hwnd)
            win32gui.SetForegroundWindow(hwnd)


def get_screen(x1, y1, x2, y2):
    box = (x1, y1, x2, y2)
    screen = ImageGrab.grab(box)
    img = np.array(screen)
    return img


def hp_info():
    img = get_screen(f['x'], f['y'] + 500, f['width'] - 700, f['height'] - 50)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    upper_range = np.array([122, 160, 160])
    lower_range = np.array([120, 150, 150])
    mask = cv2.inRange(hsv, lower_range, upper_range)

    moments = cv2.moments(mask, 1)
    dArea = moments['m00']
    if dArea > 1:
        return 0
    else:
        upper_range = np.array([122, 200, 200])
        lower_range = np.array([120, 100, 100])
        mask = cv2.inRange(hsv, lower_range, upper_range)
        moments = cv2.moments(mask, 1)
        dArea = moments['m00']
        if dArea > 1:
            return 1
        return 2


def debuff_info():
    debuff_img = get_screen(f['x'], f['y'] + 30, f['width'] - 400, f['height'] - 500)
    for root, dirs, files in os.walk("debuffs"):
        for debuff_name in files:
            try:
                query_img = cv2.imread(f'debuffs/{debuff_name}')
                query_img = cv2.resize(query_img, (30, 30))
                query_img_bw = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
                original_img_bw = cv2.cvtColor(debuff_img, cv2.COLOR_BGR2GRAY)
                result = cv2.matchTemplate(original_img_bw, query_img_bw, cv2.TM_CCOEFF_NORMED)

                threshold = 0.8
                loc = np.where(result >= threshold)

                if len(loc[0]) > 0:

                    return debuff_name.split(".")[0]

            except:
                pass


def heal_or_logout():
    realtime_hp = hp_info()
    if realtime_hp == 1:
        pyautogui.press(settings.heal_button)
        print("use heal")
        sleep(1)
    elif realtime_hp == 2:
        if settings.logout_macro == 'Нет':
            pyautogui.press('enter')
            pyautogui.write('/exit')
            pyautogui.press('enter')
            sleep(2)
        else:
            pyautogui.press('F1')
            sleep(1)


def debuff_type(debuff):
    if debuff in ['assas mark', 'conduciivity', 'Elemental Weakness', 'Enfeeble',
                  'frostbite', 'temporal chains', 'Vulnerability']:
        return 'curs'
    elif debuff in ['Bleed', 'Corrupted Blood']:
        return 'bleed'
    elif debuff in ['poisoned']:
        return 'poison'
    elif debuff in ['frozen']:
        return 'frozen'
    elif debuff in ['shoked']:
        return 'shoked'

def main():
    importlib.reload(settings)
    global f

    f = get_window_info()

    while True:
        disc = win32gui.FindWindow(None, 'Path of Exile')
        if win32gui.IsIconic(disc) == 0 and disc == win32gui.GetForegroundWindow():
            if settings.track_hp:
                heal_or_logout()

            if settings.track_debuffs:
                realtime_debuff = debuff_type(debuff_info())
                print(realtime_debuff)
                if realtime_debuff == 'curs' and settings.track_curs:
                    pyautogui.press(settings.curs_button)
                elif realtime_debuff == 'bleed' and settings.track_bleed:
                    pyautogui.press(settings.bleed_button)
                elif realtime_debuff == 'poison' and settings.track_poison:
                    pyautogui.press(settings.poison_button)
                elif realtime_debuff == 'frozen' and settings.track_freeze:
                    pyautogui.press(settings.freeze_button)
                elif realtime_debuff == 'shoked' and settings.track_shock:
                    pyautogui.press(settings.shock_button)

        if cv2.waitKey(30) == ord("q"):
            cv2.destroyAllWindows()
            break



