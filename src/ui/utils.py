from PyQt5.QtWidgets import QMessageBox

class MessageBoxHelper:
    """Helper para mostrar mensajes estandarizados con estilo consistente."""
    
    @staticmethod
    def _apply_style(msg_box):
        """Aplica el estilo visual blanco/claro al QMessageBox."""
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #ffffff;
                color: #000000;
            }
            QLabel {
                color: #000000;
                background-color: transparent;
                background: transparent;
                background: none;
                border: none;
                font-size: 14px;
            }
            QPushButton {
                background-color: #f0f0f0;
                color: #000000;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 6px 20px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)

    @staticmethod
    def show_info(parent, title, text):
        """Muestra un mensaje de información."""
        msg = QMessageBox(parent)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        MessageBoxHelper._apply_style(msg)
        msg.addButton("Aceptar", QMessageBox.AcceptRole)
        msg.exec_()

    @staticmethod
    def show_warning(parent, title, text):
        """Muestra un mensaje de advertencia."""
        msg = QMessageBox(parent)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        MessageBoxHelper._apply_style(msg)
        msg.addButton("Aceptar", QMessageBox.AcceptRole)
        msg.exec_()

    @staticmethod
    def show_error(parent, title, text):
        """Muestra un mensaje de error."""
        msg = QMessageBox(parent)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        MessageBoxHelper._apply_style(msg)
        msg.addButton("Aceptar", QMessageBox.AcceptRole)
        msg.exec_()

    @staticmethod
    def ask_confirmation(parent, title, text):
        """Muestra un diálogo de confirmación (Sí/No). Retorna True si es Sí."""
        msg = QMessageBox(parent)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Question)
        MessageBoxHelper._apply_style(msg)
        btn_yes = msg.addButton("Sí", QMessageBox.YesRole)
        btn_no = msg.addButton("No", QMessageBox.NoRole)
        msg.exec_()
        return msg.clickedButton() == btn_yes
