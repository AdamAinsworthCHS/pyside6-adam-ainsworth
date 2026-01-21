"""
app_with_style.py
by HundredVisionsGuy
A styling challenge to adjust sizes and styles of
fonts and colors.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QListWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        # create layout
        layout = QVBoxLayout()

        # add list of buyable items
        shop_list = QListWidget()
        shop_list.addItems(["item1", "item2", "item3"])

        # add widgets & layouts to main layout
        layout.addWidget(shop_list)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
