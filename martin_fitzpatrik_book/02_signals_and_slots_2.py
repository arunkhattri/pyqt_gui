# 02_signals_and_slots_2.py

"""Changing the interface"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)


class MainWindow(QMainWindow):
    """QMainWindow"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self._button_clicked)

        # set the central widget of the Window
        self.setCentralWidget(self.button)

    def _button_clicked(self):
        self.button.setText("You already clicked me.")
        # disable the button
        self.button.setEnabled(False)

        # also change the window title.
        self.setWindowTitle("My Oneshot App")


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
