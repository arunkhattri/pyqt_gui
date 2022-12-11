# 06_widgets_line_edit.py

"""QLineEdit"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text ...")

        widget.returnPressed.connect(self._return_pressed)
        widget.selectionChanged.connect(self._selection_changed)
        widget.textChanged.connect(self._text_changed)
        widget.textEdited.connect(self._text_edited)

        self.setCentralWidget(widget)

    def _return_pressed(self):
        print("Return Pressed!")
        self.centralWidget().setText("BOOM!")

    def _selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def _text_changed(self, s):
        print("Text changed")
        print(s)

    def _text_edited(self, s):
        print("Text edited")
        print(s)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
