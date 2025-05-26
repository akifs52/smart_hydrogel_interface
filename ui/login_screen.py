from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from data.data_manager import find_user

class LoginScreen(QWidget):
    def __init__(self, login_callback, back_callback):
        super().__init__()
        self.login_callback = login_callback
        self.back_callback = back_callback
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.back_callback)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        # Önce doktor olarak ara
        user = find_user(email, password, "doctor")
        if user:
            self.login_callback(user)
            return

        # Eğer doktor bulunmazsa hasta olarak ara
        user = find_user(email, password, "patient")
        if user:
            self.login_callback(user)
            return

        # Hatalı giriş
        self.email_input.setText("")
        self.password_input.setText("")
        self.email_input.setPlaceholderText("Invalid credentials")