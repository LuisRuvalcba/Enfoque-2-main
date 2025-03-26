import numpy as np

# Función para calcular la cinemática inversa de un brazo robótico de 2 grados de libertad
def cinematica_inversa(x_objetivo, y_objetivo, l1, l2):
    # Calcular el ángulo de la primera articulación
    theta1 = np.arctan2(y_objetivo, x_objetivo)
    
    # Calcular la distancia desde la base del brazo hasta el punto objetivo
    distancia_objetivo = np.sqrt(x_objetivo**2 + y_objetivo**2)
    
    # Calcular el ángulo de la segunda articulación utilizando el teorema del coseno
    cos_theta2 = (l1**2 + l2**2 - distancia_objetivo**2) / (2 * l1 * l2)
    sin_theta2 = np.sqrt(1 - cos_theta2**2)
    theta2 = np.arctan2(sin_theta2, cos_theta2)
    
    # Devolver los ángulos calculados en radianes
    return theta1, theta2

# Parámetros del brazo robótico
longitud_l1 = 1.5
longitud_l2 = 1.0
posicion_objetivo_x = 1.0
posicion_objetivo_y = 1.0

# Calcular los ángulos de las articulaciones para alcanzar la posición objetivo
theta1, theta2 = cinematica_inversa(posicion_objetivo_x, posicion_objetivo_y, longitud_l1, longitud_l2)

# Mostrar los ángulos calculados
print("Angulo de la primera articulacion:", np.degrees(theta1))
print("Angulo de la segunda articulacion:", np.degrees(theta2))
