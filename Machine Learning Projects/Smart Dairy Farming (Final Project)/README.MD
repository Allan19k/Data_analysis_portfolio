# Detección de Producción de Leche en Vacas con YOLOv11

Este proyecto fue desarrollado durante el 7º semestre de la carrera como parte de la materia de *Machine Learning*, bajo la guía de la Dra. Graciela Ramírez. El objetivo fue aplicar modelos de visión por computadora para estimar el nivel de producción de leche de vacas a partir de imágenes.

## 📊 Descripción
Se entrenó un modelo de detección usando **YOLOv11**, una versión avanzada de la familia YOLO, la cual destaca por su velocidad y precisión. El modelo fue entrenado para clasificar vacas en tres categorías según su producción de leche:

- `low_yield` ⬌ menos de 5,000 ml
- `medium_yield` ⬌ entre 5,001 y 9,000 ml
- `high_yield` ⬌ más de 9,000 ml

## 📆 Flujo del Proyecto
1. Recolección y limpieza de datos
2. Clasificación de imágenes según niveles de producción
3. Entrenamiento de modelo YOLOv11 con etiquetado personalizado
4. Exportación del modelo en formato `.pt` y despliegue para inferencia en móvil usando Ultralytics Hub

## 🧵 Motivación
El proyecto tiene un fuerte vínculo personal, ya que el autor proviene de una familia ganadera del estado de Chihuahua. Este trabajo representa un esfuerzo por combinar la tecnología con la ganadería tradicional para mejorar los procesos de producción mediante el uso de IA.

## 🎓 Tecnologías Usadas
- Python 3.11
- Ultralytics YOLOv11
- Roboflow
- Pandas, NumPy, Matplotlib
- Jupyter Notebook / Google Colab

## 📑 Resultado
El proyecto fue aceptado y publicado como artículo científico, demostrando el potencial de la visión por computadora en contextos agrícolas y ganaderos.

## ✨ Reconocimientos
Agradecimiento especial a la Dra. Graciela Ramírez por su acompañamiento y orientación durante todo el proyecto.

---

> “Aplicar la inteligencia artificial al campo no solo es posible, es necesario. Este proyecto es una muestra de que la tecnología puede tener un impacto real donde más se necesita.”


---

#machinelearning #yolov11 #computervision #ultralytics #ganaderiainteligente #ia
