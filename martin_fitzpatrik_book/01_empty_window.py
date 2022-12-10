# 01_empty_window.py

"""Simple Empty QMainWindow to our application."""

import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

WIDTH = 400
HEIGHT = 300


# subclass QMainWindow to customize application's main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(WIDTH, HEIGHT))

        # set the central widget of the window.
        self.setCentralWidget(button)


app = QApplication([])

window = MainWindow()

window.show()
sys.exit(app.exec())
