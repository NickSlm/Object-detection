from ntpath import join
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QPushButton,QVBoxLayout,QWidget,QGridLayout
from PyQt5.QtGui import QPainter, QBrush, QPen,QColor
import sys
from image_detection import image_detect
from utils import get_recipes

class Overlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()

    def init_window(self):
        # MAKE WIDOW TRANSPARENT
        # self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        # self.setAttribute(Qt.WA_NoChildEventsForParent, True)
        self.setWindowFlags(Qt.Window|Qt.X11BypassWindowManagerHint|Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setGeometry(0,0,1920,1024)
        self.showMaximized()

        self.setCentralWidget(self.create_layout())

    def create_layout(self):
        self.central_widget = QWidget()
        self.vlayout = QVBoxLayout()
        self.glayout = QGridLayout()

        # Create Buttons
        recipes_data = get_recipes()
        for recipe in recipes_data.keys():
            self.recipe = QPushButton()
            self.recipe.setStyleSheet("QPushButton"
                            "{"
                            f"border-image: url({recipes_data[recipe]['icon']});"
                            "}"
                            "QToolTip"
                            "{"
                            "color: black;"
                            "border: 1px solid darkkhaki;"
                            "padding: 5px;"
                            "border-radius: 3px;"
                            "opacity: 200;"
                            "font: bold 12px;"
                            "}"
                            )
            self.recipe.setToolTip(f"{recipe}\n{', '.join(recipes_data[recipe]['drops'])}")
            self.recipe.setMinimumSize(48,48)
            self.recipe.setMaximumSize(48,48)    
            self.recipe.clicked.connect(self.select_recipe)
            self.vlayout.addWidget(self.recipe,alignment=QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.central_widget.setLayout(self.vlayout)

        return self.central_widget

    def keyPressEvent(self, e):
        # Close overlay
        if e.key() == Qt.Key_F8:
            self.close()

    def paintEvent(self,e):
        painter = QPainter(self)
        self.mark_objects(painter)

    def mark_objects(self,painter):
        s_x,s_y,e_x,e_y = image_detect(r'D:\Find image on screen\images\templates\ModRecipeCorpseeploder.png')
        painter.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
        painter.drawRect(s_x,s_y, 48 ,48)

    def select_recipe(self):
        print("recipe")