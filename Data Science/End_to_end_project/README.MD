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

# Crear un DataFrame para comparar los resultados de los modelos en el conjunto de prueba
# Asegúrate de que las variables lin_rmse_test, tree_rmse_test y forest_rmse_test_rs existan de celdas anteriores
comparison_data = {'Model': ['Linear Regression', 'Decision Tree', 'Random Forest'],
                   'Test RMSE': [lin_rmse_test, tree_rmse_test, forest_rmse_test_rs]}
comparison_df = pd.DataFrame(comparison_data)

# Ordenar por Test RMSE para encontrar el mejor modelo (menor RMSE es mejor)
comparison_df = comparison_df.sort_values(by='Test RMSE')

print("Comparación de modelos (RMSE en el conjunto de prueba):")
display(comparison_df)

# Identificar el mejor modelo
best_model_name = comparison_df.iloc[0]['Model']
best_rmse = comparison_df.iloc[0]['Test RMSE']

print(f"\nEl mejor modelo basado en el Test RMSE es: {best_model_name} con un RMSE de {best_rmse:.2f}")

"El mejor modelo basado en el Test RMSE es: Random Forest con un RMSE de 46869.40"

### 🧩 Guardar / Cargar modelo 

import joblib
import os

# Define the directory to save the model and pipeline
model_dir = "saved_models"
os.makedirs(model_dir, exist_ok=True)

# Save the best Random Forest model
joblib.dump(best_forest_reg_rs, os.path.join(model_dir, "best_random_forest_model.pkl"))

# Save the full pipeline (including preprocessing)
joblib.dump(full_pipeline, os.path.join(model_dir, "full_pipeline.pkl"))

print(f"Modelo y pipeline guardados en el directorio: {model_dir}")

### 📲 Uso de la app de streamlit (app.py)





