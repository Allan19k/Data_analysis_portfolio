# 🧬 Logistic Regression Classifier – Lung Cancer Dataset

Este proyecto implementa y evalúa un modelo de Regresión Logística (usando SGDClassifier) para predecir la presencia de cáncer de pulmón 
utilizando el dataset de Lung Cancer disponible en Kaggle.

---

##  📌 Objetivo del proyecto 

Se sigue el flujo completo de un proyecto de Machine Learning supervisado, integrando:

- Exploración y comprensión del dataset

- Análisis de correlación

- Partición Train/Test

- Preprocesamiento mediante Pipeline

- Entrenamiento con SGDClassifier

- Validación cruzada

- Búsqueda de hiperparámetros (GridSearch/RandomSearch)

- Evaluación final del modelo

Este repositorio forma parte de la carpeta de proyectos Lung_Cancer_Dataset_Projects, donde se comparan diversos modelos.

---

## 📂 Dataset

- Fuente: Kaggle — Lung Cancer Dataset

- Tarea: Clasificación binaria

- Objetivo: Identificar si un paciente presenta cáncer de pulmón

- Características: Variables clínicas (numéricas y categóricas)

---

## 🔍 Exploración inicial de los datos (EDA)

La exploración inicial incluyó:

✔ Identificación de valores nulos

Se analizó columna por columna para detectar datos faltantes.

No se realizaron modificaciones en esta etapa, solo detección.

✔ Distribución de características

Se visualizaron histogramas/plots para:

Distribución de cada variable clínica

Observación de posibles outliers

Detección de desbalanceo en la variable objetivo

✔ Correlación

Se generó una:

Matriz de correlación

Mapa de calor (Heatmap)


Esto permitió identificar qué variables tienen mayor relación con el diagnóstico final.

---

## ✂ Partición Train/Test

Se dividió el dataset en:

* 80% Entrenamiento

* 20% Prueba


Se evaluó si se requería una partición estratificada, revisando:

Distribución de la variable objetivo (clases)

Existencia de desbalance












