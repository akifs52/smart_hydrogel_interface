from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import QRectF, Qt

class DoctorDashboard(QWidget):
    def __init__(self, user_data):
        super().__init__()
        self.setFixedSize(400, 300)
        self.setWindowTitle("Smart Hydrogel - Doctor Dashboard")
        self.user_data = user_data  # JSON'dan gelen kullanıcı verisi

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.fillRect(self.rect(), QColor("#fefefe"))

        container_rect = QRectF(20, 20, 360, 260)
        painter.setBrush(QColor("white"))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(container_rect, 20, 20)

        # Header
        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        painter.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        painter.drawText(QRectF(30, 30, 300, 40), Qt.AlignmentFlag.AlignLeft, "SMART HYDROGEL")

        # Avatar
        painter.setBrush(QColor("#aed6f1"))
        painter.drawEllipse(30, 80, 60, 60)

        # Name & Type
        painter.setPen(Qt.GlobalColor.black)
        painter.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        painter.drawText(QRectF(100, 85, 250, 30), Qt.AlignmentFlag.AlignLeft, self.user_data.get("name", "N/A"))
        painter.setFont(QFont("Arial", 10))
        painter.drawText(QRectF(100, 110, 250, 30), Qt.AlignmentFlag.AlignLeft, "Doctor")

        # Info cards
        def draw_card(x, y, title, value):
            painter.setBrush(QColor("#f6f6f6"))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRoundedRect(QRectF(x, y, 150, 60), 10, 10)
            painter.setPen(QPen(Qt.GlobalColor.black))
            painter.setFont(QFont("Arial", 10))
            painter.drawText(QRectF(x+10, y+5, 130, 20), Qt.AlignmentFlag.AlignLeft, title)
            painter.setFont(QFont("Arial", 11, QFont.Weight.Bold))
            painter.drawText(QRectF(x+10, y+25, 130, 30), Qt.AlignmentFlag.AlignLeft, value)

        draw_card(30, 160, "EMAIL", self.user_data.get("email", "N/A"))
        draw_card(220, 160, "USER TYPE", self.user_data.get("type", "N/A"))