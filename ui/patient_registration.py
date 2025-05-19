from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from data.data_manager import save_user

class PatientRegistration(QWidget):
    def __init__(self, submit_callback, back_callback):
        super().__init__()
        self.submit_callback = submit_callback
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

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name Surname")
        layout.addWidget(self.name_input)

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")
        layout.addWidget(self.age_input)

        self.gender_input = QComboBox()
        self.gender_input.addItems(["Female", "Male"])
        layout.addWidget(self.gender_input)

        self.condition_input = QLineEdit()
        self.condition_input.setPlaceholderText("Condition (ex: diabetes)")
        layout.addWidget(self.condition_input)

        self.hydrogel_input = QLineEdit()
        self.hydrogel_input.setPlaceholderText("Type of Hydrogel")
        layout.addWidget(self.hydrogel_input)

        self.start_date_input = QLineEdit()
        self.start_date_input.setPlaceholderText("Treatment Start Date (dd/mm/yyyy)")
        layout.addWidget(self.start_date_input)

        self.emergency_contact_input = QLineEdit()
        self.emergency_contact_input.setPlaceholderText("For Emergency Call: 5XX XXX XX XX")
        layout.addWidget(self.emergency_contact_input)

        submit_btn = QPushButton("Register")
        submit_btn.clicked.connect(self.submit)
        layout.addWidget(submit_btn)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.back_callback)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def submit(self):
        patient_data = {
            "email": self.email_input.text(),
            "password": self.password_input.text(),
            "name": self.name_input.text(),
            "age": self.age_input.text(),
            "gender": self.gender_input.currentText(),
            "condition": self.condition_input.text(),
            "hydrogel": self.hydrogel_input.text(),
            "start_date": self.start_date_input.text(),
            "emergency_contact": self.emergency_contact_input.text(),
            "type": "patient"
        }

        save_user("patient", patient_data)

        # Hasta kaydı başarılı, dashboard'a yönlendir
        self.submit_callback(patient_data)