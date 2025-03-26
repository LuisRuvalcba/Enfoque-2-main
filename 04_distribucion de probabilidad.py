import numpy as np

# Simulación del lanzamiento del dado
lanzamientos = np.random.randint(1, 7, size=1000)

# Calculamos la frecuencia de cada resultado
frecuencia = {i: np.sum(lanzamientos == i) for i in range(1, 7)}

# Calculamos la probabilidad de cada resultado
probabilidad = {k: v / len(lanzamientos) for k, v in frecuencia.items()}

print("Distribucion de probabilidad del dado:")
for num, prob in probabilidad.items():
    print(f"Numero: {num}, Probabilidad: {prob}")
