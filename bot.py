from pickletools import uint8
from time import sleep
import cv2
import numpy as np
import win32gui
from PIL import ImageGrab
import pyautogui
import movement

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


def find_items(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    upper_range = np.array([61, 255, 255])
    lower_range = np.array([59, 200, 200])

    mask = cv2.inRange(hsv, lower_range, upper_range)

    (_, _, _, coords) = cv2.minMaxLoc(mask)
    moments = cv2.moments(mask, 1)
    dArea = moments['m00']
    if dArea > 1000:
        return coords
    else:
        return (0, 0)


def mask_for_move(screen, vertex):
    mask = np.zeros_like(screen)
    cv2.fillPoly(mask, vertex, 255)
    mask1 = cv2.bitwise_and(screen, mask)
    return mask1

def draw_lines(screen, lines):
    try:
        for line in lines:
            cor = line[0]
            cv2.line(screen, (cor[0], cor[1]), (cor[2], cor[3]), [255, 255, 255], 10)
    except:
        pass


f = get_window_info()
print(f)
while True:
    img = get_screen(f['x'], f['y'], f['width'], f['height'])
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # sobelx = cv2.Sobel(gray_img, cv2.CV_32F, 1, 0, ksize=5)
    # sobely = cv2.Sobel(gray_img, cv2.CV_32F, 0, 1, ksize=5)
    # sobel = (sobelx + sobely)
    can = cv2.Canny(gray_img, 200, 300, 20)
    vertex = np.array([[100, 50], [650, 50], [650, 500], [100, 500]])
    can1 = mask_for_move(can, [vertex])
    lines = cv2.HoughLinesP(can1, 1, np.pi/180, 25, 100, 5)
    draw_lines(can1, lines)
    cv2.imshow('mask', can1)
    # movement.PressKey(movement.q)
    if cv2.waitKey(30) == ord("q"):
        cv2.destroyAllWindows()
        break



    # coords = find_items(img)
    # while coords != (0, 0):
    #     print(coords)
    #     pyautogui.moveTo(coords)
    #     pyautogui.click()
    #     sleep(2)
    #     coords = find_items(img)


