import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import NearestNeighbors

# Generar datos sintéticos
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Entrenar el modelo k-NN
k = 4
modelo_knn = NearestNeighbors(n_neighbors=k)
modelo_knn.fit(X)

# Calcular las distancias y los índices de los vecinos más cercanos
distancias, indices = modelo_knn.kneighbors(X)

# Visualizar los clusters
plt.scatter(X[:, 0], X[:, 1], c=indices[:, 0], s=50, cmap='viridis')
plt.show()
