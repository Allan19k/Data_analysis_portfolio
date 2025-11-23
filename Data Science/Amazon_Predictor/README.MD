# 📈 Proyecto Final: Amazon Stock Price Predictor — End-to-End Data Science Project 

Este proyecto desarrolla un sistema completo de Machine Learning para predecir el precio de cierre ajustado (Adj Close) de las acciones de Amazon, utilizando información histórica del mercado y técnicas modernas de ciencia de datos.
Incluye EDA, comparación de modelos, tuneo de hiperparámetros y despliegue local con Streamlit.

---

## 📌 Objetivo del Proyecto

Construir, entrenar, comparar y desplegar modelos de Machine Learning capaces de predecir el valor Adj Close de Amazon para el siguiente día, utilizando:

- Datos históricos: Open, High, Low, Close, Volume.

- Dependencias temporales mediante lags (1, 2 y 3 días previos).

- Modelos clásicos, ensambles y redes neuronales.

- Despliegue local mediante una aplicación interactiva en Streamlit.

Este predictor puede apoyar decisiones financieras, análisis de tendencias y evaluación de riesgo.

---

## 📂 Contenido del Proyecto

- Amazon_Stock_Price_Predictor.ipynb — Notebook completo del proyecto (EDA → Modelos → Resultados).

- AmazonStockPricePredictor.py — Aplicación local en Streamlit. 

- saved_models/ — Contiene:

    -  best_ridge_model.pkl
    -  preprocess_pipeline.pkl
    -  y_scaler.pkl

---

## 🗂 Obtención del Dataset

El dataset proviene de Kaggle:

📎 Amazon Stock Price All-Time
https://www.kaggle.com/datasets/kannan1314/amazon-stock-price-all-time

Incluye datos desde 1997 hasta octubre de 2021:

- Open

- High

- Low

- Close

- Adj Close

- Volume

--- 

## 🔍 Exploración Inicial (EDA)

El análisis incluyó:

✔ Distribuciones de las variables financieras

Histogramas / KDE para visualizar rangos y tendencias.

✔ Correlaciones

    - Se construyó una matriz de correlación para identificar relaciones entre variables.

    - Adj Close correlacionado fuertemente con Close, High, Low → esperado.

✔ Detección de valores nulos

El dataset no presentó valores faltantes, lo que facilitó el preprocesamiento.

✔ Visualizaciones clave

    - Línea de tiempo del precio Adj Close.

    - Volumen negociado a lo largo del tiempo.

    - Comparación entre precios diarios (Open/High/Low/Close).

    - Gráfico OHLC para análisis financiero tradicional.

---

## 🔧 Ingeniería de Características

🔹 Creación de Variables Rezagadas (Lags)

Las series de tiempo requieren capturar dependencia temporal:

- Adj Close_Lag1 (1 día previo)

- Adj Close_Lag2 (2 días previos)

- Adj Close_Lag3 (3 días previos)

Esto convierte el problema en un dataset adecuado para modelos supervisados clásicos y redes neuronales.

🔹 Estandarización y Preprocesamiento

Se implementó un Pipeline que incluye:

    - Estandarización de variables (StandardScaler)

    - Ensamblaje final de features

    - Aplicación solo al conjunto de entrenamiento para evitar fugas de información (data leakage)


🔹 Escalado de la variable objetivo (solo para redes neuronales)

Los modelos MLP/DNN/LSTM requieren escalar y → se usó StandardScaler.


---

## 🔀 División del Dataset (Train/Test)

Debido a que es una serie de tiempo, se respetó el orden temporal:

Train: ~80% inicial

Test: ~20% final


Después de generar los lags, el DataFrame cambió su tamaño, por lo que se volvió a dividir y escalar.

---

## 🤖 Modelos Implementados

Todos fueron evaluados con:

- RMSE

- MAE

- MSE

- R² Score

🔹 Modelos Lineales

Ridge Regression ✔ → Mejor modelo del proyecto


🔹 Máquinas de Soporte Vectorial

SVR (linear kernel)


🔹 Árboles & Ensambles

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor

AdaBoost Regressor

XGBoost Regressor

Voting Regressor

🔹 Redes Neuronales

MLP Regressor

DNN personalizada

LSTM (modelo secuencial)

---

## 🧪 Búsqueda de Hiperparámetros

Se utilizó GridSearchCV para explorar espacios 









