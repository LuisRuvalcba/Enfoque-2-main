import numpy as np

# Definición de los dígitos a reconocer y los fonemas que los componen
digitos = ['uno', 'dos', 'tres']
fonemas = {
    'uno': ['u', 'n', 'o'],
    'dos': ['d', 'o', 's'],
    'tres': ['t', 'r', 'e', 's']
}

# Definición de las probabilidades iniciales de los dígitos
pi = {
    'uno': 1/3,
    'dos': 1/3,
    'tres': 1/3
}

# Matrices de transición entre fonemas
A = np.array([
    [0.7, 0.2, 0.1],
    [0.1, 0.7, 0.2],
    [0.2, 0.1, 0.7],
    [0.3, 0.3, 0.4]
])

# Matrices de emisión de fonemas para cada dígito
B = {
    'uno': np.array([
        [0.1, 0.7, 0.2],
        [0.2, 0.1, 0.7],
        [0.2, 0.1, 0.7]
    ]),
    'dos': np.array([
        [0.2, 0.1, 0.7],
        [0.2, 0.1, 0.7],
        [0.7, 0.2, 0.1]
    ]),
    'tres': np.array([
        [0.2, 0.1, 0.7],
        [0.1, 0.7, 0.2],
        [0.1, 0.7, 0.2],
        [0.2, 0.1, 0.7]
    ])
}

# Función para calcular la probabilidad de un dígito dada una secuencia de fonemas
def probabilidad_digito(secuencia_fonemas, digito):
    probabilidad = pi[digito]
    for i in range(len(secuencia_fonemas)):
        probabilidad *= B[digito][i][fonemas[digito].index(secuencia_fonemas[i])]
    return probabilidad

# Secuencia de fonemas de entrada
secuencia_entrada = ['u', 'n', 'o']

# Reconocimiento del dígito hablado
probabilidades = {digito: probabilidad_digito(secuencia_entrada, digito) for digito in digitos}
digito_reconocido = max(probabilidades, key=probabilidades.get)

print("Secuencia de Fonemas de Entrada:", secuencia_entrada)
print("Digito Reconocido:", digito_reconocido)
print("Probabilidad:", probabilidades[digito_reconocido])
