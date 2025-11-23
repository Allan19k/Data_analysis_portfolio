# 📈 Amazon Stock Price Predictor — End-to-End Data Science Project 

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
    - preprocess_pipeline.pkl
    - y_scaler.pkl



