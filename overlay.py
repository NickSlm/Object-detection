from ntpath import join
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QPushButton,QVBoxLayout,QWidget,QScrollArea,QFormLayout, QGroupBox,QGridLayout
from PyQt5.QtGui import QPainter, QBrush, QPen,QColor,QIcon
import sys
from image_detection import image_detect
from utils import get_recipes

class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 0
        self.w = 1096
        self.h = 1024

        self.setWindowFlags(Qt.Window|Qt.X11BypassWindowManagerHint|Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(self.left,self.top,self.w,self.h)
        self.showMaximized()


        form_layout = QFormLayout()
        group_box = QGroupBox()

        recipes_data = get_recipes()        
        for recipe in recipes_data.keys():
            self.recipe = QPushButton()
            self.recipe.clicked.connect(self.select_recipe)
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
            form_layout.addRow(self.recipe)

        group_box.setLayout(form_layout)
        scroll = QScrollArea()
        scroll.setWidget(group_box)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        scroll.setFixedWidth(96)

        layout = QGridLayout()
        layout.addWidget(scroll,0,0,QtCore.Qt.AlignTop)

        self.setLayout(layout)

        self.show()

        
    def keyPressEvent(self, e):
        # Close overlay
        if e.key() == Qt.Key_F8:
            self.close()

    def paintEvent(self,e):
        painter = QPainter(self)
        self.mark_objects(painter)

    def mark_objects(self,painter):
        s_x,s_y,e_x,e_y = image_detect(r'D:\Find image on screen\images\templates\ModRareKillEnergyShield.png')
        painter.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
        painter.drawRect(s_x,s_y, 48 ,48)

    def select_recipe(self):
        print("recipe")