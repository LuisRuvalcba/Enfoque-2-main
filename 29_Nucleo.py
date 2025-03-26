import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.svm import SVC

# Generar datos sintéticos
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Entrenar el modelo SVM con núcleo gaussiano (RBF)
modelo_svm = SVC(kernel='rbf', probability=True)
modelo_svm.fit(X, y)

# Crear una malla para visualizar la frontera de decisión
xx, yy = np.meshgrid(np.linspace(X[:,0].min()-1, X[:,0].max()+1, 100),
                     np.linspace(X[:,1].min()-1, X[:,1].max()+1, 100))
Z = modelo_svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z_proba = modelo_svm.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)
Z_proba = Z_proba.reshape(xx.shape)

# Visualizar la frontera de decisión y las probabilidades
plt.contourf(xx, yy, Z_proba, cmap='RdBu', alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='RdBu', edgecolors='k')
plt.colorbar(label='Probabilidad')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('SVM con Nucleo Gaussiano (RBF)')
plt.show()
