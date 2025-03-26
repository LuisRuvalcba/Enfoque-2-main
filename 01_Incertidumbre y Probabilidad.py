import random

# Función para simular el lanzamiento de una moneda
def lanzamiento_moneda():
    # Generamos un número aleatorio entre 0 y 1
    resultado = random.randint(0, 1)
    # Si es 0, consideramos cara. Si es 1, consideramos cruz.
    if resultado == 0:
        return 'cara'
    else:
        return 'cruz'

# Número de lanzamientos
num_lanzamientos = 1000
# Contadores para cara y cruz
cara_count = 0
cruz_count = 0

# Simulamos los lanzamientos y contamos las caras y las cruces
for _ in range(num_lanzamientos):
    resultado = lanzamiento_moneda()
    if resultado == 'cara':
        cara_count += 1
    else:
        cruz_count += 1

# Calculamos las probabilidades
probabilidad_cara = cara_count / num_lanzamientos
probabilidad_cruz = cruz_count / num_lanzamientos

# Imprimimos los resultados
print(f'Probabilidad de obtener cara: {probabilidad_cara}')
print(f'Probabilidad de obtener cruz: {probabilidad_cruz}')

