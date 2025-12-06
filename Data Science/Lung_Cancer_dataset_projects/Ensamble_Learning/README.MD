# 🧪 Ensemble Classifier - Lung Cancer Prediction 


En esta práctica se exploraron 6 modelos de ensamble para mejorar el rendimiento en la tarea de clasificación binaria del dataset de cáncer de pulmón. 

A diferencia de modelos individuales, los ensambles combinan múltiples clasificadores para reducir la varianza, el sesgo o ambos, logrando predicciones más robustas.

Los modelos implementados fueron: 

[x] VotingClassifier (Hard Voting)

[x] Bagging

[x] Pasting

[x] AdaBoost

[x] Gradient Boosting

[x] XGBoost

> [!NOTE]
> 🔎 El preprocesamiento fue el mismo que en las prácticas anteriores (LR, SVM, RF), por lo que aquí únicamente se documentan los modelos de ensamble y sus resultados.

---

## ⚙ Modelos Implementados

1️⃣ VotingClassifier — Hard Voting

Clasificadores base:

* Regresión Logística

* Decision Tree

* Random Forest

Adicionalmente, se evaluó cada clasificador por separado 

---

2️⃣ BaggingClassifier

* Clasificador base: Decision Tree

* Parámetros:

```
n_estimators=100  
max_samples=1.0  
bootstrap=True  
random_state=42  
n_jobs=-1

```

Bagging entrena múltiples modelos independientes con remuestreo con reemplazo.

---

3️⃣ PastingClassifier

* Clasificador base: Decision Tree

* Parámetros:

```

n_estimators=100  
max_samples=1.0  
bootstrap=False   # sin reemplazo  
random_state=42  
n_jobs=-1

```

Es equivalente al Bagging pero sin reemplazo, lo que modifica el nivel de variabilidad entre los modelos del ensamble.

--- 

4️⃣ AdaBoostClassifier

* Clasificador base: Decision Tree

* Parámetros:

```
estimator=DecisionTreeClassifier(max_depth=1)  
n_estimators=50  
learning_rate=1.0  
random_state=42

```

AdaBoost ajusta clasificadores sucesivos priorizando las instancias mal clasificadas previamente.

---

5️⃣ GradientBoostingClassifier

Parámetros:

```
n_estimators=100  
learning_rate=0.1  
max_depth=3  
random_state=42

```

Modelo de boosting secuencial, cada árbol busca corregir el error residual de los anteriores.

---

6️⃣ XGBoostClassifier

Parámetros principales:

```
xgb.XGBClassifier(
    random_state=42,
    eval_metric='logloss'
)

```

Se requirió mapear las etiquetas {YES, NO} → {1, 0}.


XGBoost emplea optimizaciones avanzadas de boosting, regularización y manejo eficiente del gradiente.

---

## 📊 Resultados Obtenidos

📈 Comparación de Modelos de Ensamble

| Modelo                      | Accuracy   | Precision  | Recall     | F1-score   |
| --------------------------- | ---------- | ---------- | ---------- | ---------- |
| **VotingClassifier (Hard)** | **0.9194** | **0.9623** | **0.9444** | **0.9533** |
| BaggingClassifier           | 0.9032     | 0.9615     | 0.9259     | 0.9434     |
| PastingClassifier           | **0.9194** | **0.9804** | 0.9259     | 0.9524     |
| AdaBoostClassifier          | **0.9194** | 0.9455     | **0.9630** | **0.9541** |
| GradientBoostingClassifier  | 0.8548     | 0.9245     | 0.9074     | 0.9159     |
| XGBoostClassifier           | 0.8871     | 0.9273     | 0.9444     | 0.9358     |

---

## 🏆 Modelo Ganador

✅ VotingClassifier (Hard Voting)

El mejor desempeño general fue obtenido por el VotingClassifier, que combinó Regresión Logística, Árbol de Decisión y Random Forest.
Obtuvo el mejor balance global entre precisión, recall y F1-score, logrando un rendimiento sólido y consistente.

---

## 📚 Comparación con Prácticas Anteriores

Para contextualizar, se compararon los ensambles contra los mejores modelos previos:

| Práctica                      | Mejor Modelo              | Accuracy   |
| ----------------------------- | ------------------------- | ---------- |
| **Logistic Regression**       | LR Ajustado               | 0.9032     |
| **SVM**                       | SVM Lineal Ajustado       | 0.9032     |
| **Random Forest**             | RF sin escalar (default)  | 0.9032     |
| **Ensambles (esta práctica)** | **VotingClassifier Hard** | **0.9194** |

⭐ Los ensambles superaron a todos los modelos individuales, mostrando la ventaja de combinar clasificadores.

---

## 🧾 Conclusión

Esta práctica permitió explorar diversos enfoques de Ensemble Learning, mostrando cómo cada técnica aporta distintas fortalezas:

* Bagging/Pasting redujeron la varianza.

* Boosting (AdaBoost, Gradient Boosting, XGBoost) mejoraron el rendimiento corrigiendo errores residuales.

* VotingClassifier logró la predicción más robusta al combinar modelos heterogéneos.

Los resultados confirmaron que, para este dataset en particular, el enfoque híbrido del VotingClassifier genera el mejor desempeño, superando tanto a los modelos individuales como a los otros métodos de ensamble.

---







