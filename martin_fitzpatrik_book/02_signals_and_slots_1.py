# 02_signals_and_slots_1.py

"""Simple custom slot which accepts the clicked signal from push button."""

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

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        self.setFixedSize(QSize(WIDTH, HEIGHT))

        # set the central widget of the window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)


app = QApplication([])

window = MainWindow()

window.show()
sys.exit(app.exec())
