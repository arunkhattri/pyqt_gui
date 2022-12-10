# 02_signals_and_slots_1a.py

"""
Simple custom slot which accepts the clicked signal from push button.
output the checkstate (checked state for the button).
store the current state of a widget in a python variable.
"""

import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)
WIDTH = 400
HEIGHT = 300


# subclass QMainWindow to customize application's main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        # default value for our variable
        self.button_is_checked = True

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        # initial state of the widget
        button.setChecked(self.button_is_checked)

        self.setFixedSize(QSize(WIDTH, HEIGHT))

        # set the central widget of the window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked")

    def the_button_was_toggled(self, checked):
        # update the variable
        self.button_is_checked = checked
        print(self.button_is_checked)


app = QApplication([])

window = MainWindow()

window.show()
sys.exit(app.exec())
