from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class WelcomeScreen(QWidget):
    def __init__(self, go_to_login, go_to_signup):
        super().__init__()
        self.setWindowTitle("Welcome - Smart Hydrogel")
        self.setFixedSize(600, 400)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Smart Hydrogel")
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        subtitle = QLabel("Precision medicine starts here…")
        subtitle.setFont(QFont("Arial", 12))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle)

        layout.addSpacing(40)

        btn_login = QPushButton("Log In")
        btn_login.setFixedSize(200, 40)
        btn_login.clicked.connect(go_to_login)
        layout.addWidget(btn_login, alignment=Qt.AlignmentFlag.AlignCenter)

        btn_signup = QPushButton("Register")
        btn_signup.setFixedSize(200, 40)
        btn_signup.clicked.connect(go_to_signup)
        layout.addWidget(btn_signup, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)