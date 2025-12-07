# 🚬 Lung Cancer Classification — Machine Learning Projects

Colección de prácticas aplicadas de Data Science utilizando el dataset de cáncer de pulmón (Kaggle).

Este repositorio reúne una serie de proyectos desarrollados para aplicar diferentes técnicas de Machine Learning, abarcando desde modelos lineales hasta ensambles avanzados. Cada práctica contiene su propio README con el procedimiento completo, análisis, implementación, resultados y conclusiones.

El objetivo global fue explorar múltiples enfoques de clasificación, evaluar su rendimiento, realizar comparaciones entre modelos y comprender cómo el preprocesamiento, la optimización y la naturaleza del algoritmo influyen en el desempeño final.

---

## 📂 Contenido del Proyecto

Este directorio contiene las siguientes prácticas:

1️⃣ Logistic Regression 

Objetivo: Entrenar un modelo de clasificación usando Regresión Logística y optimizarlo mediante GridSearch.

**Incluye**

* Análisis exploratorio

* Correlaciones

* Partición Train/Test

* Pipeline de preprocesamiento

* Modelo SGD sin ajustar

* Modelo SGD ajustado

* Cross Validation (10 folds)

* Evaluación con métricas: Accuracy, Recall, Precision, F1-score

* Matriz de confusión

* Conclusiones basadas en los resultados

Mejor modelo:

SGDClassifier ajustado.
Accuracy final: ~0.9032

2️⃣ SVM — Modelos Lineales y No Lineales

Objetivo: Comparar distintos tipos de SVM y evaluar su capacidad para clasificar correctamente casos de cáncer pulmonar.

Modelos implementados:

- SVM Lineal

- SVM RBF

- SVM Polinomial

GridSearch / RandomSearch

Matrices de confusión y métricas completas

Hallazgos importantes:

* El SVM Lineal Ajustado obtuvo el mejor desempeño general.

* Comparación con 3 artículos científicos de Kaggle que usaron el mismo dataset.

Accuracy final del mejor modelo: 0.9032

3️⃣ Random Forest — Comparación de Escalado y Ajuste

Objetivo: Evaluar el impacto del escalado y la optimización de hiperparámetros en Random Forest.

Modelos evaluados:

- RF sin escalar (default)

- RF sin escalar + ajuste

- RF escalado (default)

- RF escalado + ajuste (no fue necesario implementarlo)

Conclusiones clave:

* El escalado no mejora necesariamente los modelos basados en árboles.

* El mejor desempeño se obtuvo sin escalar y sin ajuste.

Mejor modelo:

Random Forest (default, sin escalado)
Accuracy: 0.9032

4️⃣ Ensemble Learning 

Objetivo: Probar técnicas de ensamble para superar el rendimiento de modelos individuales.

Modelos implementados:

- VotingClassifier (Hard Voting)

- BaggingClassifier

- PastingClassifier

- AdaBoost

- Gradient Boosting

- XGBoost

Comparación general:

Los modelos de ensamble fueron evaluados con métricas estándar, mostrando un rendimiento superior respecto a LR, SVM y Random Forest.

Mejor modelo:
⭐ VotingClassifier (Hard Voting)
Accuracy: 0.9194
F1-score: 0.9533

Conclusión:
* Los ensambles demostraron ser los modelos más robustos y con mejor desempeño en el dataset.

---

## 📊 Comparación Global entre las Prácticas

| Práctica / Modelo   | Mejor Modelo             | Accuracy   |
| ------------------- | ------------------------ | ---------- |
| Logistic Regression | SGD Ajustado             | 0.9032     |
| SVM                 | SVM Lineal Ajustado      | 0.9032     |
| Random Forest       | RF Default (No escalado) | 0.9032     |
| **Ensembles**       | **VotingClassifier**     | **0.9194** |

🏆 Modelo ganador absoluto del proyecto:

⭐ VotingClassifier (Hard Voting)

Superó a todos los modelos individuales y otros ensambles en precisión, balance y desempeño general

---

## 🔍 Conclusión General del Proyecto

Este conjunto de prácticas permitió:

* Aplicar el ciclo completo de Machine Learning.

* Comparar modelos lineales, no lineales y basados en árboles.

* Implementar pipelines de preprocesamiento robustos.

* Ajustar hiperparámetros con técnicas modernas (GridSearch, RandomSearch).

* Utilizar modelos avanzados como AdaBoost, Gradient Boosting y XGBoost.

* Demostrar la superioridad de los ensambles al combinar las fortalezas de distintos algoritmos.

## 👨‍💻 Autor

Allan Hall

Estudiante de Ingeniería en Ciencias de la Computación | Enfoque en Data Science & Machine Learning

Proyecto desarrollado como parte de la materia de Data Science a cargo de la Dra. Olanda Prieto Ordaz



