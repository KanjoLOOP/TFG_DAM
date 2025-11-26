from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import art3d
import trimesh
import numpy as np

class Viewer3DWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.figure = Figure(figsize=(5, 5), dpi=100, facecolor='#2b2b2b')
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.configure_axes()

    def configure_axes(self):
        self.ax.set_facecolor('#2b2b2b')
        self.ax.grid(False)
        self.ax.set_axis_off() # Ocultar ejes para limpieza
        # Ajustar límites iniciales
        self.ax.set_xlim(-100, 100)
        self.ax.set_ylim(-100, 100)
        self.ax.set_zlim(0, 200)

    def load_model(self, file_path):
        """Carga y renderiza un archivo STL."""
        self.ax.clear()
        self.configure_axes()
        
        try:
            mesh = trimesh.load(file_path)
            
            # Si es una escena, tomar la primera geometría
            if isinstance(mesh, trimesh.Scene):
                if len(mesh.geometry) > 0:
                    mesh = list(mesh.geometry.values())[0]
                else:
                    return

            # Simplificar malla si es muy densa para rendimiento en matplotlib
            if len(mesh.faces) > 5000:
                mesh = mesh.simplify_quadratic_decimation(5000)

            # Obtener vértices y caras
            vertices = mesh.vertices
            faces = mesh.faces

            # Crear colección de polígonos
            poly3d = art3d.Poly3DCollection(vertices[faces], alpha=0.8)
            poly3d.set_facecolor('#0d6efd')
            poly3d.set_edgecolor('#0a58ca')
            poly3d.set_linewidth(0.1)

            self.ax.add_collection3d(poly3d)

            # Auto-escalado
            scale = vertices.flatten()
            self.ax.auto_scale_xyz(scale, scale, scale)
            
            self.canvas.draw()
            
        except Exception as e:
            print(f"Error al cargar modelo: {e}")
            self.ax.text(0, 0, 0, "Error al cargar", color='red')
            self.canvas.draw()
