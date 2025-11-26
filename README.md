# Gestor 3D

![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![Versión](https://img.shields.io/badge/Versión-0.1.0-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)

## 📋 Descripción
**Gestor 3D** es una aplicación de escritorio multiplataforma diseñada para entusiastas y profesionales de la impresión 3D. Permite gestionar proyectos, calcular costes de impresión, organizar una biblioteca de modelos con visualización 3D integrada, controlar el inventario de filamentos y acceder a un marketplace de diseños.

## 🎯 Objetivos del Proyecto
- **Gestión Integral**: Centralizar proyectos, materiales y costes en una sola aplicación
- **Calculadora de Costes**: Estimación precisa basada en material, energía y tiempo
- **Biblioteca 3D**: Organización visual de archivos STL con visor integrado
- **Inventario**: Control de stock de filamentos con registro detallado
- **Marketplace**: Plataforma de intercambio de modelos (simulado)

## ✨ Características

### 🧮 Calculadora de Costes
- Cálculo automático de coste de filamento
- Estimación de consumo energético
- Desglose detallado de gastos

### 📚 Biblioteca de Modelos
- Importación de archivos STL
- Visor 3D integrado (Matplotlib + Trimesh)
- Gestión de modelos (añadir/eliminar)

### 📦 Inventario de Filamentos
- Registro de rollos (marca, tipo, color, peso, precio)
- Tabla interactiva con búsqueda
- Control de stock restante

### 🛒 Marketplace
- Catálogo de modelos 3D
- Simulación de compra/descarga

## 🛠️ Tecnologías
- **Lenguaje**: Python 3.8+
- **Interfaz**: PyQt5
- **Base de Datos**: SQLite
- **Visualización 3D**: Trimesh + Matplotlib

## 📥 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip

### Pasos
```bash
# Clonar el repositorio
git clone https://github.com/KanjoLOOP/TFG_DAM.git
cd Gestor3D

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python src/main.py
```

## 📖 Documentación
- [Manual de Usuario](MANUAL_USUARIO.md) - Guía completa de uso
- [Documentación de Desarrollo](DESARROLLO.md) - Arquitectura y decisiones técnicas
- [Fundamentos Teóricos](DOCUMENTACION.md) - Objetivos y metodología

## 🗂️ Estructura del Proyecto
```
Gestor3D/
├── src/
│   ├── main.py              # Punto de entrada
│   ├── database/            # Esquema y gestor de BD
│   ├── logic/               # Lógica de negocio
│   └── ui/                  # Interfaces gráficas
├── assets/
│   ├── styles.qss           # Estilos
│   └── models/              # Biblioteca de STL
├── MANUAL_USUARIO.md
├── DESARROLLO.md
└── requirements.txt
```

## 🚀 Estado del Proyecto
**Versión Actual**: 0.1.0 (MVP)

### Completado ✅
- [x] Interfaz gráfica con navegación
- [x] Calculadora de costes funcional
- [x] Biblioteca con visor 3D
- [x] Inventario CRUD
- [x] Marketplace simulado

### Próximas Mejoras 🔜
- [ ] Autenticación de usuarios
- [ ] Exportación de informes PDF
- [ ] Integración con slicers (Cura, PrusaSlicer)
- [ ] Marketplace real con API
- [ ] Gráficos de estadísticas

## 👨‍💻 Autor
Desarrollado como Trabajo de Fin de Grado (TFG) - DAM

## 📄 Licencia
Este proyecto es de código abierto para fines educativos.
