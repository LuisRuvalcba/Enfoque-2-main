import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
dt = 0.1  # Intervalo de tiempo
A = np.array([[1, dt], [0, 1]])  # Matriz de transición de estado
H = np.array([[0, 1]])  # Matriz de observación
Q = np.array([[0.01, 0], [0, 0.01]])  # Covarianza del proceso (ruido del sistema)
R = np.array([[0.1]])  # Covarianza de la medición (ruido del sensor)

# Estado inicial
x = np.array([[0], [1]])  # Posición inicial y velocidad inicial

# Estimación inicial de la covarianza del estado
P = np.eye(2) * 0.1

# Generación de datos de velocidad observada
np.random.seed(0)
velocidad_verdadera = [1 + np.random.normal(0, 0.5) for _ in np.arange(0, 10, dt)]

# Aplicación del filtro de Kalman
velocidad_estimada = []
for z in velocidad_verdadera:
    # Predicción
    x_pred = np.dot(A, x)
    P_pred = np.dot(np.dot(A, P), A.T) + Q
    
    # Actualización (corrección)
    y = z - np.dot(H, x_pred)
    S = np.dot(np.dot(H, P_pred), H.T) + R
    K = np.dot(np.dot(P_pred, H.T), np.linalg.inv(S))
    x = x_pred + np.dot(K, y)
    P = np.dot(np.eye(2) - np.dot(K, H), P_pred)
    
    velocidad_estimada.append(x[1, 0])

# Graficar resultados
plt.plot(np.arange(0, 10, dt), velocidad_verdadera, label='Velocidad Verdadera', color='b')
plt.plot(np.arange(0, 10, dt), velocidad_estimada, label='Velocidad Estimada', color='r', linestyle='--')
plt.xlabel('Tiempo')
plt.ylabel('Velocidad')
plt.title('Filtro de Kalman para Estimacion de Velocidad')
plt.legend()
plt.grid(True)
plt.show()
