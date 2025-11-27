from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QListWidget, QFileDialog, QMessageBox, QSplitter, QLineEdit, QFrame, QLabel)
from src.ui.utils import MessageBoxHelper
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from src.logic.library_manager import LibraryManager
from src.ui.viewer_3d import Viewer3DWidget

class LibraryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = LibraryManager()
        self.init_ui()
        self.refresh_list()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20) # Margen generoso
        layout.setSpacing(20)
        
        # --- Toolbar Superior ---
        toolbar = QHBoxLayout()
        toolbar.setSpacing(15)
        
        # Búsqueda moderna
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Buscar modelo...")
        self.search_input.setProperty("class", "ModernInput") # Usar propiedad dinámica si Qt lo soporta, o setObjectName
        self.search_input.setObjectName("ModernInput") # Mapeado en QSS como QLineEdit#ModernInput o .ModernInput si usamos setStyleSheet manual
        # Nota: En QSS global definí QLineEdit.ModernInput, así que debo usar setProperty o heredar.
        # Para simplificar, aplicaré el estilo directamente aquí o usaré el objectName si ajusto el QSS.
        # Ajustaré el QSS para usar selector de clase fake si es necesario, pero por ahora setStyleSheet directo para asegurar.
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #2a2a2a;
                border: 1px solid #3a3a3a;
                border-radius: 20px;
                padding: 8px 15px;
                font-size: 14px;
                color: #e0e0e0;
            }
            QLineEdit:focus {
                border: 1px solid #00bcd4;
                background-color: #333333;
            }
        """)
        self.search_input.textChanged.connect(self.filter_list)
        
        # Botones de acción
        self.btn_add = QPushButton(" + Añadir Modelo")
        self.btn_add.setCursor(Qt.PointingHandCursor)
        self.btn_add.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 600;
                font-size: 13px;
                border: none;
            }
            QPushButton:hover {
                background-color: #218838;
                margin-top: -1px; /* Sutil efecto de elevación */
            }
        """)
        self.btn_add.clicked.connect(self.add_model)
        
        self.btn_delete = QPushButton("Eliminar")
        self.btn_delete.setCursor(Qt.PointingHandCursor)
        self.btn_delete.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: 600;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        self.btn_delete.clicked.connect(self.delete_model)
        
        toolbar.addWidget(self.search_input, 1)
        toolbar.addWidget(self.btn_add)
        toolbar.addWidget(self.btn_delete)
        
        layout.addLayout(toolbar)
        
        # --- Contenido Principal (Splitter) ---
        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(1)
        splitter.setStyleSheet("QSplitter::handle { background-color: #3a3a3a; }")

        # Panel Izquierdo: Lista de Tarjetas
        list_container = QWidget()
        list_layout = QVBoxLayout(list_container)
        list_layout.setContentsMargins(0, 0, 10, 0) # Margen derecho para separar del splitter
        list_layout.setSpacing(10)
        
        # Etiqueta de sección
        lbl_list = QLabel("Mis Modelos")
        lbl_list.setStyleSheet("font-size: 14px; font-weight: bold; color: #808080; margin-bottom: 5px;")
        list_layout.addWidget(lbl_list)

        self.model_list = QListWidget()
        self.model_list.setObjectName("LibraryList") # Usa el estilo definido en QSS
        self.model_list.setSpacing(8)
        self.model_list.itemClicked.connect(self.on_model_selected)
        
        list_layout.addWidget(self.model_list)
        splitter.addWidget(list_container)

        # Panel Derecho: Visor 3D
        viewer_container = QWidget()
        viewer_layout = QVBoxLayout(viewer_container)
        viewer_layout.setContentsMargins(10, 0, 0, 0)
        viewer_layout.setSpacing(10)
        
        lbl_viewer = QLabel("Previsualización 3D")
        lbl_viewer.setStyleSheet("font-size: 14px; font-weight: bold; color: #808080; margin-bottom: 5px;")
        viewer_layout.addWidget(lbl_viewer)
        
        # Marco para el visor con bordes redondeados
        viewer_frame = QFrame()
        viewer_frame.setStyleSheet("""
            QFrame {
                background-color: #1e1e1e;
                border-radius: 12px;
                border: 1px solid #3a3a3a;
            }
        """)
        vf_layout = QVBoxLayout(viewer_frame)
        vf_layout.setContentsMargins(0, 0, 0, 0)
        
        self.viewer = Viewer3DWidget()
        # Recortar esquinas del visor (truco: el frame contenedor tiene radius, el widget hijo debe respetar)
        # Matplotlib widget a veces ignora border-radius, pero el frame visual ayuda.
        vf_layout.addWidget(self.viewer)
        
        viewer_layout.addWidget(viewer_frame)
        splitter.addWidget(viewer_container)
        
        # Configuración del splitter
        splitter.setSizes([350, 700])
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)

        layout.addWidget(splitter)
        self.setLayout(layout)

    def refresh_list(self):
        """Recarga la lista de modelos desde la BD."""
        self.model_list.clear()
        self.all_models = self.manager.get_all_models()
        self.filter_list(self.search_input.text())

    def filter_list(self, text):
        """Filtra la lista de modelos según el texto."""
        self.model_list.clear()
        if not hasattr(self, 'all_models') or not self.all_models:
            return
            
        search_text = text.lower()
        for model in self.all_models:
            if search_text in model['name'].lower():
                # Crear item con icono (simulado)
                from PyQt5.QtWidgets import QListWidgetItem
                
                item = QListWidgetItem(f"  {model['name']}")
                # item.setIcon(QIcon("path/to/icon.png")) # Si tuviéramos iconos
                item.setSizeHint(QSize(0, 50)) # Altura fija para parecer tarjeta
                
                # Guardamos el ID en el item
                item.setData(Qt.UserRole, model['id'])
                item.setData(Qt.UserRole + 1, model['file_path'])
                
                self.model_list.addItem(item)

    def add_model(self):
        """Abre diálogo para seleccionar archivo STL."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Modelo 3D", "", "Archivos STL (*.stl)")
        if file_path:
            import os
            name = os.path.basename(file_path)
            
            success, msg = self.manager.add_model(file_path, name)
            if success:
                self.refresh_list()
                MessageBoxHelper.show_info(self, "Éxito", msg)
            else:
                MessageBoxHelper.show_warning(self, "Error", msg)

    def delete_model(self):
        """Elimina el modelo seleccionado."""
        current_item = self.model_list.currentItem()
        if not current_item:
            return
        
        model_id = current_item.data(Qt.UserRole)
        
        if MessageBoxHelper.ask_confirmation(self, "Confirmar", "¿Estás seguro de eliminar este modelo?"):
            if self.manager.delete_model(model_id):
                self.refresh_list()
                self.viewer.ax.clear() # Limpiar visor
                self.viewer.configure_axes() # Reconfigurar ejes vacíos
                self.viewer.canvas.draw()
            else:
                MessageBoxHelper.show_warning(self, "Error", "No se pudo eliminar el modelo.")

    def on_model_selected(self, item):
        """Carga el modelo en el visor cuando se selecciona."""
        file_path = item.data(Qt.UserRole + 1)
        self.viewer.load_model(file_path)
