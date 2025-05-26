from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
from data.data_manager import save_user

class DoctorRegistration(QWidget):
    def __init__(self, submit_callback, back_callback):
        super().__init__()
        self.submit_callback = submit_callback
        self.back_callback = back_callback
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name Surname")
        layout.addWidget(self.name_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        submit_btn = QPushButton("Register")
        submit_btn.clicked.connect(self.submit)
        layout.addWidget(submit_btn)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.back_callback)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def submit(self):
        doctor_data = {
            "name": self.name_input.text(),
            "email": self.email_input.text(),
            "password": self.password_input.text(),
            "type": "doctor"
        }

        # Kayıt işlemi
        save_user("doctor", doctor_data)

        # Dashboard'a yönlendirme
        self.submit_callback(doctor_data)