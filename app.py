from image_detection import ImageDetector
from PyQt5 import QtWidgets
import sys
from overlay import Overlay
from windowcapture import get_window_info

def main():
    info  = get_window_info()
    image_detect = ImageDetector(info)
    app = QtWidgets.QApplication(sys.argv)
    overlay = Overlay(image_detect.scan())
    overlay.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()