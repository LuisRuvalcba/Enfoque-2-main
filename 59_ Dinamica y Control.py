import numpy as np
import matplotlib.pyplot as plt

# Función para simular el movimiento del robot
def mover_robot(velocidad, dt):
    # Modelo de movimiento simple: el robot avanza a una velocidad constante
    nueva_posicion = velocidad * dt
    return nueva_posicion

# Función para el control de velocidad proporcional
def control_velocidad(objetivo, actual, kp):
    # Calculamos la señal de control proporcional
    señal_control = kp * (objetivo - actual)
    return señal_control

# Parámetros del controlador
kp = 0.5  # Ganancia proporcional

# Parámetros de simulación
velocidad_objetivo = 1.0  # Velocidad deseada
tiempo_simulacion = 10.0  # Tiempo de simulación en segundos
dt = 0.1  # Paso de tiempo

# Inicializamos el controlador y el estado del robot
velocidad_actual = 0.0  # Velocidad inicial del robot
tiempo = np.arange(0, tiempo_simulacion, dt)
posiciones = []

# Simulamos el control de velocidad y el movimiento del robot
for t in tiempo:
    señal_control = control_velocidad(velocidad_objetivo, velocidad_actual, kp)
    velocidad_actual += señal_control * dt
    nueva_posicion = mover_robot(velocidad_actual, dt)
    posiciones.append(nueva_posicion)

# Visualizamos los resultados
plt.plot(tiempo, posiciones)
plt.xlabel('Tiempo (s)')
plt.ylabel('Posicion del Robot')
plt.title('Control de Velocidad Proporcional para un Robot Movil')
plt.grid(True)
plt.show()
