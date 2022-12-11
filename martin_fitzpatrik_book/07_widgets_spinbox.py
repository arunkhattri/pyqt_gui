# 07_widgets_spinbox.py

"""QSpinBox and QDoubleSpinBox"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSpinBox()
        widget.setMinimum(0)
        widget.setMaximum(10)

        widget.setPrefix("₹")
        widget.setSuffix("p")
        widget.setSingleStep(1)
        widget.valueChanged.connect(self._value_changed)
        widget.textChanged.connect(self._text_changed)

        self.setCentralWidget(widget)

    def _value_changed(self, i):
        print(i)

    def _text_changed(self, s):
        print(s)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
