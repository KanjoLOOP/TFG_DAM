import sys
import os

# Añadir el directorio raíz al path para que funcionen los imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt5.QtWidgets import QApplication
from src.ui.main_window import MainWindow
from src.ui.login_widget import LoginWidget
from src.logic.auth_manager import AuthManager

class App:
    """Clase principal que maneja el ciclo de vida de la aplicación."""
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setStyle("Fusion")  # Forzar estilo Fusion
        self.auth_manager = AuthManager()
        self.login_widget = None
        self.main_window = None
        
    def show_login(self):
        """Muestra la pantalla de login."""
        self.login_widget = LoginWidget(self.auth_manager)
        self.login_widget.login_successful.connect(self.on_login_successful)
        self.login_widget.show()
    
    def on_login_successful(self, user):
        """Callback cuando el login es exitoso."""
        if self.login_widget:
            self.login_widget.close()
            self.login_widget = None
        
        self.main_window = MainWindow(self.auth_manager)
        self.main_window.logout_requested.connect(self.on_logout_requested)
        self.main_window.show()
    
    def on_logout_requested(self):
        """Callback cuando se solicita cerrar sesión."""
        if self.main_window:
            self.main_window.close()
            self.main_window = None
        
        # Volver a mostrar login
        self.show_login()
    
    def run(self):
        """Inicia la aplicación."""
        self.show_login()
        return self.app.exec_()

def main():
    app = App()
    sys.exit(app.run())

if __name__ == "__main__":
    main()

