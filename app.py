from image_detection import image_detect
from PyQt5 import QtWidgets
import sys
from overlay import Overlay

def main():
    app = QtWidgets.QApplication(sys.argv)
    overlay = Overlay()
    overlay.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()