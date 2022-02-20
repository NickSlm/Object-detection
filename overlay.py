from ntpath import join
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton,QWidget,QFormLayout,QGridLayout,QLabel,QHBoxLayout
from PyQt5.QtGui import QPainter,QPixmap
from functools import partial
import sys
from utils import get_recipes, get_templates

class Overlay(QWidget):
    def __init__(self,image_detect):
        super().__init__()
        self.left = 0
        self.top = 0
        self.w = 1096
        self.h = 1024
        self.show_recipe_list = False
        self.image_detect = image_detect

        self.setWindowFlags(Qt.Window|Qt.X11BypassWindowManagerHint|Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(self.left,self.top,self.w,self.h)
        self.showMaximized()

        grid = QGridLayout()
        # Create available recipe list
        recipe_layout = QFormLayout()
        recipe_layout.setVerticalSpacing(4)
        recipe_layout.setHorizontalSpacing(0)
        self.recipe_widget = QWidget()

        # Create menu layout
        # menu_layout = QFormLayout()
        menu_layout = QHBoxLayout()
        # Create menu buttons
        btn_show = QPushButton("Show")
        btn_show.clicked.connect(self.show_recipes)
        btn_show.setFixedWidth(64)
        btn_find = QPushButton("Find")
        btn_find.clicked.connect(self.find_recipes)
        btn_find.setFixedWidth(64)
        btn_exit = QPushButton("Quit")
        btn_exit.clicked.connect(self.close_application)
        btn_exit.setFixedWidth(64)
        menu_layout.addWidget(btn_show)
        menu_layout.addWidget(btn_find)
        menu_layout.addWidget(btn_exit)

        recipes_data = get_recipes() 
        self.templates_data = get_templates()  
        for recipe in recipes_data.keys():
            icon = QLabel()
            pixmap = QPixmap(recipes_data[recipe]['icon'])
            pixmap = pixmap.scaled(16,16)
            label = QLabel(recipe)
            label.setStyleSheet("background-color:rgba(255, 191, 0, 100);font: bold;")
            label.setToolTip(' '.join(recipes_data[recipe]['drops']))
            icon.setStyleSheet("background-color:rgba(255, 191, 0, 100);font: bold;")
            icon.setPixmap(pixmap)

            icon.mousePressEvent = partial(self.button_press,recipe)
            label.mousePressEvent = partial(self.button_press,recipe)

            recipe_layout.addRow(icon,label)
    
        self.recipe_widget.setLayout(recipe_layout)
        self.recipe_widget.setFixedWidth(156)

        menu_widget = QWidget()
        menu_widget.setLayout(menu_layout)

        grid.addWidget(menu_widget,0,0,Qt.AlignCenter | Qt.AlignTop)
        grid.addWidget(self.recipe_widget,0,0,Qt.AlignCenter)
        self.setLayout(grid)

        self.show()
 
    def keyPressEvent(self, e):
        # Close overlay
        if e.key() == Qt.Key_F8:
            self.close()

    def paintEvent(self,e):
        painter = QPainter(self)
        painter.end()

    def button_press(self,index,QmouseEvent):
        print(index)

    def close_application(self):
        self.close()
    
    def find_recipes(self):
        results = self.image_detect.scan()
        print(results)

    def show_recipes(self):
        self.recipe_widget.setHidden(not self.recipe_widget.isHidden())
