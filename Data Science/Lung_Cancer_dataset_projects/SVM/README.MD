# 🧠 SVM Classifier – Lung Cancer Dataset

Este proyecto implementa y compara tres modelos de Máquinas de Vectores de Soporte (SVM) para predecir cáncer de pulmón usando el Lung Cancer Dataset de Kaggle. El objetivo es evaluar el comportamiento de diferentes kernels (lineal, RBF y polinomial) y determinar cuál ofrece el mejor rendimiento utilizando métricas de clasificación y validación cruzada.

El flujo seguido es el estándar del proceso de Data Science:

1. Exploración inicial de datos

2. Partición Train/Test con revisión de estratificación

3. Preprocesamiento mediante Pipeline

4. Entrenamiento de SVM con tres kernels

5. Búsqueda de hiperparámetros (GridSearch/RandomSearch)

6. Evaluación con métricas de clasificación

7. Matriz de confusión

8. Comparación con artículos científicos previos

9. Conclusiones

---

## 📂 Dataset

- Fuente: Kaggle [Lung Cancer Dataset](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer.)

- Tarea: Clasificación binaria

- Objetivo: Identificar si un paciente presenta cáncer de pulmón

- Características: Variables clínicas (numéricas y categóricas)

---

## 🔍 Exploración inicial de los datos (EDA)

La exploración inlcuyo:

    - Identificación de valores nulos

    - Análisis de balance de clases
    
    - Histogramas y distribuciones

    - Matriz de correlación

En esta etapa NO se aplicaron transformaciones; solo análisis descriptivo.

---



