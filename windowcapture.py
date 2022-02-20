import win32gui
import win32ui
import win32con

from dataClass import WindowInfo



def get_window_info():

    info = WindowInfo()

    hwnd = win32gui.FindWindow(None, 'Untitled - Paint')
    if hwnd == 0:
        print("CHANGE TO SHOW ERROR")

    x_0,y_0,x_1,y_1 = win32gui.GetWindowRect(hwnd)
    info.win_x = x_0
    info.win_y = y_0
    info.win_width = x_1 - x_0
    info.win_height = y_1 - y_0

    x_0,y_0,x_1,y_1 = win32gui.GetClientRect(hwnd)
    info.client_width = x_1 - x_0
    info.client_height = y_1 - y_0

    return info

