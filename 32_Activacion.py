# Importamos las bibliotecas necesarias
import numpy as np

# Definimos la función de activación ReLU
def relu(x):
    return np.maximum(0, x)

# Creamos una red neuronal simple con una sola capa oculta
def red_neuronal_simple(x):
    # Pesos y sesgos para la capa oculta
    pesos_oculta = np.array([[0.1, 0.2, 0.3],
                              [0.4, 0.5, 0.6]])
    sesgo_oculta = np.array([0.1, 0.2, 0.3])

    # Pesos y sesgo para la capa de salida
    pesos_salida = np.array([[0.4], [0.5], [0.6]])
    sesgo_salida = np.array([0.4])

    # Calculamos la salida de la capa oculta
    salida_oculta = np.dot(x, pesos_oculta) + sesgo_oculta
    activacion_oculta = relu(salida_oculta)  # Aplicamos la función de activación ReLU

    # Calculamos la salida de la red neuronal
    salida = np.dot(activacion_oculta, pesos_salida) + sesgo_salida

    return salida

# Entrada de ejemplo
entrada = np.array([1.0, 0.5])

# Obtenemos la salida de la red neuronal
salida_red = red_neuronal_simple(entrada)
print("Salida de la red neuronal:", salida_red)
