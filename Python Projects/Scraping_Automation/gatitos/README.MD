# 🐱 Descarga concurrente de imágenes con Python (Threading)

## 🎯 Objetivo
Desarrollar una aplicación en Python que utilice **hilos (`threading`)** para descargar imágenes desde la web de manera concurrente, reduciendo tiempos de espera y mostrando la utilidad del cómputo paralelo en tareas simples de automatización.

---

## 📝 Descripción
Este proyecto implementa una solución para descargar imágenes de gatos desde el sitio [placecats.com](https://www.placecats.com/).  
Cada imagen es descargada en un hilo independiente, lo que permite que varias descargas se realicen en paralelo.

Las imágenes se almacenan en una carpeta llamada `cats/`, con nombres asignados automáticamente (`gato_1.jpg`, `gato_2.jpg`, ...).

---

## 🔧 Funciones y herramientas utilizadas
- **`threading`**: permite crear un hilo por cada imagen a descargar.  
- **`requests`**: gestiona las solicitudes HTTP a la página web para obtener las imágenes.  
- **`os`**: creación de carpetas y manejo de rutas para guardar los archivos.  

---

## 📂 Archivos
- `app_gatitos.py`: código principal con la lógica de descarga.  
- `cats/`: carpeta donde se almacenan las imágenes descargadas.  
- `app para descargar imagenes.pdf`: documento explicando la práctica y mostrando ejemplos de las imágenes guardadas.  

---

## 🚀 Ejecución
1. Clona el repositorio o descarga el archivo `app_gatitos.py`.  
2. Instala la librería `requests` si no la tienes:  pip install requests
3. Ejecuta el programa: python app_gatitos.py
4. Al finalizar, revisa la carpeta cats/ para ver las imágenes descargadas.

## 📌 Resultados
- Descarga exitosa de múltiples imágenes en paralelo.
- Ejemplo práctico de cómo aplicar cómputo paralelo con hilos en Python.
- Proyecto base para extender hacia scraping de datos y análisis en otras fuentes web.



