# 02_signals_and_slots_3.py

"""
Connect the .windowTitleChanged signal on the QMainWindow to a custom
slot method.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)
from random import choice


WINDOW_TITLES = [
    "My App",
    "Someone's App",
    "Still My App",
    "App is Hacked!!!",
    "What on earth?",
    "Something went wrong",
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self._button_clicked)

        self.windowTitleChanged.connect(
            self._window_title_changed
        )

        # set the central widget of the window
        self.setCentralWidget(self.button)

    def _button_clicked(self):
        print("Clicked.")
        new_window_title = choice(WINDOW_TITLES)
        print(f"Setting title: {new_window_title}")
        self.setWindowTitle(new_window_title)

    def _window_title_changed(self, window_title):
        print(f"Window Title changed: {window_title}")

        if window_title == "Something went wrong":
            self.button.setDisabled(True)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
