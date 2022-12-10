# 03_widgets_1.py

"""QLabel widget"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        # get the current font (system font)
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
