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
    QVBoxLayout,
    QWidget,
    QListWidget,
    QLabel
)

# variables
owned_items = []

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        

        # create layout
        layout = QVBoxLayout()

        # add list of buyable items
        self.shop_list = QListWidget()
        self.shop_list.addItems(["item1", "item2", "item3"])
        self.shop_list.itemClicked.connect(self.buy_item)

        # add a label to display owned items
        self.inventory = QLabel("Inventory: ")

        # add widgets & layouts to main layout
        layout.addWidget(self.shop_list)
        layout.addWidget(self.inventory)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def buy_item(self):
        stringItemsList = ""
        owned_items.append(self.shop_list.selectedItems()[0])
        for i in range (len(owned_items)):
            stringItemsList += owned_items[i].text() + ", "
        self.inventory.setText("Inventory: " + stringItemsList)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
