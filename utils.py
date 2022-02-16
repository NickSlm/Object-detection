from matplotlib.font_manager import json_dump, json_load
from PIL import Image
import numpy as np
import cv2
import win32gui
import json

from dataClass import WindowInfo

# List all running windows application titles
def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print(hex(hwnd), win32gui.GetWindowText( hwnd ))
        
# win32gui.EnumWindows( winEnumHandler, None )

def get_recipes():
    with open(r'D:\Find image on screen\data\recipes.json') as f:
        data = json.load(f)
    return data

def get_templates():
    with open(r"D:\Find image on screen\data\template.json") as f:
        data = json.load(f)
    return data


def create_scan_image(image,scale):
    template_image = Image.open(image)
    # check if needed
    template_image.resize((int(template_image.width * scale),int(template_image.height * scale)))

    template_background = Image.new('RGBA',template_image.size,(10,10,32))
    template_image_w_alpha = Image.alpha_composite(template_background,template_image)

    template_scan = cv2.cvtColor(np.array(template_image_w_alpha),cv2.COLOR_RGB2GRAY)

    w,h = template_scan.shape

    return template_scan[int(h * 1.0 / 10):int(h * 2.3 / 3), int(w * 1.0 / 6):int(w * 5.5 / 6)]


def get_img_scale(win_info: WindowInfo):
    template_img_h = 48.0
    constant = 1440.0 / (template_img_h * 1)
    scale = win_info.client_height / (template_img_h * constant)
    return scale