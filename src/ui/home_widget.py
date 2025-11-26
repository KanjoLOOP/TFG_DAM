from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class HomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Bienvenido al Gestor 3D")
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(label)
        layout.addStretch()
        self.setLayout(layout)
