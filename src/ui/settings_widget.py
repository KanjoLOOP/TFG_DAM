from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QComboBox, QCheckBox, QTextEdit, QPushButton, QFrame, QMessageBox)
from PyQt5.QtCore import Qt, pyqtSignal

class SettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Título
        title = QLabel("Configuración")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #e0e0e0; margin-bottom: 20px;")
        main_layout.addWidget(title)

        # --- Sección General (Idioma y Tema) ---
        general_frame = QFrame()
        general_frame.setObjectName("Card")
        general_layout = QVBoxLayout(general_frame)
        general_layout.setContentsMargins(20, 20, 20, 20)
        
        gen_title = QLabel("General")
        gen_title.setStyleSheet("font-size: 18px; font-weight: 600; color: #e0e0e0; border: none; margin-bottom: 10px;")
        general_layout.addWidget(gen_title)



        # Idioma
        lang_layout = QHBoxLayout()
        lang_label = QLabel("Idioma:")
        lang_label.setStyleSheet("font-size: 14px; color: #e0e0e0; border: none;")
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["Español", "English", "Français"])
        self.lang_combo.setStyleSheet("""
            QComboBox {
                background-color: #333333;
                color: white;
                border: 1px solid #555;
                padding: 5px;
                border-radius: 4px;
                min-width: 150px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #333333;
                color: white;
                selection-background-color: #555;
                selection-color: white;
            }
        """)
        lang_layout.addWidget(lang_label)
        lang_layout.addWidget(self.lang_combo)
        lang_layout.addStretch()
        general_layout.addLayout(lang_layout)

        main_layout.addWidget(general_frame)

        # --- Sección Reportar Error ---
        report_frame = QFrame()
        report_frame.setObjectName("Card")
        report_layout = QVBoxLayout(report_frame)
        report_layout.setContentsMargins(20, 20, 20, 20)
        
        rep_title = QLabel("Reportar Error")
        rep_title.setStyleSheet("font-size: 18px; font-weight: 600; color: #e0e0e0; border: none; margin-bottom: 10px;")
        report_layout.addWidget(rep_title)
        
        report_desc = QLabel("Describe el problema que has encontrado:")
        report_desc.setStyleSheet("color: #b0b0b0; margin-bottom: 5px; border: none;")
        report_layout.addWidget(report_desc)

        self.error_text = QTextEdit()
        self.error_text.setPlaceholderText("Escribe aquí los detalles del error...")
        self.error_text.setMinimumHeight(100)
        self.error_text.setStyleSheet("""
            QTextEdit {
                background-color: #333;
                color: #e0e0e0;
                border: 1px solid #555;
                border-radius: 4px;
                padding: 10px;
            }
        """)
        report_layout.addWidget(self.error_text)

        btn_layout = QHBoxLayout()
        self.send_btn = QPushButton("Enviar Reporte")
        self.send_btn.setCursor(Qt.PointingHandCursor)
        self.send_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        self.send_btn.clicked.connect(self.submit_report)
        btn_layout.addStretch()
        btn_layout.addWidget(self.send_btn)
        report_layout.addLayout(btn_layout)

        main_layout.addWidget(report_frame)
        
        main_layout.addStretch()
        self.setLayout(main_layout)

    def submit_report(self):
        text = self.error_text.toPlainText()
        if not text.strip():
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Reporte vacío")
            msg_box.setText("Por favor describe el error antes de enviar.")
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.addButton("Aceptar", QMessageBox.AcceptRole)
            msg_box.exec_()
            return
        
        # Aquí iría la lógica real de envío
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Reporte Enviado")
        msg_box.setText("Gracias por tu reporte. Lo revisaremos pronto.")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton("Aceptar", QMessageBox.AcceptRole)
        msg_box.exec_()
        self.error_text.clear()
