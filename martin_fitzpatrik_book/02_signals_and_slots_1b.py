# 02_signals_and_slots_1b.py

"""
Simple custom slot which accepts the clicked signal from push button.
store the current state of a widget in a python variable.
Retrieve the value from the widget directly in handler
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)


# subclass QMainWindow to customize application's main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.button_is_checked = True

        # keep a reference to the button on self
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        # release signal fires, but does not send the checked state
        self.button.released.connect(
            self.the_button_was_released
        )
        self.button.setChecked(self.button_is_checked)

        # set the central widget of the window.
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        # check state of the button
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication([])

window = MainWindow()

window.show()
sys.exit(app.exec())
