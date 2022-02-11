import pyautogui
import cv2
import numpy
from windowcapture import WindowCapture
from PIL import ImageGrab

def main():
    while True:
        image = ImageGrab.grab()
        image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
        template = cv2.imread(r'D:\Find image on screen\images\frost-strider.png')

        result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        start_x,start_y = max_loc
        end_x = start_x + template.shape[1]
        end_y = start_y + template.shape[0]

        cv2.rectangle(image,(start_x, start_y), (end_x, end_y), (255, 0, 0), 3)

        print(start_x,start_y,end_x,end_y)

        cv2.imshow('Screenshot', image)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()