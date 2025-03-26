import numpy as np

# Simulamos el lanzamiento de dos monedas
num_experimentos = 10000
lanzamiento_1 = np.random.randint(0, 2, size=num_experimentos)  # 0 representa cara, 1 representa cruz
lanzamiento_2 = np.random.randint(0, 2, size=num_experimentos)

# Contamos la cantidad de veces que se obtuvo cara en ambos lanzamientos
cara_en_ambos = np.sum((lanzamiento_1 == 0) & (lanzamiento_2 == 0))

# Calculamos las probabilidades de cada evento
prob_cara_1 = np.sum(lanzamiento_1 == 0) / num_experimentos
prob_cara_2 = np.sum(lanzamiento_2 == 0) / num_experimentos
prob_cara_en_ambos = cara_en_ambos / num_experimentos

# Verificamos si los eventos son independientes
independencia_condicional = prob_cara_en_ambos == prob_cara_1 * prob_cara_2

print("Probabilidad de obtener cara en el primer lanzamiento:", prob_cara_1)
print("Probabilidad de obtener cara en el segundo lanzamiento:", prob_cara_2)
print("Probabilidad de obtener cara en ambos lanzamientos:", prob_cara_en_ambos)
print("Los eventos son independientes?:", independencia_condicional)
