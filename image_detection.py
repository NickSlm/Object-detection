from venv import create
import cv2
import json
import numpy as np
from utils import get_templates,create_scan_image,get_img_scale
from windowcapture import get_window_info
from PIL import ImageGrab
from typing import Dict


class ImageDetector:
    def __init__(self,info):
        self.info = info
        self._scanner_window_size = (
                self.info.win_x,
                self.info.win_y + int(self.info.client_height / 4),
                int(self.info.client_width / 3),
                int(self.info.client_height * 2 /3)
            )
        self.conf_threshold = 0.91
        self.scale = get_img_scale(self.info)
        self.recipes_templates = get_templates()
        
    def scan(self):
        bbox = (
            self._scanner_window_size[0],
            self._scanner_window_size[1],
            self._scanner_window_size[0] + self._scanner_window_size[2],
            self._scanner_window_size[1] + self._scanner_window_size[3]
        )
        screen = ImageGrab.grab(bbox=bbox)
        screen.save('test2.png')
        screen = np.array(screen)
        screen = cv2.cvtColor(screen,cv2.COLOR_RGB2GRAY)


        results = {}
        for recipe in self.recipes_templates.keys():
            template = create_scan_image(self.recipes_templates[recipe]['icon'],self.scale)
            heat_map = cv2.matchTemplate(screen,template,cv2.TM_CCOEFF_NORMED)
            _, confidence, _, (x, y) = cv2.minMaxLoc(heat_map)
            print(f'Best match for {recipe}: x={x}, y={y} confidence={confidence}', 'too low' if confidence < self.conf_threshold else '')
            best_matches = np.where(heat_map >= self.conf_threshold)
            if len(best_matches[0]) > 0:
                rectangles = []
                t_h,t_w = template.shape[0],template.shape[1]
                for (x,y) in zip(best_matches[1],best_matches[0]):
                    rectangles.append([int(x),int(y),int(t_w),int(t_h)])
                    rectangles.append([int(x),int(y),int(t_w),int(t_h)])
                rectangles,_ = cv2.groupRectangles(rectangles,1,0.1)
                results[recipe] = [(rect[0], rect[1]) for rect in rectangles]
        return results