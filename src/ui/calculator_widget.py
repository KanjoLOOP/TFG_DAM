from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QFormLayout, QGroupBox)
from PyQt5.QtCore import Qt
from src.logic.cost_calculator import CostCalculator

class CalculatorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.calculator = CostCalculator()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        # Título
        title = QLabel("Calculadora de Costes de Impresión")
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)

        # Formulario de Entrada
        form_group = QGroupBox("Parámetros de Impresión")
        form_layout = QFormLayout()

        self.input_weight = QLineEdit()
        self.input_weight.setPlaceholderText("Ej: 150")
        form_layout.addRow("Peso del Modelo (g):", self.input_weight)

        self.input_price_kg = QLineEdit()
        self.input_price_kg.setPlaceholderText("Ej: 20.00")
        form_layout.addRow("Precio del Filamento (€/kg):", self.input_price_kg)

        self.input_time = QLineEdit()
        self.input_time.setPlaceholderText("Ej: 5.5")
        form_layout.addRow("Tiempo de Impresión (horas):", self.input_time)

        self.input_power = QLineEdit()
        self.input_power.setText("350") # Valor por defecto común
        form_layout.addRow("Consumo Impresora (Watts):", self.input_power)

        self.input_energy_cost = QLineEdit()
        self.input_energy_cost.setText("0.15") # Valor por defecto
        form_layout.addRow("Coste Energía (€/kWh):", self.input_energy_cost)

        form_group.setLayout(form_layout)
        layout.addWidget(form_group)

        # Botón Calcular
        self.btn_calculate = QPushButton("Calcular Coste Total")
        self.btn_calculate.clicked.connect(self.calculate)
        layout.addWidget(self.btn_calculate)

        # Resultados
        results_group = QGroupBox("Resultados")
        results_layout = QVBoxLayout()

        self.lbl_filament_cost = QLabel("Coste Filamento: 0.00 €")
        self.lbl_energy_cost = QLabel("Coste Energía: 0.00 €")
        self.lbl_total_cost = QLabel("COSTE TOTAL: 0.00 €")
        self.lbl_total_cost.setStyleSheet("font-size: 16px; font-weight: bold; color: #0d6efd;")

        results_layout.addWidget(self.lbl_filament_cost)
        results_layout.addWidget(self.lbl_energy_cost)
        results_layout.addWidget(self.lbl_total_cost)
        results_group.setLayout(results_layout)
        layout.addWidget(results_group)

        layout.addStretch()
        self.setLayout(layout)

    def calculate(self):
        try:
            weight = float(self.input_weight.text() or 0)
            price_kg = float(self.input_price_kg.text() or 0)
            time = float(self.input_time.text() or 0)
            power = float(self.input_power.text() or 0)
            energy_price = float(self.input_energy_cost.text() or 0)

            filament_cost = self.calculator.calculate_filament_cost(weight, price_kg)
            energy_cost = self.calculator.calculate_energy_cost(power, time, energy_price)
            total_cost = self.calculator.calculate_total_cost(filament_cost, energy_cost)

            self.lbl_filament_cost.setText(f"Coste Filamento: {filament_cost:.2f} €")
            self.lbl_energy_cost.setText(f"Coste Energía: {energy_cost:.2f} €")
            self.lbl_total_cost.setText(f"COSTE TOTAL: {total_cost:.2f} €")

        except ValueError:
            self.lbl_total_cost.setText("Error: Ingrese valores numéricos válidos")
            self.lbl_total_cost.setStyleSheet("font-size: 16px; font-weight: bold; color: red;")
