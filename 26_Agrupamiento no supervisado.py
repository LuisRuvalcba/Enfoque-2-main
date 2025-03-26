import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generar datos sintéticos
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Aplicar el algoritmo K-Means
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Obtener los centroides y las etiquetas de los clusters
centroides = kmeans.cluster_centers_
etiquetas = kmeans.labels_

# Visualizar los clusters y los centroides
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, s=50, cmap='viridis')
plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=200, color='red')
plt.show()
