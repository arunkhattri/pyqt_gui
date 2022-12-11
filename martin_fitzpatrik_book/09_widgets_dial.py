# 09_widgets_dial.py

"""QDial"""


import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QDial()

        widget.setRange(100, 200)
        widget.setSingleStep(10)

        widget.valueChanged.connect(self._value_changed)
        widget.sliderMoved.connect(self._slider_moved)
        widget.sliderPressed.connect(self._slider_pressed)
        widget.sliderReleased.connect(self._slider_released)

        self.setCentralWidget(widget)

    def _value_changed(self, i):
        print(f"[-] {i}")

    def _slider_moved(self, p):
        print(f"[-] position: {p}")

    def _slider_pressed(self):
        print("[i] Pressed!")

    def _slider_released(self):
        print("[i] Released!")


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
