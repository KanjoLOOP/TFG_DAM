import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class Gestor3DApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor 3D")
        self.setGeometry(100, 100, 800, 600)
        
        label = QLabel("Bienvenido a Gestor 3D", self)
        label.move(350, 250)
        label.adjustSize()

def main():
    app = QApplication(sys.argv)
    window = Gestor3DApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
