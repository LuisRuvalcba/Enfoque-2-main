import numpy as np
import matplotlib.pyplot as plt

# Función para calcular las trayectorias posibles del robot en función de sus velocidades
def calcular_trayectorias(velocidad_lineal, velocidad_angular):
    # Definir los valores de tiempo
    t = np.linspace(0, 2*np.pi, 100)
    # Calcular las trayectorias en función de las velocidades
    x = velocidad_lineal * np.cos(velocidad_angular * t)
    y = velocidad_lineal * np.sin(velocidad_angular * t)
    return x, y

# Velocidades lineales y angulares para explorar el espacio de configuración
velocidades_lineales = [1, 2, 1.5]
velocidades_angulares = [0.5, 1, 1.5]

# Crear un gráfico para mostrar las trayectorias en el espacio de configuración
plt.figure(figsize=(10, 8))
for v_lineal in velocidades_lineales:
    for v_angular in velocidades_angulares:
        x, y = calcular_trayectorias(v_lineal, v_angular)
        plt.plot(x, y, label=f'V_lin={v_lineal}, V_ang={v_angular}')
plt.title('Espacio de Configuracion para un Robot Movil de Dos Ruedas')
plt.xlabel('Posición en X')
plt.ylabel('Posición en Y')
plt.legend()
plt.grid(True)
plt.show()
