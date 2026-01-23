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

# shopitem class
class ShopItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# variables
owned_items = []
healing_potion = ShopItem("Healing Potion", 40)
mana_potion = ShopItem("Mana Potion", 30)
copper_blade = ShopItem("Copper Blade", 50)
copper_helm = ShopItem("Copper Helm", 70)
copper_shield = ShopItem("Copper Shield", 60)
shop_items = [healing_potion, mana_potion, copper_blade, copper_helm, copper_shield]
shop_items_string = [
    healing_potion.name + " ($40)", 
    mana_potion.name + " ($30)", 
    copper_blade.name + " ($50)", 
    copper_helm.name + " ($70)", 
    copper_shield.name + " ($60)"
]



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        # money variable
        self.money = 200

        # create layout
        layout = QVBoxLayout()

        # add a label to display money
        self.money_label = QLabel("Money: 200")

        # add list of buyable items
        self.shop_list = QListWidget()
        self.shop_list.addItems(shop_items_string)
        self.shop_list.itemClicked.connect(self.buy_item)

        # add a label to display owned items
        self.inventory_label = QLabel("Inventory: ")

        # add widgets & layouts to main layout
        layout.addWidget(self.money_label)
        layout.addWidget(self.shop_list)
        layout.addWidget(self.inventory_label)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def buy_item(self):
        string_items_list = ""
        item_pos = shop_items_string.index(self.shop_list.selectedItems()[0].text())
        if self.money >= shop_items[item_pos].price:
            self.money -= shop_items[item_pos].price
            owned_items.append(shop_items[item_pos])
            
            for i in range (len(owned_items)):
                string_items_list += owned_items[i].name + ", "
            self.inventory_label.setText("Inventory: " + string_items_list)
            self.money_label.setText("Money: " + "$" + str(self.money))

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
