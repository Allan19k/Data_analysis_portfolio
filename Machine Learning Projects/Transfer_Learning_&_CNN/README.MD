# 🧠 Transfer Learning con ResNet50 para Clasificación de Herramientas – Kaggle Dataset

Este proyecto implementa una red neuronal convolucional utilizando **Transfer Learning con ResNet50** para clasificar imágenes de herramientas, con base en un conjunto de datos disponible en **Kaggle**. 
El enfoque se centró en mejorar el rendimiento del modelo original a través de técnicas avanzadas de entrenamiento, preprocesamiento y ajuste fino.

---

## 🎯 Objetivo

Desarrollar un modelo de clasificación robusto y eficiente que identifique correctamente las clases presentes en una base de datos de herramientas, utilizando estrategias de mejora sobre un modelo preentrenado.

---

## 🛠️ Tecnologías utilizadas

- 🐍 Python 3
- 🧠 TensorFlow + Keras
- 🧩 ResNet50 (`imagenet`)
- 📊 Matplotlib & Seaborn

---

## 🧪 Implementaciones realizadas

1. **Carga del modelo preentrenado ResNet50** sin las capas finales (`include_top=False`).
2. **Congelamiento parcial de capas** (primeras 100 capas congeladas, el resto entrenable).
3. **Clasificador personalizado (MLP)** añadido al modelo:
   - Capa de pooling global
   - Capas densas con activación `ReLU` y `Dropout` (50%)
   - Capa de salida con activación `softmax`
4. **Optimización del entrenamiento**:
   - Optimizador: `Adam` con tasa de aprendizaje 0.0001
   - Función de pérdida: `categorical_crossentropy`
5. **Técnicas avanzadas de mejora de desempeño**:
   - **Aumento de datos (Data Augmentation) agresivo**: rotación, desplazamiento, zoom, shear, volteo horizontal, etc.
   - **Class weights automáticos** para combatir el desbalanceo de clases
   - Callbacks: `EarlyStopping` y `ReduceLROnPlateau`
6. **Validación cruzada implícita** mediante partición del 20% como conjunto de validación

---

## 📊 Evaluación del modelo

- Se desplegó la **matriz de confusión** y el **informe de clasificación** para evaluar el rendimiento sobre el conjunto de validación.
- Se logró una mejora significativa en la precisión del modelo comparado con una arquitectura base sin ajustes.

---

## 📁 Archivos incluidos

- `CNN_Transfer_Learning.ipynb`: Notebook con todo el flujo de trabajo implementado: carga de datos, procesamiento, entrenamiento y evaluación.

---

## ✅ Conclusiones

La integración de Transfer Learning con **técnicas de mejora específicas** como el congelamiento parcial, regularización con dropout y el ajuste del clasificador, permitió mejorar sustancialmente la capacidad del modelo para clasificar imágenes de herramientas. 
Este enfoque resulta altamente útil para tareas de visión por computadora cuando se dispone de un dataset limitado.

---

## 📄 Licencia

Este proyecto forma parte de mi portafolio académico con fines educativos y de demostración técnica.
