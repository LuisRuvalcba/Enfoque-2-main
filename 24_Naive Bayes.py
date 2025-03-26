from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Cargar los datos de comentarios de películas
comentarios = load_files('Comentarios/Comentario1.txt')

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(comentarios.data, comentarios.target, test_size=0.2, random_state=42)

# Vectorización de palabras
vectorizer = CountVectorizer()
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Entrenar el clasificador Naive Bayes
clasificador = MultinomialNB()
clasificador.fit(X_train_vect, y_train)

# Predecir en el conjunto de prueba
predicciones = clasificador.predict(X_test_vect)

# Calcular la precisión
precision = accuracy_score(y_test, predicciones)
print("Precision:", precision)
