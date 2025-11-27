# Amazon Stock Price Predictor 🛒🛍️ 

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

    -  best_ridge_model.pkl (el modelo)
    -  preprocess_pipeline.pkl (el pipeline de preprocesamiento)
    -  y_scaler.pkl (el escalador y para la transformación inversa en Streamlit)

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

    - Random Forest Regressor

    - Gradient Boosting Regressor

    - AdaBoost Regressor

    - XGBoost Regressor

    - Voting Regressor

🔹 Redes Neuronales

    - MLP (MultiLayer Perceptron)

    - DNN (Deep Neural Network)

    - LSTM secuencial (Long Short Term Memory)

---

## 🧪 Búsqueda de Hiperparámetros

Se utilizó GridSearchCV por las siguientes razones:
1. **Optimización del Rendimiento**

    - Cada modelo de Machine Learning (como Regresión Ridge, Random Forest, SVR, MLP, etc.) tiene hiperparámetros que deben configurarse antes de entrenar. La elección correcta de estos valores es crucial para que el modelo alcance su máximo rendimiento predictivo y para evitar el sobreajuste o subajuste.

2. **Búsqueda Exhaustiva y Sistemática**

    - Grid Search explora de manera exhaustiva todas las combinaciones posibles de un conjunto predefinido de valores de hiperparámetros. Esto asegura que se evalúen diversas configuraciones y se encuentre la que produce el mejor desempeño (según una métrica específica como el Error Cuadrático Medio o R-squared).

3. **Evaluación Robusta con Validación Cruzada**

    - Grid Search entrena y evalúa el modelo para cada combinación de hiperparámetros utilizando validación cruzada. Esto proporciona una estimación más robusta del rendimiento del modelo en datos no vistos, ayudando a seleccionar el modelo que mejor generaliza.

---

## 🏆 Resultados y Modelo Ganador

El mejor modelo fue:

🥇 Ridge Regression

Con:

    - R² = 0.99 aprox. (casi 1)

    - RMSE = 0.04314 aprox. 

    - MAE = 0.02887 aprox. 

→ Fue seleccionado para despliegue final.

---

## 🚀 Implementación con Streamlit

Se desarrolló una aplicación interactiva usando la libreria de Python "Streamlit" en:

📄 AmazonStockPricePredictor.py  ✔ 

La app:

    - Carga best_ridge_model.pkl

    - Carga preprocess_pipeline.pkl

    - Carga y_scaler.pkl

    - Permite ingresar valores actuales + lags

    - Predice el Adj Close del siguiente día

🖼 Pantalla principal de Streamlit

Incluye:

    - Entradas para Open/High/Low/Close/Volume

    - Entradas para lags

    - Botón Predecir

    - Resultado con formato y animación (st.balloons())

▶ Para ejecutar localmente:

streamlit run AmazonStockPricePredictor.py'

> [!NOTE]
> Para ejecutar localmente en CMD usa el siguiente comando: streamlit run (ruta del archivo) + AmazonStockPricePredictor.py

Asegúrate de tener:

    saved_models/
    
    - best_ridge_model.pkl
    - preprocess_pipeline.pkl
    - y_scaler.pkl


---

## 🧠 Conclusiones

- El dataset de Amazon permite capturar de forma clara tendencias financieras.

- Los modelos basados en regresión penalizada (Ridge) superaron a modelos más complejos.

- Incluir lags fue crucial para mejorar la precisión.

- La combinación Pipeline + RandomizedSearchCV + Streamlit permitió crear un proyecto completo y profesional.

- El predictor funciona de manera estable y puede expandirse con:

    - Modelos secuenciales avanzados (GRU, LSTM mejor diseñadas)

    - Feature engineering más agresivo

    - Validación temporal TimeSeriesSplit

    - Actualización automática con nuevas cotizaciones

---

## 🏁 Librerias utilizadas


        - Pandas / NumPy

        - Matplotlib / Seaborn

        - Scikit-Learn

        - TensorFlow/Keras

        - Streamlit

        - Joblib

---












