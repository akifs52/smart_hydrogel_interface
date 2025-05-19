import sys
from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt6.QtCore import Qt
from ui.login_screen import LoginScreen
from ui.splash_screen import SplashScreen
from ui.welcome_screen import WelcomeScreen
from ui.patient_registration import PatientRegistration
from ui.doctor_registration import DoctorRegistration
from ui.user_type_selection import UserTypeSelection
from ui.patient_dashboard import PatientDashboard
from data.data_manager import save_user, load_users, find_user

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Hydrogel")
        self.setGeometry(100, 100, 800, 600)

        # Splash Screen ile başla
        self.splash = SplashScreen(self.show_welcome)
        self.setCentralWidget(self.splash)

    def show_welcome(self):
        self.welcome = WelcomeScreen(
            go_to_login=self.show_login,
            go_to_signup=self.show_registration_choice
        )
        self.setCentralWidget(self.welcome)

    def show_login(self):
        self.login_screen = LoginScreen(
            login_callback=self.handle_login,
            back_callback=self.show_welcome
        )
        self.setCentralWidget(self.login_screen)

    def handle_login(self, email, password, user_type):
        user = find_user(email, password, user_type)
        if user:
            if user_type == "patient":
                self.show_patient_dashboard(user)
            elif user_type == "doctor":
                self.show_doctor_dashboard(user)
        else:
        # Geçersiz girişte tekrar login ekranı göster
            self.show_login()

    def show_registration_choice(self):
        self.user_type_selection = UserTypeSelection(
            go_to_patient=self.show_patient_registration,
            go_to_doctor=self.show_doctor_registration,
            back_callback=self.show_welcome
        )
        self.setCentralWidget(self.user_type_selection)

    def show_patient_registration(self):
        self.patient_registration = PatientRegistration(
            submit_callback=self.show_patient_dashboard,  # Artık hasta bilgisi alacak
            back_callback=self.show_registration_choice
        )
        self.setCentralWidget(self.patient_registration)


    def show_doctor_registration(self):
        self.doctor_registration = DoctorRegistration(
            submit_callback=self.show_doctor_dashboard,
            back_callback=self.show_registration_choice
        )
        self.setCentralWidget(self.doctor_registration)

    def show_patient_dashboard(self, user_data=None):
        label = QLabel(f"Hoş geldiniz, {user_data['name']}" if user_data else "Hasta Paneli (Geliştirilecek)")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

    def show_doctor_dashboard(self):
        label = QLabel("Doktor Paneli (Geliştirilecek)")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())