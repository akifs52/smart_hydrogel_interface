from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class LoginScreen(QWidget):
    def __init__(self, login_success_callback, back_callback):
        super().__init__()
        self.login_success_callback = login_success_callback
        self.back_callback = back_callback

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Email:"))
        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        layout.addWidget(QLabel("Password:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Log In")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.back_callback)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def handle_login(self):
        from data.data_manager import find_user  # local import to avoid circular imports
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        user = find_user(email, password)
        if user:
            QMessageBox.information(self, "Login Success", f"Welcome {user['type'].capitalize()}!")
            self.login_success_callback(user)
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect email or password.")