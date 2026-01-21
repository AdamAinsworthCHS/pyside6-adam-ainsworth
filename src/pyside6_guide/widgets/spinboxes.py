"""
spinboxes.py
by HundredVisionsGuy
A demo of the two main types of spinboxes
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rectangle Area Calculator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        # TODO: Create An HBox Layout with a QSpinBox that gets a whole number
        layout = QHBoxLayout()

        self.long = QDoubleSpinBox()

        # TODO: Create another HBox that gets a number with a decimal point
        self.wide = QDoubleSpinBox()

        # TODO: Add 2 buttons in an hbox: one for calculating & a clear button
        self.calculate_button = QPushButton("Calculate")
        self.clear_button = QPushButton("Clear")

        self.calculate_button.clicked.connect(self.calculate)
        self.clear_button.clicked.connect(self.clear)

        # TODO: Create an output label to display the instructions and results
        self.output = QLabel("Type the length and width into the provided boxes \n and press calculate to find the area of your rectangle")

        # TODO: Re-write the instructions to tell the user what to do.

        """
        Challenge: make a simple calculator app that uses 2 inputs.
            * Pick a math or science formula (like area of circle or force).
            * Change the instructions to explain what the user should do.
            * Format the results by rounding the output to 2 decimal places.
            * Format the output using clear language.
        """

        # add widgets & layouts to main layout
        layout.addWidget(self.long)
        layout.addWidget(self.wide)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.output)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
        
    def calculate(self):
        product = self.long.value() * self.wide.value()
        product = round(product, 2)
        self.output.setText("The area of the rectangle is " + str(product))
    
    def clear(self):
        self.output.setText("Type the length and width into the provided boxes \n and press calculate to find the area of your rectangle")
        self.long.setValue(0)
        self.wide.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
