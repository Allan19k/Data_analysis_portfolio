# 🌁 End-to-End: California Housing Price Prediction

**Resumen**  
Proyecto end-to-end para predecir el valor medio de viviendas en California usando el dataset del repositorio *hands-on-ml2* (Andreas Geron). 
Se entrenaron tres modelos (Regresión Lineal, Decision Tree y Random Forest), se regularizaron con **RandomizedSearchCV**, se compararon por RMSE y se exportó el mejor modelo junto con el pipeline completo para servirlo localmente mediante **Streamlit**.

---

## 📁 Archivos principales
- `End_to_end_project.ipynb` — Notebook con todo el flujo (EDA, pipelines, entrenamiento y evaluación).
- `app.py` — App Streamlit para cargar el modelo/pipeline y realizar predicciones locales.


---

## 🧭 Flujo seguido (resumen)
1. **Get data**  
   Descarga del CSV: `datasets/housing/housing.csv` desde el repo de *hands-on-ml2*.

2. **Discover & visualize**  
   - Análisis exploratorio (valores N/A, histogramas, boxplots, correlaciones).
   - Conversión de `ocean_proximity` a categórica y tratamiento de NA (ej. `.median()` o `SimpleImputer`).

3. **Prepare data for ML**  
   - Pipeline con steps: imputación, codificación (OneHotEncoder), escala (StandardScaler/MinMax si aplica) y creación de atributos combinados (rooms_per_household, population_per_household, bedrooms_per_room) mediante un `Transformer` personalizado (`CombinedAttributesAdder`).

4. **Select & train models**  
   - Modelos: `LinearRegression`, `DecisionTreeRegressor`, `RandomForestRegressor`.
   - Búsqueda de hiperparámetros con `RandomizedSearchCV` (CV=3 por defecto).
   - Métrica: RMSE (se usó `scoring="neg_root_mean_squared_error"` ó `neg_mean_squared_error` y se sacó raíz).

5. **Fine-tuning**  
   - Se probaron combinaciones de hiperparámetros relevantes (ver “Hiperparámetros y justificación”).

6. **Present / Deploy**  
   - Guardado del `full_pipeline` y del `best_model` con `joblib`.
   - App local con Streamlit (`app.py`) que carga los archivos guardados y permite ingresar features para predecir en vivo.

---

## ⚙️ Hiperparámetros (ejemplos y justificación)

### Regresión Lineal
- No hay muchos hiperparámetros a optimizar en `LinearRegression` (es un baseline). Se usó como referencia.

### Decision Tree Regressor (parámetros explorados)

param_distribs = {
  "max_depth": [None, 10, 20, 30,40,50],
  "min_samples_split": [2, 5, 10],
  "min_samples_leaf": [1, 2, 4],
}

Por qué: 

max_depth controla complejidad y sobreajuste.

min_samples_split y min_samples_leaf evitan hojas con muy pocos datos (reduce varianza).

### Random Forest Regressor (parámetros explorados)

param_distribs_rf = {
    'n_estimators': [3, 10, 30, 100, 300],
    'max_features': [2, 4, 6, 8, 10, 12],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

Por qué:

- n_estimators (más árboles → predicciones más estables).

- max_features controla la diversidad entre árboles (reduce correlación).

- max_depth, min_samples_* para controlar complejidad y evitar overfitting.

Se usó RandomizedSearchCV porque:

- Explora un espacio de parámetros más amplio con menor costo computacional que un GridSearch exhaustivo.

- Es eficiente cuando algunas combinaciones tienen poco sentido o el espacio es grande.

### 🧮 Evaluación (calcular RMSE)

import pandas as pd

Crear un DataFrame para comparar los resultados de los modelos en el conjunto de prueba
Asegúrate de que las variables lin_rmse_test, tree_rmse_test y forest_rmse_test_rs existan de celdas anteriores
comparison_data = {'Model': ['Linear Regression', 'Decision Tree', 'Random Forest'],
                   'Test RMSE': [lin_rmse_test, tree_rmse_test, forest_rmse_test_rs]}
comparison_df = pd.DataFrame(comparison_data)

Ordenar por Test RMSE para encontrar el mejor modelo (menor RMSE es mejor)

comparison_df = comparison_df.sort_values(by='Test RMSE')

print("Comparación de modelos (RMSE en el conjunto de prueba):")
display(comparison_df)

Identificar el mejor modelo

best_model_name = comparison_df.iloc[0]['Model']
best_rmse = comparison_df.iloc[0]['Test RMSE']

print(f"\nEl mejor modelo basado en el Test RMSE es: {best_model_name} con un RMSE de {best_rmse:.2f}")

"El mejor modelo basado en el Test RMSE es: Random Forest con un RMSE de 46869.40"

### 🧩 Guardar / Cargar modelo 

import joblib
import os

Define the directory to save the model and pipeline

model_dir = "saved_models"
os.makedirs(model_dir, exist_ok=True)

Save the best Random Forest model

joblib.dump(best_forest_reg_rs, os.path.join(model_dir, "best_random_forest_model.pkl"))

Save the full pipeline (including preprocessing)

joblib.dump(full_pipeline, os.path.join(model_dir, "full_pipeline.pkl"))

print(f"Modelo y pipeline guardados en el directorio: {model_dir}")

### 📲 Uso de la app de streamlit (app.py)

1. Coloca best_random_forest_model.pkl y full_pipeline.pkl en la carpeta indicada por model_dir (por defecto en app.py está C:/StreamlitApp/saved_models — cambia según tu máquina)
2. Instala dependencias (streamlit) y ejecuta en cmd lo siguiente: streamlit run `ruta completa del archivo .py` (se recomienda guardarlo en C:, para que sea más fácil a la hora de meter la ruta completa del archivo y evitar problemas)
3. En la interfaz podrás introducir valores para las features (longitud, latitud, median_income, total_rooms, total_bedrooms, population, households, housing_median_age y ocean_proximity) y pulsar Predecir Valor de la Vivienda.

### 📌 Documentación técnica de app.py (funcionalidad principal)

CombinedAttributesAdder: Transformer personalizado que crea atributos combinados:

rooms_per_household = total_rooms / households

population_per_household = population / households

bedrooms_per_room = total_bedrooms / total_rooms (opcional)

Esto replica exactamente las transformaciones que se usaron durante el entrenamiento para mantener coherencia entre entrenamiento y predicción.

Carga de pipeline y modelo:

full_pipeline realiza las mismas transformaciones que se definieron y guardaron durante el entrenamiento.

best_model es el estimador final (Random Forest en este caso).

Flujo de predicción:

El usuario ingresa los valores en la UI de Streamlit.

input_data se transforma con full_pipeline.transform.

best_model.predict devuelve la predicción final (valor medio de la vivienda).

Mensajes de estado: st.success / st.error para feedback al usuario. Si la carga del modelo falla, la app se detiene con st.stop().






