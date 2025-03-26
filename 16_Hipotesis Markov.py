import numpy as np
import matplotlib.pyplot as plt

# Definimos la matriz de transición de probabilidades
matriz_transicion = np.array([[[0.2, 0.6, 0.2],  # Probabilidad de pasar de A a A, B y C
                                [0.7, 0.1, 0.2],  # Probabilidad de pasar de B a A, B y C
                                [0.3, 0.4, 0.3]], # Probabilidad de pasar de C a A, B y C
                               [[0.5, 0.3, 0.2],  # Probabilidad de pasar de A a A, B y C
                                [0.2, 0.5, 0.3],  # Probabilidad de pasar de B a A, B y C
                                [0.1, 0.1, 0.8]]])# Probabilidad de pasar de C a A, B y C

# Definimos los estados posibles
estados = ['A', 'B', 'C']

# Configuración inicial
estado_actual = 'A'
estado_anterior = 'B'
longitud = 100

# Generamos la secuencia de estados utilizando el proceso de Markov
secuencia_estados = [estado_anterior, estado_actual]
for _ in range(longitud - 2):
    prob_transicion = matriz_transicion[estados.index(estado_anterior), estados.index(estado_actual)]
    estado_siguiente = np.random.choice(estados, p=prob_transicion)
    secuencia_estados.append(estado_siguiente)
    estado_anterior = estado_actual
    estado_actual = estado_siguiente

# Graficamos la secuencia de estados
plt.figure(figsize=(10, 4))
plt.plot(range(longitud), secuencia_estados, marker='o', linestyle='-', color='b')
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.title('Proceso de Markov de Orden 2')
plt.yticks(range(len(estados)), estados)
plt.grid(True)
plt.show()
