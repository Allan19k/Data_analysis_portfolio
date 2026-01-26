# 🏡 Intro to Machine Learning – Kaggle Course Projects

Este repositorio documenta los ejercicios y prácticas realizadas durante el curso **Intro to Machine Learning** de **Kaggle**, utilizando el dataset **Home Data for ML Course**, enfocado en la predicción del precio de viviendas en Iowa, Estados Unidos.

El objetivo principal fue comprender los fundamentos del aprendizaje automático supervisado, desde la exploración de datos hasta la implementación y validación de modelos de regresión.

---

## 📊 Dataset

- **Nombre:** Home Data for ML Course  
- **Fuente:** Kaggle  
- **Problema:** Regresión (predicción de precios de casas)  
- **Variable objetivo:** `SalePrice`  

El dataset contiene características relacionadas con propiedades residenciales, como número de habitaciones, área habitable, año de construcción, calidad general, entre otras.

---

## 📘 Contenido del Curso y Prácticas

### 1️⃣ How Models Work
**Tipo:** Tutorial teórico  
Introducción conceptual al funcionamiento de los modelos de Machine Learning explicando:
- Como funcionan los modelos de ML y un ejemplo simple 
- ¿Que son los árboles de decisión?

> En esta lección no se realizó implementación práctica de código.

---

### 2️⃣ Basic Data Exploration
**Objetivo:** Comprender y explorar el dataset  

Actividades realizadas:
- Carga del dataset con `pandas`
- Análisis estadístico básico (`describe`)
- Solución de 2 preguntas con la información obtenida

  * What is the average lot size (rounded to nearest integer)?
  avg_lot_size = 10517

  * As of today, how old is the newest home (current year - the date in which it was built)
  newest_home_age = 15

Esta etapa permitió entender la estructura del conjunto de datos antes de aplicar modelos.

---

### 3️⃣ Your First Machine Learning Model
**Modelo implementado:** `DecisionTreeRegressor`  

Actividades:
- Selección de características predictoras
- Separación de variables independientes (`X`) y variable objetivo (`y`)
- Entrenamiento de un modelo de Árbol de Decisión
- Generación de predicciones iniciales  

Este ejercicio representó el primer acercamiento práctico al entrenamiento de modelos de Machine Learning.

---

### 4️⃣ Model Validation
**Objetivo:** Evaluar el rendimiento del modelo  

- Se utilizó la métrica **MAE (Mean Absolute Error)** para evaluar el desempeño
- Se realizó una partición **Train / Validation**
- Se compararon predicciones contra valores reales  

📉 **Resultado obtenido:**
- **MAE:** `29652.93`

Este resultado permitió identificar que el modelo inicial podía mejorarse.

---

### 5️⃣ Underfitting and Overfitting
**Objetivo:** Ajustar el modelo para mejorar su desempeño  

Actividades:
- Comparación de Árboles de Decisión con distintos valores de `max_leaf_nodes`
- Identificación del tamaño óptimo del árbol
- Reentrenamiento del modelo usando el mejor parámetro encontrado  

Este ejercicio reforzó conceptos clave como:
- Underfitting
- Overfitting
- Selección adecuada de hiperparámetros

---

### 6️⃣ Random Forests
**Modelo implementado:** `RandomForestRegressor`  

Actividades:
- Implementación de un modelo de ensamble más robusto
- Comparación de desempeño frente al Árbol de Decisión
- Validación del modelo usando MAE  

📉 **Resultado obtenido:**
- **MAE:** `21857.16`

Este modelo logró una mejora significativa en el error, demostrando la ventaja de los métodos de ensamble frente a modelos simples.

---

## 🧠 Conclusiones

El curso permitió comprender el flujo básico de un proyecto de Machine Learning:
  - Exploración de datos
  - Entrenamiento de modelos
  - Validación y comparación
- Se evidenció cómo el ajuste de hiperparámetros impacta directamente en el desempeño
- Los modelos de **Random Forest** mostraron un mejor balance entre sesgo y varianza
- Esta práctica sirvió como base para proyectos más avanzados de **Data Science y Machine Learning**

---

## 🛠️ Herramientas Utilizadas

- Python
- Pandas
- Scikit-learn
- Jupyter Notebook / Kaggle Notebooks

---

## 📌 Autor

**Allan Hall**  
Estudiante de Ingeniería en Ciencias de la Computación  
Enfoque en Análisis de Datos y Machine Learning  
