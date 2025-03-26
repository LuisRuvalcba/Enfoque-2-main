import numpy as np

# Definimos los datos de entrada y salida
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas
y = np.array([0, 0, 0, 1])  # Salidas esperadas

# Definimos una función para determinar si los datos son linealmente separables
def es_linealmente_separable(X, y):
    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            if (y[i] != y[j]):
                if (np.array_equal(X[i], X[j])):
                    continue
                if (np.dot(X[i], X[j]) <= 0):
                    return False
    return True

# Verificamos si los datos son linealmente separables
if es_linealmente_separable(X, y):
    print("Los datos son linealmente separables")
else:
    print("Los datos no son linealmente separables")
