simport numpy as np
import matplotlib.pyplot as plt

# Función para simular el movimiento del robot (odometría)
def mover_robot(posicion_anterior, distancia, angulo):
    x_prev, y_prev, theta_prev = posicion_anterior
    x_nuevo = x_prev + distancia * np.cos(theta_prev + angulo)
    y_nuevo = y_prev + distancia * np.sin(theta_prev + angulo)
    theta_nuevo = theta_prev + angulo
    return x_nuevo, y_nuevo, theta_nuevo

# Función para simular la observación del entorno (datos del sensor)
def observar_entorno(posicion_actual, rango_maximo):
    x, y, _ = posicion_actual
    # Simular datos del sensor (distancia a obstáculos)
    distancia = np.sqrt(x ** 2 + y ** 2) + np.random.normal(0, 0.1)
    return min(distancia, rango_maximo)

# Algoritmo SLAM básico para generar un mapa 2D
def slam_2d(num_pasos, distancia_avance, angulo_giro, rango_maximo):
    mapa = []
    posicion_actual = (0, 0, 0)  # Iniciar en el origen
    for _ in range(num_pasos):
        # Movimiento del robot (odometría)
        posicion_actual = mover_robot(posicion_actual, distancia_avance, angulo_giro)
        # Observación del entorno (datos del sensor)
        distancia_medida = observar_entorno(posicion_actual, rango_maximo)
        mapa.append((posicion_actual[0], posicion_actual[1], distancia_medida))
    return mapa

# Parámetros
num_pasos = 100
distancia_avance = 0.1
angulo_giro = np.pi / 12
rango_maximo = 5

# Generar el mapa utilizando SLAM
mapa_generado = slam_2d(num_pasos, distancia_avance, angulo_giro, rango_maximo)

# Mostrar el mapa generado
plt.figure(figsize=(8, 6))
for punto in mapa_generado:
    plt.scatter(punto[0], punto[1], c='b', marker='.')
plt.title('Mapa 2D generado con SLAM')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
