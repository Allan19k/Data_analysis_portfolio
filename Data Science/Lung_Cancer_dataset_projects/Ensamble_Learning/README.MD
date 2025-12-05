# 🧪 Práctica: Modelos de Ensamble

Clasificación de Cáncer de Pulmón — Ensemble Learning

En esta práctica se exploraron 6 modelos de ensamble para mejorar el rendimiento en la tarea de clasificación binaria del dataset de cáncer de pulmón. 
A diferencia de modelos individuales, los ensambles combinan múltiples clasificadores para reducir la varianza, el sesgo o ambos, logrando predicciones más robustas.

Los modelos implementados fueron: VotingClassifier (Hard Voting), Bagging, Pasting, AdaBoost, Gradient Boosting y XGBoost.

> [!NOTE]
> 🔎 El preprocesamiento fue el mismo que en las prácticas anteriores (LR, SVM, RF), por lo que aquí únicamente se documentan los modelos de ensamble y sus resultados.

## ⚙ Modelos Implementados

⿡ VotingClassifier — Hard Voting

Clasificadores base:

* Regresión Logística

* Decision Tree

* Random Forest

Adicionalmente, se evaluó cada clasificador por separado 

⿢ BaggingClassifier

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

⿣ PastingClassifier

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

 AdaBoostClassifier

* Clasificador base: Decision Tree

* Parámetros:

```
estimator=DecisionTreeClassifier(max_depth=1)  
n_estimators=50  
learning_rate=1.0  
random_state=42

```

AdaBoost ajusta clasificadores sucesivos priorizando las instancias mal clasificadas previamente.









