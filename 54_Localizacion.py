import numpy as np

# Definir la función de movimiento del robot
def mover_robot(posicion_anterior, distancia, angulo):
    x_prev, y_prev = posicion_anterior
    x_nuevo = x_prev + distancia * np.cos(angulo)
    y_nuevo = y_prev + distancia * np.sin(angulo)
    return x_nuevo, y_nuevo

# Definir la función de observación (simulada)
def observar(distancia_real, distancia_medida, desviacion):
    prob = 1.0 / (desviacion * np.sqrt(2 * np.pi)) * \
           np.exp(-0.5 * ((distancia_real - distancia_medida) / desviacion) ** 2)
    return prob

# Algoritmo de Monte Carlo para localización
def localizar_particulas(num_particulas, num_pasos, distancia_medida, desviacion_observacion):
    # Generar partículas aleatorias
    particulas = np.random.rand(num_particulas, 2) * 10  # Espacio 2D de 10x10 unidades
    for _ in range(num_pasos):
        # Mover el robot (simulado)
        distancia_real = np.random.normal(1, 0.2)  # Distancia real con ruido
        angulo = np.random.uniform(0, 2*np.pi)  # Ángulo de giro aleatorio
        for i in range(num_particulas):
            particulas[i] = mover_robot(particulas[i], distancia_real, angulo)
        # Actualizar pesos basados en la observación
        for i in range(num_particulas):
            distancia_medida_simulada = np.linalg.norm(particulas[i] - [5, 5])  # Distancia al punto central
            particulas[i, 2] = observar(distancia_real, distancia_medida_simulada, desviacion_observacion)
        # Normalizar los pesos
        particulas[:, 2] /= np.sum(particulas[:, 2])
        # Resamplear partículas
        indices = np.random.choice(num_particulas, num_particulas, p=particulas[:, 2])
        particulas = particulas[indices]
    return particulas

# Parámetros
num_particulas = 1000
num_pasos = 10
distancia_medida = 4.5  # Distancia medida desde el punto central
desviacion_observacion = 0.1  # Desviación estándar de la observación (ruido)

# Localizar el robot
particulas_localizadas = localizar_particulas(num_particulas, num_pasos, distancia_medida, desviacion_observacion)

# Mostrar la ubicación estimada del robot
ubicacion_estimada = np.mean(particulas_localizadas[:, :2], axis=0)
print("Ubicacion estimada del robot:", ubicacion_estimada)
