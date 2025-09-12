# 🚗💲 Práctica – Regresión Lineal (Car Price Prediction) Examen Primer Parcial 

**Dataset:** `car_price` (Kaggle) 

Fuente: https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge

---

## 🎯 Objetivo

Desarrollar un modelo de **Regresión Lineal** para predecir el precio de automóviles a partir del dataset `car_price`. 
El ejercicio incluye: partición Train/Test, exploración de datos, creación de un pipeline de preprocesamiento, entrenamiento de un modelo baseline, búsqueda de hiperparámetros (GridSearch / RandomSearch), evaluación mediante RMSE y validación final en el conjunto de test.

---

## Estructura del trabajo

1. 🗂️ **Obtención de los datos**  
   - Para obtener la base de datos directamente desde Kaggle, se siguieron los siguientes pasos:
      - Instalación de la librería de Kaggle: Se instaló la librería kaggle usando pip, que es la herramienta oficial para interactuar            con la API de Kaggle desde Python. Esto permite ejecutar comandos de Kaggle directamente en el entorno.
      - Configuración de la API de Kaggle: Para que la librería de Kaggle pueda autenticarse y descargar datasets, se necesita un archivo kaggle.json. Este archivo contiene las credenciales de la cuenta de Kaggle. El proceso implica:

         1.  Crear un directorio .kaggle en el directorio principal del usuario (~/.kaggle).
         2.  Copiar el archivo kaggle.json (que previamente se descargó desde la configuración de la cuenta de Kaggle) a este nuevo    directorio.
         3.  Cambiar los permisos del archivo kaggle.json para asegurarse de que solo el propietario pueda leer y escribir en él (chmod 600 ~/.kaggle/kaggle.json). Esto es crucial por razones de seguridad para proteger las credenciales.
      - Descarga del Dataset: Una vez configurada la autenticación, se utilizó el comando kaggle datasets download para descargar el dataset específico (deepcontractor/car-price-prediction-challenge). Se especificó el directorio de destino (-p /content/dataset) donde se guardaría el archivo zip descargado y se añadió la opción --unzip para descomprimir automáticamente el archivo después de la descarga.

2. 🗃️ **Partición Train / Test**  
   - Se dividió el dataset en **80% Train** y **20% Test**, manteniendo el conjunto de test intacto hasta la evaluación final.

3. 🤓 **Exploración de la base de datos (EDA)**
    - Análisis inicial para comprender la estructura de los datos, identificar posibles problemas (como valores faltantes o inconsistencias) y visualizar distribuciones de características clave.

4. 🤔 **Preprocesamiento y Pipeline**
    - Limpieza y transformación de los datos, incluyendo el manejo de valores inconsistentes, la codificación de variables categóricas y el escalado de características numéricas para preparar los datos para los modelos de Machine Learning.

5.📉 **Implementación de modelo de Regresión Lineal** 
      - Entrenamiento y evaluación de un modelo de Regresión Lineal simple utilizando validación cruzada.

6. 📈 **Implementación y optimización de modelo Ridge** 
   - Implementación de un modelo de Regresión Ridge y uso de Grid Search para encontrar los mejores hiperparámetros, evaluando su rendimiento también con validación cruzada.

7. 💯 **Evaluación del modelo final**
   - Evaluación del mejor modelo obtenido en el conjunto de prueba no visto para obtener métricas finales de rendimiento.

8. 📋 **Conclusiones**
   - Se describen los hallazgos encontrados: si la regularización mejoró el rendimiento  y recomendaciones para pasos siguientes (más datos, ingeniería de features, modelos no lineales, etc.). 

## 🚀 Conclusiones y recomendaciones 

1. La regresión lineal sirve como baseline sólido para entender relaciones entre características y el precio.

2. La búsqueda de hiperparámetros mejoró la generalización frente al modelo sin ajuste.

3. La calidad del preprocesamiento (imputación y escalado) impactó claramente en el rendimiento final.

4. Para mejorar el modelo seria necesario experimentar con modelos no lineales como Random Forest o XGBoost









