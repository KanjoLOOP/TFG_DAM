from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QFormLayout, QGroupBox, QSpinBox,
                             QGridLayout, QFrame, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
from src.logic.cost_calculator import CostCalculator
from src.logic.report_generator import ReportGenerator

class CalculatorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.calculator = CostCalculator()
        self.report_generator = ReportGenerator()
        self.last_calculation = None
        self.init_ui()

    def init_ui(self):
        # Estilo global
        # Estilo global movido a QSS
        pass

        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Título
        title = QLabel("Calculadora de Costes")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: white; padding: 0 0 10px 0;")
        main_layout.addWidget(title)

        # === PARÁMETROS DE CÁLCULO ===
        params_group = QGroupBox("Parámetros de Cálculo")
        params_layout = QGridLayout()
        params_layout.setSpacing(20)
        params_layout.setContentsMargins(15, 25, 15, 15)

        self.input_price_kg = QLineEdit("20")
        self.input_price_kg.setPlaceholderText("Ej: 20.00")
        params_layout.addLayout(self.create_v_input("Precio Filamento (€/kg):", self.input_price_kg), 0, 0)

        self.input_power = QLineEdit("350")
        params_layout.addLayout(self.create_v_input("Consumo (Watts):", self.input_power), 0, 1)

        self.input_energy_cost = QLineEdit("0.15")
        params_layout.addLayout(self.create_v_input("Coste Energía (€/kWh):", self.input_energy_cost), 0, 2)

        params_group.setLayout(params_layout)
        main_layout.addWidget(params_group, 1)

        # === PIEZA ===
        pieza_group = QGroupBox("Datos de la Pieza")
        pieza_layout = QGridLayout()
        pieza_layout.setSpacing(20)
        pieza_layout.setContentsMargins(15, 25, 15, 15)

        # Tiempo (H/Min)
        time_widget = QWidget()
        time_box = QHBoxLayout(time_widget)
        time_box.setContentsMargins(0, 0, 0, 0)
        time_box.setSpacing(5)
        
        self.input_hours = QSpinBox()
        self.input_hours.setRange(0, 999)
        self.input_hours.setSuffix(" h")
        self.input_hours.setValue(5)
        
        self.input_minutes = QSpinBox()
        self.input_minutes.setRange(0, 59)
        self.input_minutes.setSuffix(" m")
        self.input_minutes.setValue(0)
        
        time_box.addWidget(self.input_hours)
        time_box.addWidget(self.input_minutes)
        
        pieza_layout.addLayout(self.create_v_input("Tiempo de Impresión:", time_widget), 0, 0)

        self.input_weight = QLineEdit()
        self.input_weight.setPlaceholderText("Ej: 157")
        pieza_layout.addLayout(self.create_v_input("Peso (g):", self.input_weight), 0, 1)

        self.input_supplies = QLineEdit("0")
        pieza_layout.addLayout(self.create_v_input("Insumos Extra (€):", self.input_supplies), 0, 2)

        pieza_group.setLayout(pieza_layout)
        main_layout.addWidget(pieza_group, 1)

        # === GANANCIA ===
        ganancia_group = QGroupBox("Ganancia y Margen")
        ganancia_layout = QHBoxLayout()
        ganancia_layout.setSpacing(25)
        ganancia_layout.setContentsMargins(15, 25, 15, 15)

        self.input_margin = QLineEdit("4")
        ganancia_layout.addLayout(self.create_v_input("Multiplicador:", self.input_margin), 1)

        ref_frame = QFrame()
        ref_frame.setObjectName("Card")
        ref_frame.setStyleSheet("padding: 5px;") # Keep padding override if needed, or move to QSS
        ref_box = QVBoxLayout(ref_frame)
        ref_box.setContentsMargins(5, 5, 5, 5)
        ref_label = QLabel("Referencias:  Minorista → x4  |  Mayorista → x3  |  Llaveros → x5")
        ref_label.setStyleSheet("color: #aaa; font-size: 13px; font-style: italic;")
        ref_label.setAlignment(Qt.AlignCenter)
        ref_box.addWidget(ref_label)
        
        ganancia_layout.addWidget(ref_frame, 2)

        ganancia_group.setLayout(ganancia_layout)
        main_layout.addWidget(ganancia_group, 1)

        # Botones de Acción
        btn_layout = QHBoxLayout()
        
        self.btn_calculate = QPushButton("CALCULAR RESULTADOS")
        self.btn_calculate.setCursor(Qt.PointingHandCursor)
        self.btn_calculate.setStyleSheet("""
            QPushButton {
                background-color: #8b0000;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #a00000;
            }
        """)
        self.btn_calculate.clicked.connect(self.calculate)
        btn_layout.addWidget(self.btn_calculate)
        
        self.btn_export = QPushButton("EXPORTAR PDF")
        self.btn_export.setCursor(Qt.PointingHandCursor)
        self.btn_export.setStyleSheet("""
            QPushButton {
                background-color: #2C3E50;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #34495E;
            }
        """)
        self.btn_export.clicked.connect(self.export_pdf)
        self.btn_export.setEnabled(False) # Deshabilitado hasta calcular
        btn_layout.addWidget(self.btn_export)
        
        main_layout.addLayout(btn_layout)

        # === RESULTADOS ===
        results_group = QGroupBox("Desglose de Costes")
        results_layout = QGridLayout()
        results_layout.setSpacing(15)
        results_layout.setContentsMargins(15, 25, 15, 15)

        self.lbl_filament_cost = self.create_result_card("Filamento", "0.00 €")
        results_layout.addWidget(self.lbl_filament_cost, 0, 0)

        self.lbl_energy_cost = self.create_result_card("Energía", "0.00 €")
        results_layout.addWidget(self.lbl_energy_cost, 0, 1)

        self.lbl_supplies_cost = self.create_result_card("Insumos", "0.00 €")
        results_layout.addWidget(self.lbl_supplies_cost, 0, 2)

        self.lbl_total_cost = self.create_result_card("COSTE TOTAL", "0.00 €")
        results_layout.addWidget(self.lbl_total_cost, 1, 0, 1, 3) # Span full width

        self.lbl_sale_price = self.create_result_card("PRECIO VENTA", "0.00 €", big=True)
        results_layout.addWidget(self.lbl_sale_price, 2, 0, 1, 3) # Span full width

        results_group.setLayout(results_layout)
        main_layout.addWidget(results_group, 1)

        self.setLayout(main_layout)

    def create_v_input(self, text, widget):
        """Crea un layout vertical con etiqueta y widget."""
        lay = QVBoxLayout()
        lay.setSpacing(5)
        lay.setContentsMargins(0, 0, 0, 0)
        label = QLabel(text)
        lay.addWidget(label)
        lay.addWidget(widget)
        return lay

    def create_result_card(self, title, value, color_bg="#2a2a2a", big=False):
        """Crea una tarjeta para mostrar resultados."""
        card = QFrame()
        card = QFrame()
        card.setObjectName("Card")
        lay = QHBoxLayout(card)
        lay.setContentsMargins(10, 8, 10, 8)
        
        lbl_title = QLabel(title)
        lbl_title.setStyleSheet("color: #bbb; font-weight: bold; border: none; background: transparent;")
        
        lbl_val = QLabel(value)
        font_size = "26px" if big else "18px"
        lbl_val.setStyleSheet(f"color: white; font-weight: bold; font-size: {font_size}; border: none; background: transparent;")
        lbl_val.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        lay.addWidget(lbl_title)
        lay.addStretch()
        lay.addWidget(lbl_val)
        
        # Guardamos referencia al label de valor para actualizarlo luego
        card.value_label = lbl_val 
        return card

    def calculate(self):
        try:
            # Obtener valores
            hours = self.input_hours.value()
            minutes = self.input_minutes.value()
            total_time = hours + (minutes / 60.0)  # Convertir a horas decimales
            
            weight = float(self.input_weight.text() or 0)
            supplies = float(self.input_supplies.text() or 0)
            margin = float(self.input_margin.text() or 1)
            
            price_kg = float(self.input_price_kg.text() or 0)
            power = float(self.input_power.text() or 0)
            energy_price = float(self.input_energy_cost.text() or 0)

            # Calcular costes
            filament_cost = self.calculator.calculate_filament_cost(weight, price_kg)
            energy_cost = self.calculator.calculate_energy_cost(power, total_time, energy_price)
            total_cost = self.calculator.calculate_total_cost(filament_cost, energy_cost, supplies)
            
            # Calcular precio de venta
            sale_price = self.calculator.calculate_sale_price(total_cost, margin)

            # Mostrar resultados con colores discretos
            # Mostrar resultados
            self.lbl_filament_cost.value_label.setText(f"{filament_cost:.2f} €")
            self.lbl_energy_cost.value_label.setText(f"{energy_cost:.2f} €")
            self.lbl_supplies_cost.value_label.setText(f"{supplies:.2f} €")
            self.lbl_total_cost.value_label.setText(f"{total_cost:.2f} €")
            self.lbl_sale_price.value_label.setText(f"{sale_price:.2f} €")
            
            # Guardar datos para exportación
            self.last_calculation = {
                'weight': weight,
                'time': total_time,
                'price_per_kg': price_kg,
                'power': power,
                'energy_cost_rate': energy_price,
                'filament_cost': filament_cost,
                'energy_cost': energy_cost,
                'total_cost': total_cost
            }
            self.btn_export.setEnabled(True)
            
        except ValueError:
            self.lbl_total_cost.value_label.setText("Error")
            self.btn_export.setEnabled(False)

        except ValueError:
            self.lbl_total_cost.value_label.setText("Error: Ingrese valores numéricos válidos")
            self.lbl_sale_price.value_label.setText("")
            self.btn_export.setEnabled(False)

    def export_pdf(self):
        """Exporta los resultados a PDF."""
        if not self.last_calculation:
            return
            
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Guardar Informe", "", "Archivos PDF (*.pdf)"
        )
        
        if file_path:
            if not file_path.endswith('.pdf'):
                file_path += '.pdf'
                
            try:
                self.report_generator.generate_cost_report(self.last_calculation, file_path)
                QMessageBox.information(self, "Éxito", "Informe guardado correctamente")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo guardar el informe: {str(e)}")
