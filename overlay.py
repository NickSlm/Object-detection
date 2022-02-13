import PyQt5

from image_detection import image_detect

class Overlay():
    def __init__(self) -> None:
        pass
    def get_img_loc(self):
        s_x,s_y,e_x,e_y = image_detect(r'D:\Find image on screen\images\abberath-touched.png')
