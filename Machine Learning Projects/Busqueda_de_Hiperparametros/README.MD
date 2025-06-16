# 🍷 Búsqueda de Hiperparámetros en Modelos de Clasificación – GridSearchCV

Este proyecto muestra cómo optimizar modelos de clasificación en Machine Learning mediante la técnica de *búsqueda de hiperparámetros* usando GridSearchCV. 
El análisis se aplicó al conjunto de datos **load_wine** de la librería scikit-learn, el cual contiene información química de diferentes tipos de vino.

---

## 🎯 Objetivo

Implementar una red neuronal multicapa (MLP) optimizada mediante GridSearchCV, evaluando su desempeño en un problema de clasificación multiclase con base en los datos químicos de muestras de vino.
---

## 🛠 Tecnologías utilizadas

- 🐍 Python 3
- 📚 scikit-learn
- 📊 seaborn y matplotlib
- 📁 Jupyter Notebook

---

## 📈 Descripción del procedimiento

1. **Carga del dataset load_wine** desde sklearn.datasets.
2. *Partición del conjunto de datos* en 80% para entrenamiento y 20% para prueba.
3. *Estandarización de los datos* mediante una técnica de escalamiento.
4. *Definición del modelo base:*
   - Red neuronal MLP con dos capas ocultas.
5. **Búsqueda de hiperparámetros con GridSearchCV (CV=5):**
   - Tres configuraciones distintas en el número de neuronas en las capas ocultas.
   - Tres funciones de activación diferentes.
   - Tres algoritmos optimizadores distintos.
6. *Selección y despliegue del mejor modelo* resultante del proceso de búsqueda.
7. *Evaluación del modelo sobre el conjunto de prueba:*
   - Despliegue de la *matriz de confusión*.
   - Reporte de métricas: *accuracy, **precision, **recall, y **f1-score*.
8. *Conclusión final* del experimento con interpretación de resultados.

---

## 🔍 Resultados obtenidos

- El modelo optimizado superó al modelo base en términos de precisión.
- Se identificó una combinación de hiperparámetros más eficiente para clasificar correctamente las clases de vino.
- El análisis evidenció cómo una buena elección de hiperparámetros mejora la capacidad predictiva.

---

## 📎 Archivos incluidos

- Busqueda_de_Hiperparametros.ipynb: Notebook con código, explicación paso a paso y visualización de resultados.

---

## ✅ Conclusiones

Este ejercicio demuestra cómo la técnica de búsqueda en cuadrícula (GridSearchCV) permite encontrar automáticamente la configuración óptima de hiperparámetros para modelos de clasificación. En este caso, el dataset de vinos sirvió para practicar análisis de modelos multiclase y evaluar rendimiento en un contexto realista.

---

## 📄 Licencia

Este proyecto es parte de mi portafolio académico y está disponible con fines educativos y de demostración técnica.
