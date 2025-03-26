from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Cargar el conjunto de datos de dígitos escritos a mano
digits = load_digits()

# Dividir el conjunto de datos en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)

# Crear y entrenar el clasificador KNN
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Seleccionar una muestra de prueba aleatoria
indice = 0
muestra = X_test[indice]
etiqueta_real = y_test[indice]

# Realizar la predicción utilizando el clasificador entrenado
prediccion = knn.predict([muestra])

# Mostrar la imagen de la muestra y la etiqueta predicha
plt.gray() 
plt.matshow(muestra.reshape(8, 8))
plt.title(f'Etiqueta real: {etiqueta_real}, Etiqueta predicha: {prediccion[0]}')
plt.show()
