import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
num_particulas = 1000
tiempo_total = 10
dt = 0.1

# Función de transición del estado del objeto (movimiento rectilíneo uniforme)
def transicion_estado(posicion_actual, velocidad):
    return posicion_actual + velocidad * dt + np.random.normal(0, 0.1)

# Función de observación del objeto (medición de posición)
def observacion(posicion_real):
    return posicion_real + np.random.normal(0, 0.5)

# Inicialización de partículas
particulas = np.zeros((num_particulas, tiempo_total))
for i in range(num_particulas):
    particulas[i, 0] = np.random.uniform(0, 1) * 10  # Posición inicial aleatoria

# Filtrado de partículas
for t in range(1, tiempo_total):
    for i in range(num_particulas):
        particulas[i, t] = transicion_estado(particulas[i, t-1], 1)  # Velocidad constante = 1
    observacion_real = observacion(t)
    errores = np.abs(particulas[:, t] - observacion_real)
    pesos = np.exp(-0.5 * errores**2 / 0.5**2)  # Distribución gaussiana con desviación estándar de 0.5
    pesos /= np.sum(pesos)
    indices_remuestreo = np.random.choice(np.arange(num_particulas), size=num_particulas, p=pesos)
    particulas[:, t] = particulas[indices_remuestreo, t]

# Visualización de la trayectoria estimada
plt.plot(np.arange(0, tiempo_total, dt), np.mean(particulas, axis=0), label='Trayectoria Estimada', color='b')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtrado de Particulas para Estimacion de Trayectoria')
plt.legend()
plt.grid(True)
plt.show()
