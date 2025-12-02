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

# CARGA DEL MODELO ENTRENADO
# Obtener el directorio donde se encuentra el script de Streamlit
script_dir = os.path.dirname(__file__)
# Construir la ruta al modelo relativa al directorio del script
model_path = os.path.join(script_dir, "saved_models", "final_prediction_pipeline.pkl")


@st.cache_resource
def load_model(path):
    try:
        model = joblib.load(path)
        return model
    except FileNotFoundError:
        st.error(f"Error: El archivo del modelo no se encontró en {path}. Asegúrate de haberlo guardado correctamente.")
        return None

final_pipeline = load_model(model_path)

if final_pipeline is not None:
    st.success("Modelo cargado correctamente.")

# --- Datos del día actual ---
st.subheader("Datos del Día Actual")

col1, col2, col3 = st.columns(3)

with col1:
    open_price = st.number_input("Precio de Apertura (Open)", value=100.0, format="%.4f")
    volume = st.number_input("Volumen (Volume)", value=1_000_000.0, format="%.4f")

with col2:
    high_price = st.number_input("Precio Más Alto (High)", value=102.0, format="%.4f")
    close_price = st.number_input("Precio de Cierre (Close)", value=101.0, format="%.4f")

with col3:
    low_price = st.number_input("Precio Más Bajo (Low)", value=99.0, format="%.4f")

# --- Lags de Adj Close ---
st.subheader("Precios de Cierre Ajustados de Días Anteriores (Lags)")
col_lag1, col_lag2, col_lag3 = st.columns(3)

with col_lag1:
    adj_close_lag1 = st.number_input("Adj. Close (Hace 1 día)", value=100.50, format="%.4f")
with col_lag2:
    adj_close_lag2 = st.number_input("Adj. Close (Hace 2 días)", value=100.20, format="%.4f")
with col_lag3:
    adj_close_lag3 = st.number_input("Adj. Close (Hace 3 días)", value=99.80, format="%.4f")

    
    # 4. BOTÓN DE PREDICCIÓN
if st.button("Predecir Precio de Cierre Ajustado"):

    if final_pipeline is not None:
        # Crear DataFrame con los datos ingresados
        input_data = pd.DataFrame([[open_price, high_price, low_price, close_price, volume,
                                    adj_close_lag1, adj_close_lag2, adj_close_lag3]],
                                  columns=['Open', 'High', 'Low', 'Close', 'Volume',
                                           'Adj Close_Lag1', 'Adj Close_Lag2', 'Adj Close_Lag3'])

        # Predicción
        prediction = final_pipeline.predict(input_data)[0]

        # Mostrar ressultados
        st.success(f"### El precio de cierre ajustado (Adj. Close) para el siguiente día sería de: **${prediction:.2f} USD**")
        st.balloons()
    else:
        st.error("Error: el modelo no se cargó correctamente.")



