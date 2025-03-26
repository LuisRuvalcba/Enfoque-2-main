import numpy as np

class KohonenMap:
    def __init__(self, input_dim, map_dim):
        self.input_dim = input_dim
        self.map_dim = map_dim
        self.weights = np.random.rand(map_dim[0], map_dim[1], input_dim)

    def train(self, data, learning_rate=0.1, epochs=100):
        for epoch in range(epochs):
            for x in data:
                # Encuentra el nodo ganador (BMU)
                bmu_idx = np.argmin(np.linalg.norm(self.weights - x, axis=(2, 1)))

                # Actualiza los pesos de la vecindad de la BMU
                for i in range(self.map_dim[0]):
                    for j in range(self.map_dim[1]):
                        dist_to_bmu = np.linalg.norm(np.array([i, j]) - np.array(bmu_idx))
                        if dist_to_bmu < 2:
                            self.weights[i, j] += learning_rate * (x - self.weights[i, j])

    def predict(self, data):
        predictions = []
        for x in data:
            bmu_idx = np.argmin(np.linalg.norm(self.weights - x, axis=(2, 1)))
            predictions.append(bmu_idx)
        return predictions

# Datos de ejemplo
data = np.random.rand(100, 2)

# Creamos y entrenamos el mapa autoorganizado de Kohonen
mapa_kohonen = KohonenMap(input_dim=2, map_dim=(5, 5))
mapa_kohonen.train(data, learning_rate=0.01, epochs=100)

# Predicción de agrupamiento
predictions = mapa_kohonen.predict(data)
print(predictions)
