import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.login_screen import LoginScreen
from ui.splash_screen import SplashScreen
from ui.welcome_screen import WelcomeScreen
from ui.patient_registration import PatientRegistration
from ui.doctor_registration import DoctorRegistration
from ui.user_type_selection import UserTypeSelection
from ui.patient_dashboard import PatientDashboard
from ui.doctor_dashboard import DoctorDashboard  # Eğer varsa
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

    def handle_login(self, user):
        if user["type"] == "patient":
            self.show_patient_dashboard(user)
        elif user["type"] == "doctor":
            self.show_doctor_dashboard(user)

    def show_registration_choice(self):
        self.user_type_selection = UserTypeSelection(
            go_to_patient=self.show_patient_registration,
            go_to_doctor=self.show_doctor_registration,
            back_callback=self.show_welcome
        )
        self.setCentralWidget(self.user_type_selection)

    def show_patient_registration(self):
        self.patient_registration = PatientRegistration(
            submit_callback=self.show_patient_dashboard,
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
        self.patient_dashboard = PatientDashboard(user_data or {})
        self.setCentralWidget(self.patient_dashboard)

    def show_doctor_dashboard(self, user_data=None):
        if user_data:
            self.doctor_dashboard = DoctorDashboard(user_data)
            self.setCentralWidget(self.doctor_dashboard)
        else:
            from PyQt6.QtWidgets import QLabel
            label = QLabel("Doktor Paneli (Geliştirilecek)")
            self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
