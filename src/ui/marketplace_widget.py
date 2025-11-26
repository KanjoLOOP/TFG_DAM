from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QGridLayout, QLabel, 
                             QPushButton, QScrollArea, QFrame, QMessageBox)
from PyQt5.QtCore import Qt
import os

class MarketplaceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        title = QLabel("Marketplace de Modelos 3D")
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(title)

        # Área de scroll para los items
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")
        
        content_widget = QWidget()
        self.grid_layout = QGridLayout(content_widget)
        self.grid_layout.setSpacing(20)

        # Datos simulados
        self.mock_items = [
            {"name": "Soporte Auriculares", "price": "Gratis", "desc": "Soporte universal para mesa."},
            {"name": "Maceta Low Poly", "price": "2.50 €", "desc": "Diseño geométrico moderno."},
            {"name": "Engranaje Helicoidal", "price": "5.00 €", "desc": "Pieza mecánica funcional."},
            {"name": "Figura Dragón", "price": "10.00 €", "desc": "Modelo detallado para resina."},
            {"name": "Caja Organizadora", "price": "Gratis", "desc": "Modular y apilable."},
            {"name": "Llavero Personalizable", "price": "1.00 €", "desc": "Fácil de editar."}
        ]

        # Crear tarjetas
        for i, item in enumerate(self.mock_items):
            card = self.create_item_card(item)
            row = i // 3
            col = i % 3
            self.grid_layout.addWidget(card, row, col)

        # Rellenar espacios vacíos si hay pocos items para mantener alineación
        self.grid_layout.setRowStretch(self.grid_layout.rowCount(), 1)
        self.grid_layout.setColumnStretch(self.grid_layout.columnCount(), 1)

        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        self.setLayout(layout)

    def create_item_card(self, item_data):
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #3a3a3a;
                border-radius: 8px;
                border: 1px solid #555;
            }
            QFrame:hover {
                border: 1px solid #0d6efd;
            }
        """)
        card.setFixedSize(250, 300)
        
        layout = QVBoxLayout(card)
        
        # Placeholder de imagen
        img_placeholder = QLabel("IMG")
        img_placeholder.setAlignment(Qt.AlignCenter)
        img_placeholder.setStyleSheet("background-color: #222; color: #666; font-weight: bold; font-size: 20px;")
        img_placeholder.setFixedHeight(150)
        layout.addWidget(img_placeholder)

        # Info
        name = QLabel(item_data["name"])
        name.setStyleSheet("font-size: 16px; font-weight: bold; border: none;")
        layout.addWidget(name)

        desc = QLabel(item_data["desc"])
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #aaa; font-size: 12px; border: none;")
        layout.addWidget(desc)

        price = QLabel(item_data["price"])
        price.setStyleSheet("color: #0d6efd; font-weight: bold; font-size: 14px; border: none;")
        layout.addWidget(price)

        btn_buy = QPushButton("Obtener" if item_data["price"] == "Gratis" else "Comprar")
        btn_buy.clicked.connect(lambda: self.buy_item(item_data["name"]))
        layout.addWidget(btn_buy)

        return card

    def buy_item(self, name):
        # Simulación de compra
        QMessageBox.information(self, "Compra Exitosa", f"Has adquirido '{name}'.\n(Simulación: El modelo se añadiría a tu biblioteca)")
