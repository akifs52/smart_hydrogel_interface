from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

class PatientDashboard(QWidget):
    def __init__(self, patient_data, back_callback=None):
        super().__init__()
        self.patient_data = patient_data
        self.back_callback = back_callback
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Başlık
        title = QLabel("SMART HYDROGELS\nfor Controlled Drug Release")
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Drug release grafiği (örnek statik resim)
        drug_release_img = QLabel()
        drug_release_img.setPixmap(QPixmap("assets/drug_release_graph.png").scaledToWidth(300))
        drug_release_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(drug_release_img)

        # pH ve sıcaklık bilgileri
        info_layout = QHBoxLayout()
        ph_label = QLabel(f"pH\n<b>{self.patient_data.get('ph', '7.2')}</b>")
        temp_label = QLabel(f"Body Temperature\n<b>{self.patient_data.get('temperature', '37.0')}°C</b>")
        for lbl in [ph_label, temp_label]:
            lbl.setFont(QFont("Arial", 14))
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            info_layout.addWidget(lbl)
        main_layout.addLayout(info_layout)

        # Hasta bilgileri kartı
        profile = QLabel(
            f"<b>Patient Profile</b><br>{self.patient_data.get('name')}<br>"
            f"Age: {self.patient_data.get('age')}<br>"
            f"Condition: {self.patient_data.get('condition')}"
        )
        profile.setAlignment(Qt.AlignmentFlag.AlignCenter)
        profile.setStyleSheet("background-color: #e8f0ff; border-radius: 10px; padding: 10px;")
        main_layout.addWidget(profile)

        # Acil durum butonu
        emergency_btn = QPushButton("EMERGENCY")
        emergency_btn.setStyleSheet("background-color: #002f6c; color: white; font-size: 16px; padding: 10px; border-radius: 8px;")
        main_layout.addWidget(emergency_btn)

        # Back tuşu
        if self.back_callback:
            back_btn = QPushButton("← Back")
            back_btn.clicked.connect(self.back_callback)
            back_btn.setStyleSheet("margin-top: 10px;")
            main_layout.addWidget(back_btn)

        self.setLayout(main_layout)