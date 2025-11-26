import os
import shutil
import trimesh
from src.database.db_manager import DBManager

class LibraryManager:
    def __init__(self, db_manager=None):
        self.db = db_manager or DBManager()
        self.library_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'assets', 'models')
        
        if not os.path.exists(self.library_path):
            os.makedirs(self.library_path)

    def add_model(self, file_path, name, description=""):
        """Importa un archivo STL a la biblioteca y lo registra en la BD."""
        if not os.path.exists(file_path):
            return False, "El archivo no existe."

        filename = os.path.basename(file_path)
        dest_path = os.path.join(self.library_path, filename)
        
        # Copiar archivo a la carpeta de la biblioteca
        try:
            shutil.copy2(file_path, dest_path)
        except Exception as e:
            return False, f"Error al copiar archivo: {e}"

        # Generar miniatura (Placeholder por ahora)
        thumbnail_path = "" 
        
        # Guardar en BD
        query = """
            INSERT INTO models (name, description, file_path, thumbnail_path)
            VALUES (?, ?, ?, ?)
        """
        params = (name, description, dest_path, thumbnail_path)
        
        if self.db.execute_query(query, params):
            return True, "Modelo añadido correctamente."
        else:
            return False, "Error al guardar en base de datos."

    def get_all_models(self):
        """Obtiene todos los modelos de la BD."""
        query = "SELECT * FROM models ORDER BY added_date DESC"
        return self.db.fetch_query(query)

    def delete_model(self, model_id):
        """Elimina un modelo de la BD y del sistema de archivos."""
        # Primero obtener la ruta
        query_get = "SELECT file_path FROM models WHERE id = ?"
        result = self.db.fetch_query(query_get, (model_id,))
        
        if result:
            file_path = result[0]['file_path']
            # Borrar archivo físico
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except OSError:
                    pass # Continuar aunque falle borrado físico
            
            # Borrar de BD
            query_del = "DELETE FROM models WHERE id = ?"
            self.db.execute_query(query_del, (model_id,))
            return True
        return False
