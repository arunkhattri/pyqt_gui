#!/usr/bin/env python3
"""Simple Hello, World example with PyQt6."""

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# Create an instance of QApplication
app = QApplication([])

# Create your application's GUI
window = QWidget()
window.setWindowTitle("PyQt App")

# window's size and screen position.
# first 2 args: x & y screen coordinates
# 3rd and 4th: width and height
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)

# place helloMsg at given coordinates on the Application's window.
helloMsg.move(60, 15)

# show your application's GUI
window.show()

# Run application's event loop
sys.exit(app.exec())
