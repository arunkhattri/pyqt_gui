# 05_widgets_list.py

"""QListWidget"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self._item_changed)
        widget.currentTextChanged.connect(self._text_changed)

        self.setCentralWidget(widget)

    def _item_changed(self, i):
        print(i.text())

    def _text_changed(self, s):
        print(s)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
