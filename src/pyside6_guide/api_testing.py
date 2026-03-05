"""
api_testing.py
by Adam Ainsworth
Api stuff
"""

import sys
import requests
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QWidget
)

# q applicaiton
app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fruit Api")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 400)

        # create layout
        layout = QVBoxLayout()

        # add labels
        instructions = QLabel("Push a button, get FRUIT DATA")
        self.output = QLabel("Output: ")

        # add button
        self.apple_button = QPushButton("Apple")
        self.apple_button.clicked.connect(self.GiveDataApple)
        self.blackberry_button = QPushButton("Blackberry")
        self.blackberry_button.clicked.connect(self.GiveDataBlackberry)
        self.mango_button = QPushButton("Mango")
        self.mango_button.clicked.connect(self.GiveDataMango)

        # add widgets & layouts to main layout
        layout.addWidget(instructions)
        layout.addWidget(self.apple_button)
        layout.addWidget(self.blackberry_button)
        layout.addWidget(self.mango_button)
        layout.addWidget(self.output)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def GiveDataApple(self):
        url = "https://www.fruityvice.com/api/fruit/apple"
        response = requests.get(url)
        data = response.json()
        self.output.setText("Output: " + str(data))
    
    def GiveDataBlackberry(self):
        url = "https://www.fruityvice.com/api/fruit/blackberry"
        response = requests.get(url)
        data = response.json()
        self.output.setText("Output: " + str(data))

    def GiveDataMango(self):
        url = "https://www.fruityvice.com/api/fruit/mango"
        response = requests.get(url)
        data = response.json()
        self.output.setText("Output: " + str(data))

        


if __name__ == "__main__":
    window = MainWindow()
    window.show()

    app.exec()


