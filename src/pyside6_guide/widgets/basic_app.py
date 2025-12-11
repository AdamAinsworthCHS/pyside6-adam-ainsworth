"""
basic_app.py
by HundredVisionsGuy
A demo of the most basic input/output: labels, text inputs, and buttons.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Basic App: a simple greeting app.")

        # TODO: add a text input for user's name
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your name here.")

        # input field to add location
        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText("Enter your location here.")

        # TODO: add a push button to greet user
        greeting_button = QPushButton("Get Greeting")
        greeting_button.clicked.connect(self.get_greeting)

        # push button that clears the app
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_app)

        # TODO: add a label to greet user
        greeting = "Enter your name, then press the get greeting button"
        self.greeting_label = QLabel(greeting)

        """
        Challenges:
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will
                - clear the text in the name input
                - reset the output text to its initial value
            * Add an HBox for each input that contains a label (on the left)
              and input box so they line up side by side
                - then add that Hbox where you initially added the input
                - so basically instead of QVBoxLayout use HBox one.
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.location_input)
        layout.addWidget(greeting_button)
        layout.addWidget(clear_button)
        layout.addWidget(self.greeting_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def get_greeting(self):
        """get the user's name and greet the user by name"""
        username = self.username_input.text()
        location = self.location_input.text()
        greeting = f"Hello, {username} from {location} what is up?"
        self.greeting_label.setText(greeting)
    
    def clear_app(self):
        """clear the inputs and outputs"""
        self.username_input.setText("")
        self.location_input.setText("")
        greeting = "Enter your name, then press the get greeting button"
        self.greeting_label.setText(greeting)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
