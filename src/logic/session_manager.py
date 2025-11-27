import json
import os

class SessionManager:
    """Gestor de sesión para recordar credenciales."""
    
    SESSION_FILE = "session.json"
    
    @staticmethod
    def save_session(username, password):
        """Guarda las credenciales en un archivo JSON."""
        data = {
            "username": username,
            "password": password
        }
        try:
            with open(SessionManager.SESSION_FILE, 'w') as f:
                json.dump(data, f)
            return True
        except Exception as e:
            print(f"Error guardando sesión: {e}")
            return False
            
    @staticmethod
    def load_session():
        """Carga las credenciales guardadas."""
        if not os.path.exists(SessionManager.SESSION_FILE):
            return None, None
            
        try:
            with open(SessionManager.SESSION_FILE, 'r') as f:
                data = json.load(f)
                return data.get("username"), data.get("password")
        except Exception as e:
            print(f"Error cargando sesión: {e}")
            return None, None
            
    @staticmethod
    def clear_session():
        """Borra el archivo de sesión."""
        if os.path.exists(SessionManager.SESSION_FILE):
            try:
                os.remove(SessionManager.SESSION_FILE)
                return True
            except Exception as e:
                print(f"Error borrando sesión: {e}")
                return False
        return True
