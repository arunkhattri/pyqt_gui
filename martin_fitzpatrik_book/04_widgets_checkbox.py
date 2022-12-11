# 04_widgets_checkbox.py

"""QCheckBox"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox("This is a checkbox.")
        widget.setCheckState(Qt.CheckState.Checked)

        widget.stateChanged.connect(self._show_state)

        self.setCentralWidget(widget)

    def _show_state(self, s):
        print(Qt.CheckState(s) == Qt.CheckState.Checked)
        print(s)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
