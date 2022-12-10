# 03_widgets_2.py

"""Use QLabel to display an image using .setPixmap()"""

import os
import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

# base path, relative to this file
basedir = os.path.dirname(__file__)
img_dir = "img/pixie.jpeg"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(os.path.join(basedir, img_dir)))

        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
