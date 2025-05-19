from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class UserTypeSelection(QWidget):
    def __init__(self, go_to_patient, go_to_doctor, back_callback=None):
        super().__init__()
        self.go_to_patient = go_to_patient
        self.go_to_doctor = go_to_doctor
        self.back_callback = back_callback

        layout = QVBoxLayout()

        patient_button = QPushButton("I'm a Patient")
        patient_button.clicked.connect(self.go_to_patient)
        layout.addWidget(patient_button)

        doctor_button = QPushButton("I'm a Doctor")
        doctor_button.clicked.connect(self.go_to_doctor)
        layout.addWidget(doctor_button)

        if self.back_callback:
            back_button = QPushButton("Back")
            back_button.clicked.connect(self.back_callback)
            layout.addWidget(back_button)

        self.setLayout(layout)