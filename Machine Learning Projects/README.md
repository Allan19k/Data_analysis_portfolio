Predicción de Tasas de Cambio EUR/USD usando RNN y LSTM

Este proyecto analiza y predice las tasas de cambio diarias entre el Euro y el Dólar Estadounidense (EUR/USD) utilizando modelos de redes neuronales recurrentes: RNN y LSTM. El objetivo es comparar el rendimiento de un modelo RNN simple con un modelo LSTM, más avanzado para capturar dependencias a largo plazo en series temporales.

Este trabajo forma parte de mi portafolio de proyectos, diseñado para demostrar mis habilidades en Machine Learning y análisis de datos, alineadas con oportunidades como las prácticas profesionales en análisis de datos que requieren experiencia en ML.

Objetivo

Predecir valores futuros de la tasa de cambio EUR/USD y evaluar la efectividad de dos modelos de redes neuronales recurrentes:





RNN (Red Neuronal Recurrente Simple): Para capturar patrones básicos en series temporales.



LSTM (Memoria Larga a Corto Plazo): Para manejar dependencias a largo plazo en los datos.

Datos





Fuente: Datos históricos de precios de cierre diarios obtenidos vía yfinance.



Rango de fechas: 1 de enero de 2020 al 1 de enero de 2023.



División: 80% para entrenamiento y 20% para prueba.



Ventaneo: Se utilizó un tamaño de ventana de 10 días para crear secuencias, donde cada muestra usa los últimos 10 días para predecir el siguiente.

Metodología





Preprocesamiento:





Normalización: Se aplicó MinMaxScaler para escalar los datos entre [0, 1], mejorando la convergencia del modelo.



Ventaneo: Las secuencias de entrada se crearon con un tamaño de ventana de 10 días para capturar patrones temporales.



Modelos:





RNN: Una capa SimpleRNN con 50 unidades.



LSTM: Una capa LSTM con 50 unidades.



Ambos modelos utilizan una capa densa de salida para la predicción.



Optimizador:





Se usó Adam por su adaptabilidad, eficiencia y estabilidad en el entrenamiento de redes neuronales.



Evaluación:





Se calcularon métricas de rendimiento: MSE, RMSE y MAE para comparar los modelos.

Resultados





RNN: MSE = 0.0000, RMSE = 0.0069, MAE = 0.0054



LSTM: MSE = 0.0002, RMSE = 0.0149, MAE = 0.0115



Ambos modelos mostraron un buen rendimiento, con el RNN ligeramente superior en este caso, posiblemente debido a la simplicidad de los patrones en los datos.

Instrucciones de Uso





Entorno: El código está diseñado para ejecutarse en Google Colab.



Dependencias: Instala las siguientes bibliotecas:

!pip install yfinance
!pip install pydot
!apt-get install graphviz



Ejecución:





Carga los datos y preprocesa usando MinMaxScaler y ventaneo.



Implementa y entrena los modelos RNN y LSTM.



Evalúa los modelos con las métricas MSE, RMSE y MAE.

Conclusiones





El RNN simple superó ligeramente al LSTM en este análisis, posiblemente debido a la naturaleza de los datos.



Este proyecto demuestra habilidades en el manejo de series temporales, implementación de modelos de ML y evaluación de resultados, alineadas con roles en análisis de datos y fintech.

Licencia

Este proyecto está bajo la Licencia MIT.
