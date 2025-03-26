sfrom hmmlearn import hmm

# Definimos el modelo HMM
modelo_hmm = hmm.MultinomialHMM(n_components=2)

# Secuencia de observaciones de muestra
secuencia_observada = [[0, 1, 0, 1, 0],  # Secuencia de observaciones para la primera muestra
                       [1, 0, 1, 0, 1]]  # Secuencia de observaciones para la segunda muestra

# Ajustamos el modelo HMM con las secuencias observadas
modelo_hmm.fit(secuencia_observada)

# Realizamos inferencia para estimar la secuencia de estados ocultos
secuencia_estados_ocultos = modelo_hmm.predict(secuencia_observada)

print("Secuencia de estados ocultos estimada para la primera muestra:", secuencia_estados_ocultos[0])
print("Secuencia de estados ocultos estimada para la segunda muestra:", secuencia_estados_ocultos[1])
