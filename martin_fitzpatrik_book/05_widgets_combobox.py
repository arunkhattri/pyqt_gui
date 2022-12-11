# 05_widgets_combobox.py

"""QComboBox"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # allowing users to enter values
        widget.setEditable(True)
        # flag to determine how the insert in handled
        widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        # limit the number of items
        widget.setMaxCount(4)

        widget.currentIndexChanged.connect(self._index_changed)
        widget.currentTextChanged.connect(self._text_changed)

        self.setCentralWidget(widget)

    def _index_changed(self, i):
        print(i)

    def _text_changed(self, s):
        print(s)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
