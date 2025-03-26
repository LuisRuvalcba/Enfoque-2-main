from hmmlearn import hmm

# Definimos el modelo HMM
modelo_hmm = hmm.MultinomialHMM(n_components=2)

# Secuencia de palabras de muestra (vector de características)
secuencia = [[0, 1, 0, 1, 0],  # Ejemplo de texto positivo
             [1, 0, 1, 0, 1]]  # Ejemplo de texto negativo

# Entrenamos el modelo HMM con la secuencia de palabras
modelo_hmm.fit(secuencia)

# Clasificamos nuevas secuencias de palabras
nueva_secuencia = [[0, 1, 0, 1, 0, 1],  # Nueva secuencia de texto (positivo)
                   [1, 0, 1, 0, 1, 0]]  # Nueva secuencia de texto (negativo)
predicciones = modelo_hmm.predict(nueva_secuencia)

# Mostramos las predicciones
for i, prediccion in enumerate(predicciones):
    categoria = "positivo" if prediccion == 0 else "negativo"
    print(f"Nueva secuencia {i+1} clasificada como: {categoria}")
