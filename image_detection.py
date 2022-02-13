import cv2
from windowcapture import WindowCapture
from PIL import ImageGrab

window_capture = WindowCapture("Untitled - Paint")

def image_detect(template_name):
    image = window_capture.capture_screen()
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    template = cv2.imread(template_name)

    result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    start_x,start_y = max_loc
    end_x = start_x + template.shape[1]
    end_y = start_y + template.shape[0]

    return start_x, start_y,end_x, end_y