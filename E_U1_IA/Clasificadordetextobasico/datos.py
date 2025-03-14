import numpy as np
import pandas as pd 
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


newsgroups = fetch_20newsgroups(subset='all')


X_train, X_test, y_train, y_test = train_test_split(newsgroups.data, newsgroups.target, test_size=0.25, random_state=42)


vectorizer = CountVectorizer(stop_words='english')
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


clf = MultinomialNB()
clf.fit(X_train_vectorized, y_train)

# Predecir sobre los datos de prueba
y_pred = clf.predict(X_test_vectorized)

# Evaluar el clasificador
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del clasificador: {accuracy * 100:.2f}%")

# Mostrar un reporte de clasificación
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=newsgroups.target_names))

# Mostrar algunas predicciones con su clase verdadera
print("\nAlgunas predicciones:")
for i in range(5):
    print(f"Texto: {X_test[i][:200]}...")  # Mostramos los primeros 200 caracteres del texto
    print(f"Clase verdadera: {newsgroups.target_names[y_test[i]]}")
    print(f"Predicción: {newsgroups.target_names[y_pred[i]]}")
    print("-" * 80)

# Graficar la matriz de confusión
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(12, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=newsgroups.target_names, yticklabels=newsgroups.target_names)
plt.xlabel('Predicción')
plt.ylabel('Verdadero')
plt.title('Matriz de Confusión')
plt.xticks(rotation=90)  # Rotar etiquetas para mejorar la visualización
plt.yticks(rotation=0)   # Rotar etiquetas para mejorar la visualización
plt.show()
