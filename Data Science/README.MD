#  🥼 Data Science

Este repositorio contiene todas las prácticas y el proyecto final realizadas en 8º semestre durante la materia optativa de Ciencia de Datos.

Cada subproyecto tiene su propia carpeta con notebooks (.ipynb), código fuente (.py) y archivos de resultados (gráficas, modelos guardados, app.py para Streamlit cuando aplica).

## 🔎 Contenido

### 🌎 Social Network Analysis 

Ejercicio introductorio de DS (del libro de Data Science from Scratch). Se trabajó con estructuras de datos en Python para responder preguntas sobre una pequeña red social ficticia: 
conteo de amigos, identificación de usuarios más conectados, intereses más frecuentes y relaciones entre nodos. 


📂 [/Social_Network_Analysis](./Social_Network_Analysis)

---

### 🕵️‍♂️ Web Scraping + Análisis de Herramientas Open Source

Seguimiento de un tutorial de YouTube para scraping en Python; se añadió una etapa de análisis que extrae menciones de herramientas Open Source para Data Science y las agrupa por categorías (data management, integration, visualization etc.). 
Se crearon gráficas que muestran la frecuencia de menciones por herramienta/categoría.

📂 [/Scrapping_Web](./Scrapping_Web)

---

### 🏡 California House Prices — End to End project 

Proyecto end-to-end inspirado en el repositorio hands-on-ml2 (Andreas Géron). Flujo completo: EDA, pipeline de preprocesamiento, entrenamiento de modelos (Linear Regression, Decision Tree, Random Forest), ajuste con RandomizedSearchCV, comparación por RMSE y despliegue local del mejor modelo con Streamlit (interfaz para hacer predicciones).

📂 [/End_to_end_project](./End_to_end_project)

---

### 🏎️ Regresión Lineal (car_price)

Predicción del precio de automóviles. Incluye: partición Train/Test, EDA, pipeline de preprocesamiento (imputación, codificación, escalado cuando aplica), baseline de regresión lineal, búsqueda de hiperparámetros, evaluación con RMSE y validación final en test.

📂 [/Linear_Regression](./Linear_Regression)

---

### 🚬 Lung Cancer Dataset Projects

Contiene varias prácticas realizadas durante el semestre de un dataset de Kaggle sobre el Cáncer de Pulmon. Se implementaron y compararon los siguientes modelos de ML

* **Logistic Regression (SGD)** Modelo Base y Modelo ajustado 
* **SVM** Lineal, RBF y Polinomial (sin ajuste y con ajuste) 
* **Random Forest** Sin escalar datos (sin ajuste y con ajuste) y con Escalado de datos (Sin Ajuste) 
* **Modelos de Ensamble** VotingClassifier, Bagging, Pasting, AdaBoost, GradientBoosting, XGBoost

📂 [/Lung_Cancer_dataset_projects](./Lung_Cancer_dataset_projects)

---

### 🏬 Proyecto Final: Amazon Stock Price Predictor

Sistema completo para predecir el precio de ciere ajustado (Adj Close) de Amazon usando datos históricos: EDA, creación de lags (features rezagadas), pipelines, comparación de modelos clásicos y redes (Ridge, SVR, RandomForest, Voting, AdaBoost, GradientBoosting, XGBoost, MLP, DNN, LSTM). 
Se seleccionó el mejor modelo según métricas (RMSE, MAE, MSE) y se desplegó localmente con Streamlit para predicción interactiva.

📂 [/Amazon_Predictor](./Amazon_Predictor)

---

## 🛠 Tecnologías y librerías utilizadas

  * Lenguaje: Python

  * Entornos: Google Colab

  * Manipulación & ML: pandas, numpy, scikit-learn, xgboost, joblib

  * Visualización: matplotlib, seaborn

  * Despliegue / UI: Streamlit

  * Extras: BeautifulSoup / requests (scraping)

---
