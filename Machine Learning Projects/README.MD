# 🤖 Machine Learning

Este repositorio reúne varios proyectos desarrollados en la materia de Machine Learning que lleve en 7º semestre. 
Cada uno aborda distintos enfoques y técnicas de aprendizaje supervisado, redes neuronales, optimización de modelos y procesamiento de datos, aplicados en contextos reales y datasets clásicos.

El objetivo de esta sección es demostrar el dominio de distintas fases del desarrollo de modelos de Machine Learning: desde la preparación de datos hasta la evaluación y optimización del rendimiento.

---

## 📁 Contenido de proyectos

### 📐 1. Repaso de Álgebra para Redes Neuronales

Cuaderno didáctico con ejercicios de álgebra lineal orientados a redes neuronales y computación matricial. Está enfocado en reforzar los conocimientos matemáticos esenciales para Machine Learning, utilizando la biblioteca NumPy 🧮.
Antes de entrenar modelos, es clave dominar el manejo de vectores, matrices y operaciones lineales, ya que son la base de muchos algoritmos

📂 [`/Repaso_de_Algebra`](./Repaso_de_Algebra)

---

### 🔍 2. Búsqueda de Hiperparámetros con GridSearchCV

Optimización de un clasificador (`MLPClassifier`) utilizando `GridSearchCV` sobre el dataset `load_wine`. Se evaluaron distintas combinaciones de hiperparámetros (número de neuronas, funciones de activación, optimizadores) para encontrar la mejor configuración con validación cruzada.

📂 [`/Busqueda_de_Hiperparametros`](./Busqueda_de_Hiperparametros)

---

### 📊 3. Predicción de Tasas de Cambio EUR/USD con RNN y LSTM

Se implementaron modelos de redes neuronales recurrentes (RNN y LSTM) para predecir series temporales de tipo de cambio entre el euro y el dólar. Se compararon ambas arquitecturas usando métricas como MAE, MSE y RMSE para evaluar la efectividad del modelado.

📂 [`/Forecasting_Exchange_Rates_using_RNN_and_LSTM`](./Forecasting_Exchange_Rates_using_RNN_and_LSTM)

---

### 🧠 4. Clasificación de Imágenes con Transfer Learning (ResNet50)

Modelo de clasificación de imágenes de herramientas utilizando transferencia de aprendizaje con ResNet50. Se aplicaron técnicas de congelamiento de capas, ajuste fino del clasificador, uso de dropout, `class_weights` y data augmentation agresivo para mejorar el rendimiento sobre un conjunto de datos de Kaggle.

📂 [`/Transfer_Learning_&_CNN`](./Transfer_Learning_&_CNN)

---

### 📱 5. Proyecto Final (Smart Dairy Farming: A mobile application for Milk Yield Classification Tasks)

Proyecto final desarrollado en el curso de Machine Learning. Consiste en una aplicación móvil que utiliza un modelo de clasificación basado en visión por computadora para predecir niveles de producción de leche (alta, media o baja) a partir de imágenes. Este proyecto fue **publicado en una revista indexada en JCR** y se incluye el archivo PDF con la descripción completa del trabajo.  
  
Nota: Por cuestiones de tiempo y logística, **la parte de programación no fue documentada**, ya que el desarrollo se realizó en una computadora de la facultad.

📂 [`/Proyecto_Final`](./Machine Learning Projects/Smart Dairy Farming (Final Project))

---

## 🧠 Habilidades aplicadas

- Preprocesamiento y normalización de datos
- Construcción de modelos con scikit-learn y Keras/TensorFlow
- Transfer learning con arquitecturas CNN
- RNN y LSTM para series temporales
- Optimización con GridSearchCV
- Evaluación de modelos con métricas estadísticas y gráficas
- Interpretación de matrices de confusión y reportes de clasificación

---

## 📌 Herramientas utilizadas

- Python 3
- scikit-learn
- Keras / TensorFlow
- NumPy, Pandas, Matplotlib, Seaborn
- Jupyter Notebooks

---

## 📄 Licencia

Todos los proyectos incluidos en esta sección son de uso académico y libre distribución con fines educativos.
