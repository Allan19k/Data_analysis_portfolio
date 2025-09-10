import streamlit as st
import joblib
import pandas as pd
import os

from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

# Define los índices de las columnas relevantes para la creación de atributos combinados
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
  # Inicializador de la clase, permite especificar si se añade el atributo 'bedrooms_per_room'
  def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
    self.add_bedrooms_per_room = add_bedrooms_per_room
  # Método fit, en este caso no hace nada ya que no hay parámetros que aprender de los datos
  def fit(self, X, y=None):
    return self # Retorna la instancia de la clase
  # Método transform, crea los nuevos atributos combinados
  def transform(self, X):
    # Calcula habitaciones por hogar
    rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
    # Calcula población por hogar
    population_per_household = X[:, population_ix] / X[:, households_ix]
    # Si se especifica, calcula dormitorios por habitación
    if self.add_bedrooms_per_room:
      bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
      # Devuelve la matriz original X concatenada con los nuevos atributos
      return np.c_[X, rooms_per_household, population_per_household,
      bedrooms_per_room]
    else:
      # Devuelve la matriz original X concatenada con los atributos sin 'bedrooms_per_room'
      return np.c_[X, rooms_per_household, population_per_household]

# Define the directory where the model and pipeline are saved
model_dir = 'C:/StreamlitApp/saved_models'

# Load the trained model and the full pipeline
try:
    model_path = os.path.join(model_dir, "best_random_forest_model.pkl")
    pipeline_path = os.path.join(model_dir, "full_pipeline.pkl")
    best_model = joblib.load(model_path)
    full_pipeline = joblib.load(pipeline_path)
    st.success("Modelo y pipeline cargados exitosamente.")
except Exception as e:
    st.error(f"Error al cargar el modelo o el pipeline: {e}")
    st.stop() # Stop the app if loading fails

st.title("End to End project: California Housing Price Prediction")
st.write("Data Science 8CC2")
st.write("Allan Hall Solorio 358909")
st.write("Universidad Autónoma de Chihuahua")
st.write("Facultad de Ingeniería")
st.write("Ingeniería en Ciencias de la computación")
st.write("Docente: Olanda Prieto Ordaz")
st.write("Fecha de entrega: Jueves 4 de septiembre del 2025")
st.write("Esta aplicación predice el valor medio de una vivienda en California basado en sus características.")

# Create input fields for the features
st.header("Características de la Vivienda")

# Example input fields (adjust based on your features)
longitude = st.number_input("Longitud", value=-122.23)
latitude = st.number_input("Latitud", value=37.88)
housing_median_age = st.number_input("Edad Media de la Vivienda", value=41.0)
total_rooms = st.number_input("Total de Habitaciones", value=880.0)
total_bedrooms = st.number_input("Total de Dormitorios", value=129.0)
population = st.number_input("Población", value=322.0)
households = st.number_input("Hogares", value=126.0)
median_income = st.number_input("Ingreso Medio", value=8.3252)
ocean_proximity = st.selectbox("Proximidad al Océano", ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND'])

# Create a DataFrame from the input values
input_data = pd.DataFrame([[longitude, latitude, housing_median_age, total_rooms, total_bedrooms,
                            population, households, median_income, ocean_proximity]],
                          columns=['longitude', 'latitude', 'housing_median_age', 'total_rooms',
                                   'total_bedrooms', 'population', 'households', 'median_income',
                                   'ocean_proximity'])

# Add a button to make a prediction
if st.button("Predecir Valor de la Vivienda"):
    try:
        # Apply the same preprocessing as used during training
        input_data_prepared = full_pipeline.transform(input_data)

        # Make a prediction using the loaded model
        prediction = best_model.predict(input_data_prepared)

        # Display the prediction
        st.header("Predicción")
        st.success(f"El valor medio predicho de la vivienda es: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error al realizar la predicción: {e}")