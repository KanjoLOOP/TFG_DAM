# Manual de Usuario - Gestor 3D

## Índice
1. [Instalación](#instalación)
2. [Inicio de la Aplicación](#inicio-de-la-aplicación)
3. [Módulos](#módulos)
4. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/KanjoLOOP/TFG_DAM.git
   cd Gestor3D
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Inicializar la base de datos** (opcional, se hace automáticamente)
   ```bash
   python init_db_script.py
   ```

---

## Inicio de la Aplicación

Ejecutar desde la raíz del proyecto:
```bash
python src/main.py
```

La aplicación se abrirá en una ventana con un menú lateral de navegación.

---

## Módulos

### 1. Inicio (Dashboard)
Pantalla de bienvenida con información general.

### 2. Calculadora de Costes

**Objetivo**: Estimar el coste total de una impresión 3D.

**Cómo usar**:
1. Introducir el **peso del modelo** en gramos (ej: 150g)
2. Introducir el **precio del filamento** por kilogramo (ej: 20€/kg)
3. Introducir el **tiempo de impresión** en horas (ej: 5.5h)
4. Ajustar el **consumo de la impresora** en Watts (por defecto: 350W)
5. Ajustar el **coste de la energía** (por defecto: 0.15€/kWh)
6. Hacer clic en **"Calcular Coste Total"**

**Resultado**: Se mostrará el desglose de costes (filamento + energía) y el total.

---

### 3. Biblioteca de Modelos 3D

**Objetivo**: Organizar y visualizar archivos STL.

**Cómo usar**:
1. Hacer clic en **"Añadir Modelo"**
2. Seleccionar un archivo `.stl` desde tu ordenador
3. El modelo se copiará a la biblioteca y aparecerá en la lista
4. **Hacer clic en un modelo** de la lista para visualizarlo en 3D
5. Para eliminar: seleccionar modelo y hacer clic en **"Eliminar"**

**Visor 3D**: 
- Rotación automática al cargar
- Zoom y pan disponibles (controles de Matplotlib)

---

### 4. Inventario de Filamentos

**Objetivo**: Controlar el stock de materiales.

**Cómo usar**:

#### Añadir Filamento
1. Rellenar el formulario superior:
   - **Marca**: Fabricante (ej: Prusament, eSun)
   - **Tipo**: Material (PLA, PETG, ABS, etc.)
   - **Color**: Color del filamento
   - **Peso**: Peso inicial en gramos (ej: 1000g)
   - **Precio**: Coste del rollo en euros
2. Hacer clic en **"Añadir"**

#### Eliminar Filamento
1. Seleccionar una fila de la tabla
2. Hacer clic en **"Eliminar Seleccionado"**

---

### 5. Marketplace

**Objetivo**: Explorar modelos 3D disponibles (simulado).

**Cómo usar**:
1. Navegar por las tarjetas de modelos
2. Hacer clic en **"Obtener"** o **"Comprar"**
3. Aparecerá un mensaje de confirmación (simulación)

> **Nota**: En esta versión, el marketplace es una demostración. Los modelos no se descargan realmente.

---

## Preguntas Frecuentes

### ¿Dónde se guardan los archivos STL?
En la carpeta `assets/models/` dentro del proyecto.

### ¿Puedo usar la aplicación sin conexión a Internet?
Sí, la aplicación funciona completamente offline (excepto el marketplace simulado).

### ¿Cómo actualizo el peso restante de un filamento?
Actualmente, el peso se actualiza manualmente. En futuras versiones se integrará con proyectos para restar automáticamente.

### ¿Qué formatos de archivo 3D soporta?
Actualmente solo archivos `.stl` (estándar en impresión 3D).

### La aplicación no inicia, ¿qué hago?
1. Verificar que todas las dependencias estén instaladas: `pip install -r requirements.txt`
2. Comprobar la versión de Python: `python --version` (debe ser 3.8+)
3. Revisar errores en la terminal

---

## Soporte
Para reportar errores o sugerencias, abrir un issue en el repositorio de GitHub:
https://github.com/KanjoLOOP/TFG_DAM/issues
