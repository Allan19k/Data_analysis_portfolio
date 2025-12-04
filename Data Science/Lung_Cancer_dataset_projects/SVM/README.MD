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

## ⚙ Implementación de Modelos SVM

Se desarrollaron y evaluaron 3 modelos de SVM con kernels (Lineal, RBF y Polinomial):

📘 Evaluación

Se evaluaron:

    - Modelos sin ajustar

    - Modelos ajustados


✨ Métricas utilizadas:

    - Accuracy

    - Recall

    - Precision

    - F1-score

🔹 Modelo 1 – SVM Lineal

🔧 Hiperparámetros ajustados mediante GridSearch: 

- C


🔹 Modelo 2 – SVM RBF

Ideal para datos no lineales.

🔧 Hiperparámetros ajustados:

- C

- gamma

🔹 Modelo 3 – SVM Polinomial 

También apto para relaciones no lineales.

🔧 Hiperparámetros ajustados:

- C

- gamma

- degree

- coef0

---

## 📊 Resultados obtenidos

| Modelo SVM | Accuracy | Recall | Precision | F1-score |
|-------------------|-------------|----------|-----------|----------|
| **Lineal sin ajustar** | 0.9032 | 0.9444 | 0.9444 | 0.9444 |
| **Lineal con ajuste** | 0.9032 | 0.9444 | 0.9444 | 0.9444 |
| **RBF sin ajustar** | 0.8710 | 0.9630 | 0.8966 | 0.9286 |
| **RBF con ajuste** | 0.8710 | 0.9444 | 0.9107 | 0.9273 |
| **Polinomial sin ajustar** | 0.9032 | 0.9259 | 0.9615 | 0.9434 |
| **Polinomial con ajuste** | 0.8710 | 0.9444 | 0.9107 | 0.9273 |

---

## 🏆 Mejor modelo

El mejor modelo fue:

⭐ SVM Lineal Ajustado (C = 1)

Mantuvo el mejor Accuracy (0.9032) y métricas balanceadas entre Recall, Precision y F1-score.

Razones:

1. El dataset presenta relaciones lineales entre variables

2. Es menos sensible al ruido

3. Menor riesgo de sobreajuste que RBF o Polinomial

---

## 🧪 Matriz de Confusión

Se generó la matriz para cada modelo, permitiendo identificar:

- Casos correctamente clasificados

- Falsos positivos

- Falsos negativos (críticos en salud)

---

## 📚 Comparación de los resultados con otros modelos SVM encontrados en Kaggle 

Se compararon los resultados con 3 implementaciones previas en Kaggle de esa misma base de datos:

| Título/Autor | Hallazgos |
|-------------------|-------------|
| *Lung cancer and apply it on GUI* (Kamal Elfar) | <ul><li>Interfaz gráfica de usuario (GUI)</li><li>Uso de la libreria de python "Optuna" para la optimización de hiperparámetros |
| *Lung Cancer Prediction - EDA + SMOTE + MODELING* (Faiz) | <ul><li>El preprocesamiento de los datos: <ul><li> Convertir las columnas a minusculas</ul><li>Agregar guiones bajos para los nombres de las columnas con multiples palabras (columna_1) |
| *saved_models/* | Contiene el archivo del pipeline final. |





















