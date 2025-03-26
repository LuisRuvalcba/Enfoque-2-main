import numpy as np

# Definición de parámetros del HMM
estados_ocultos = ['Soleado', 'Nublado', 'Lluvioso']
simbolos = ['Paseo', 'Gimnasio', 'Cine']
pi = np.array([0.6, 0.2, 0.2])  # Probabilidades iniciales de los estados ocultos
A = np.array([[0.7, 0.2, 0.1],   # Matriz de transición de estados ocultos
              [0.3, 0.5, 0.2],
              [0.2, 0.3, 0.5]])
B = np.array([[0.6, 0.2, 0.2],   # Matriz de emisión
              [0.1, 0.7, 0.2],
              [0.2, 0.3, 0.5]])

# Función para estimar la secuencia de estados ocultos más probable utilizando el algoritmo de Viterbi
def viterbi(observaciones):
    longitud = len(observaciones)
    num_estados = len(estados_ocultos)
    T1 = np.zeros((num_estados, longitud))
    T2 = np.zeros((num_estados, longitud), dtype=int)

    # Paso inicial
    T1[:, 0] = pi * B[:, simbolos.index(observaciones[0])]

    # Pasos recursivos
    for t in range(1, longitud):
        for j in range(num_estados):
            T1[j, t] = np.max(T1[:, t-1] * A[:, j]) * B[j, simbolos.index(observaciones[t])]
            T2[j, t] = np.argmax(T1[:, t-1] * A[:, j])

    # Paso final
    estado_final = np.argmax(T1[:, -1])
    secuencia_estados = [estado_final]
    for t in range(longitud - 1, 0, -1):
        estado_final = T2[estado_final, t]
        secuencia_estados.insert(0, estado_final)
    return secuencia_estados

# Secuencia de observaciones dada
observaciones = ['Paseo', 'Gimnasio', 'Cine', 'Gimnasio', 'Cine']
# Estimación de la secuencia de estados ocultos más probable
secuencia_estados_estimada = [estados_ocultos[i] for i in viterbi(observaciones)]
print("Secuencia de Estados Ocultos Estimada:", secuencia_estados_estimada)
