import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# --- Configuración de la aplicación Streamlit ---
st.set_page_config(layout="wide")

# --- Datos de la portada ---
st.title("Amazon Stock Price Predictor")
st.write("### Proyecto Final de Data Science")
st.write("### Data Science 8CC2")
st.write("### Universidad Autónoma de Chihuahua")
st.write("### Facultad de Ingeniería")
st.write("### Ingeniería en Ciencias de la Computación")
st.write("### Docente: Olanda Prieto Ordaz")
st.write("### Fecha de entrega: Jueves 27 de noviembre del 2025")
st.write("> Allan Hall Solorio 358909")

st.markdown("---")

# --- Descripción del proyecto ---
st.header("Descripción del Proyecto")
st.markdown("""
El objetivo del proyecto es desarrollar y comparar varios modelos de aprendizaje capaces de predecir el precio de cierre ajustado diario de las acciones de Amazon (Adj Close) utilizando variables históricas como apertura, máximo, mínimo, volumen y el comportamiento de días previos. Esto con el fin de estimar la evolución futura del precio para identificar tendencias y evaluar la conveniencia de inversión.
""")


# --- Sección de Predicción ---
st.header("Predicción del Precio de Cierre Ajustado de Amazon")
st.write("Ingresa los datos del día actual y de los días anteriores para predecir el precio de cierre ajustado del siguiente día.")

# Ruta al directorio donde se encuentran los modelos
# Para Streamlit local, la ruta debe ser relativa al script o una ruta absoluta local.
model_dir =  'C:/Amazon_Predictor/saved_models'  # En un entorno local, esto debería ser relativo o absoluto

# --- Cargar los componentes guardados ---
try:
    best_ridge_model = joblib.load(os.path.join(model_dir, "best_ridge_model.pkl"))
    preprocess_pipeline = joblib.load(os.path.join(model_dir, "preprocess_pipeline.pkl"))
    y_scaler = joblib.load(os.path.join(model_dir, "y_scaler.pkl"))
    st.success("Modelos y escaladores cargados exitosamente.")
except FileNotFoundError:
    st.error(f"Error: No se encontraron los archivos del modelo en '{model_dir}'.")
    st.error("Asegúrate de haber descomprimido 'saved_models.zip' en la misma carpeta que 'app.py' o de especificar la ruta correcta.")
    st.stop() # Detiene la ejecución si los modelos no se cargan

# --- Función para realizar una predicción ---
def predict_amazon_stock_price(open_price, high_price, low_price, close_price, volume,
                                adj_close_lag1, adj_close_lag2, adj_close_lag3):
    new_data = pd.DataFrame([[open_price, high_price, low_price, close_price, volume,
                              adj_close_lag1, adj_close_lag2, adj_close_lag3]],
                            columns=['Open', 'High', 'Low', 'Close', 'Volume',
                                     'Adj Close_Lag1', 'Adj Close_Lag2', 'Adj Close_Lag3'])
    
    new_data_processed = preprocess_pipeline.transform(new_data)
    predicted_scaled = best_ridge_model.predict(new_data_processed)
    predicted_price = y_scaler.inverse_transform(predicted_scaled.reshape(-1, 1))[0][0]
    
    return predicted_price

# --- Entradas del usuario para las características ---
st.subheader("Datos del Día Actual (para predecir el día siguiente)")
col1, col2, col3 = st.columns(3)
with col1:
    open_price = st.number_input("Precio de Apertura (Open)", value=100.0, format="%.2f")
    high_price = st.number_input("Precio Máximo (High)", value=100.0, format="%.2f")
with col2:
    low_price = st.number_input("Precio Mínimo (Low)", value=100.0, format="%.2f")
    close_price = st.number_input("Precio de Cierre (Close)", value=100.0, format="%.2f")
with col3:
    volume = st.number_input("Volumen (Volume)", value=1000000, format="%d")

st.subheader("Precios de Cierre Ajustados de Días Anteriores (Lags)")
col_lag1, col_lag2, col_lag3 = st.columns(3)
with col_lag1:
    adj_close_lag1 = st.number_input("Adj Close (Hace 1 día)", value=99.0, format="%.2f")
with col_lag2:
    adj_close_lag2 = st.number_input("Adj Close (Hace 2 días)", value=98.0, format="%.2f")
with col_lag3:
    adj_close_lag3 = st.number_input("Adj Close (Hace 3 días)", value=97.0, format="%.2f")

# --- Botón de Predicción ---
if st.button("Predecir Precio del Siguiente Día"):
    if None not in [open_price, high_price, low_price, close_price, volume,
                    adj_close_lag1, adj_close_lag2, adj_close_lag3]:
        try:
            predicted_value = predict_amazon_stock_price(open_price, high_price, low_price, close_price, volume,
                                                         adj_close_lag1, adj_close_lag2, adj_close_lag3)
            st.success(f"### El precio de cierre ajustado predicho para el siguiente día es: **${predicted_value:.2f} USD**")
            st.balloons()
        except Exception as e:
            st.error(f"Ocurrió un error durante la predicción: {e}")
    else:
        st.warning("Por favor, rellena todos los campos para realizar la predicción.")

st.write("Para ejecutar esta aplicación localmente, guarda este código como `app.py` y asegúrate de tener la carpeta `saved_models` en el mismo directorio. Luego, ejecuta `streamlit run app.py` en tu terminal.")

