# 🌲 Random Forest Classifier – Lung Cancer Prediction


Este proyecto aplica el algoritmo de Random Forest para predecir cáncer de pulmón utilizando el Lung Cancer Dataset de Kaggle.
Se implementaron tres variaciones del modelo:

**1. Random Forest sin escalar (sin ajuste)**

**2. Random Forest sin escalar (con ajuste de hiperparametros)**

**3. Random Forest con datos escalados (sin ajuste)**

El objetivo fue evaluar cómo afecta el escalado de datos, el ajuste de hiperparámetros y la naturaleza del dataset al rendimiento del modelo. 
Finalmente, también se analizó si era necesario entrenar un cuarto modelo (RF escalado + ajuste), como lo indicaban las instrucciones de la práctica.

---

## 📂 Dataset

- Fuente: Kaggle [Lung Cancer Dataset](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer.)

- Tarea: Clasificación binaria

- Objetivo: Identificar si un paciente presenta cáncer de pulmón

- Características: Variables clínicas (numéricas y categóricas)

---

## 🔍 Exploración inicial de los datos (EDA)

La exploración inlcuyo:

    - Identificación de valores nulos

    - Análisis de balance de clases
    
    - Histogramas y distribuciones

    - Matriz de correlación

En esta etapa NO se aplicaron transformaciones; solo análisis descriptivo.

---

## ✂ Partición Train/Test

Se dividió el dataset en:

* 80% Entrenamiento

* 20% Prueba


Se evaluó si se requería una partición estratificada, revisando:

  - Distribución de la variable objetivo (clases)

  - Existencia de desbalance

Para problemas de clasificación es casi obligatoria realizar la partición estratificada, por lo tanto, si se realizo la partición estratificada

---

## 🛠 Preprocesamiento con Pipeline

Una vez analizadas las deficiencias del dataset, se creó un Pipeline que manejó:

✔ Imputación de valores nulos

Para columnas numéricas y categóricas.

✔ Codificación de variables no numéricas

En caso de existir.

✔ Normalización / Escalado

Uso de StandardScaler, crucial para modelos basados en gradiente.

✔ Integración completa

El Pipeline se entrenó solo con Train para evitar data leakage.

---

## 🌲 Implementación de Modelos Random Forest

Se implementaron 3 Modelos de Random Forest

- Random Forest (sin escalar y sin ajuste)

- Random Forest (sin escalar con ajuste)

🔧 Hiperparámetros óptimos encontrados con GridSearchCV

```
{
    'classifier__max_depth': None,
    'classifier__min_samples_leaf': 1,
    'classifier__min_samples_split': 5,
    'classifier__n_estimators': 100
}

```

- Random Forest (con datos escalados sin ajuste)

Adicionalmente se pidio implementar un 4º modelo: Random Forest con datos escalados y con ajuste

## 🛑 ¿Por qué NO se entrenó el Modelo 4 (escalado + ajuste)?

Las instrucciones pedían entrenarlo solo si el modelo escalado superaba al modelo sin escalar.

Al implementar los 3 modelos se obtuvieron los siguientes resultados:

| Modelo RF | Accuracy | Recall | Precision | F1-score |
|-------------------|-------------|----------|-----------|----------|
| **RF sin escalado y sin ajustar** | 0.9032 | 0.9615 | 0.9259 | 0.9434 |
| **RF sin escalado y con ajuste** | 0.8710 | 0.9107 | 0.9444 | 0.9273 |
| **RF con escalado y sin ajustar** | 0.8871 | 0.9434 | 0.9259 | 0.9346 |

El escalado de los datos no mejoró el rendimiento. Dado que Random Forest:

  - No es sensible al escalado

  - Está diseñado para manejar datos heterogéneos

  - No mejoró con ajuste de hiperparámetros

Se concluyó que no era necesario entrenar el Modelo 4 

---

## 🏆 Mejor Modelo

El mejor desempeño lo obtuvo:

⭐ Random Forest sin escalar (sin ajuste)

Con las métricas:

    - Accuracy: 0.9032

    - Precision: 0.9615

    - Recall: 0.9259

    - F1-score: 0.9434

Este modelo fue el más estable y con mejor balance entre Precision y Recall, crítico en diagnósticos médicos.

---

## 📚 Comparación con la práctica de SVM

También en las instrucciones de la práctica se pidio comparar estos resultados con los del SVM implementado anteriormente

| Modelo                  | Mejor Accuracy  | Observaciones                    |
| ----------------------- | --------------- | -------------------------------- |
| **SVM Lineal Ajustado** | 0.9032          | Igual desempeño que el RF 1      |
| **SVM RBF/Poly**        | 0.8710 – 0.9032 | Rendimiento variable             |
| **RF sin escalar**      | **0.9032**      | Mismo mejor valor que SVM Lineal |


+ Tanto SVM Lineal como RF sin escalar ofrecieron el MEJOR rendimiento.

+ Los modelos basados en árboles no se benefician del escalado.

+ SVM es más sensible a la escala y la selección del kernel.

+ RF es más robusto y menos sensible a parámetros.

+ Ambos métodos confirman que el dataset presenta patrones mayormente lineales y bien definidos.

---

## 🧠 Conclusiones

Este proyecto permitió analizar cómo el preprocesamiento y el ajuste de hiperparámetros afectan el desempeño de Random Forest.

* El Random Forest sin escalar y sin ajuste es el mejor modelo para este dataset.

* Escalar datos no aporta mejoras para modelos de árboles.

* El ajuste de hiperparámetros no garantizó mejoras significativas.

* Es importante probar diferentes configuraciones antes de asumir qué técnica funcionará mejor.

* Random Forest y SVM Lineal son los modelos más competitivos en este problema.

* El análisis refuerza que en tareas de salud se debe priorizar el equilibrio entre Precision y Recall, ambos altos en el modelo seleccionado.

---

## ✒️ Autor

Allan Hall Solorio





