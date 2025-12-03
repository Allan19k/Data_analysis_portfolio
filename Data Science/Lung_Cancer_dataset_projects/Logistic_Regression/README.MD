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

- Fuente: Kaggle [Lung Cancer Dataset](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer.)

- Tarea: Clasificación binaria

- Objetivo: Identificar si un paciente presenta cáncer de pulmón

- Características: Variables clínicas (numéricas y categóricas)

---

## 🔍 Exploración inicial de los datos (EDA)

La exploración inicial incluyó:

✔ Identificación de valores nulos

  - Se analizó columna por columna para detectar datos faltantes.

  - No se realizaron modificaciones en esta etapa, solo detección.

✔ Distribución de características

  - Se visualizaron histogramas/plots para:

  - Distribución de cada variable clínica

 - Observación de posibles outliers

 - Detección de desbalanceo en la variable objetivo

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

  - Distribución de la variable objetivo (clases)

  - Existencia de desbalance

Para problemas de clasificación es casi obligatoria realizar la partición estratificada, por lo tanto, si se realizo la partición estratificada

---

## 🛠 Preprocesamiento con Pipeline

Una vez analizadas las deficiencias del dataset, se creó un Pipeline que manejó:

✔ Imputación de valores nulos

Para columnas numéricas y categóricas.

✔ Codificación de variables no numéricas

En caso de existir.

✔ Normalización / Escalado

Uso de StandardScaler, crucial para modelos basados en gradiente.

✔ Integración completa

El Pipeline se entrenó solo con Train para evitar data leakage.


---

## 🤖 Implementación del modelo (SGDClassifier)

Se implementaron dos versiones del modelo:

🔹 a) Modelo sin ajustar (SGD base)

    - Se entrenó con parámetros por defecto.

    - Se aplicó Cross Validation de 10 particiones para evaluar rendimiento inicial.

    - Se calcularon métricas preliminares.

🔹 b) Modelo ajustado (SGD + GridSearch/RandomSearch)

Se buscaron hiperparámetros como:

    - loss

    - penalty

    - alpha

    - max_iter

    - learning_rate

    - eta0

Se ejecutó: RandomizedSearchCV con 10-fold Cross Validation

El mejor modelo fue seleccionado automáticamente.


---

## 🧪 Evaluación del mejor modelo

Se evaluó el modelo ajustado utilizando el conjunto de Test, obteniendo:

✔ Accuracy

✔ Precision

✔ Recall

✔ F1-score

✔ Matriz de confusión

Estas métricas permiten analizar:

    - Casos correctamente detectados

    - Falsos positivos

    - Falsos negativos (críticos en tareas médicas)

--- 

## 📊 Matriz de confusión

La matriz muestra el desempeño detallado del clasificador.
Ayuda a evaluar si el modelo tiende a:

Clasificar falsamente pacientes con cáncer

O fallar en detectar casos reales
(muy importante en medicina)

## 🧠 Conclusiones 

En esta práctica, la Regresión Logística mediante SGDClassifier demostró ser un modelo eficiente para la tarea de clasificación binaria del dataset de cáncer de pulmón. La aplicación de un Pipeline permitió un preprocesamiento limpio y reproducible, y el ajuste de hiperparámetros mejoró significativamente las métricas respecto al modelo base.

El análisis mostró que el modelo ajustado mejora en términos de precisión y recall, reduciendo errores críticos en la clasificación médica. Sin embargo, se pueden explorar modelos adicionales como SVM, Random Forest y ensamblados para comparar rendimiento.

## 🚀 Librerias utilizadas

- Python

- Pandas

- NumPy

- Scikit-learn

- Matplotlib / Seaborn

---

## 🧾 Autor

Allan Hall Solorio
Estudiante de Ingeniería en Ciencias de la Computación
Enfoque en Análisis de Datos y Machine Learning

---
