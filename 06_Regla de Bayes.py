# Probabilidades
prob_enfermedad = 0.01  # Probabilidad de tener la enfermedad (1%)
prob_positivo_dado_enfermedad = 0.9  # Probabilidad de obtener un resultado positivo en la prueba si se tiene la enfermedad (90%)
prob_negativo_dado_no_enfermedad = 0.95  # Probabilidad de obtener un resultado negativo en la prueba si no se tiene la enfermedad (95%)

# Función para calcular la probabilidad condicional utilizando la Regla de Bayes
def prob_enfermedad_dado_positivo(prob_enfermedad, prob_positivo_dado_enfermedad, prob_negativo_dado_no_enfermedad):
    prob_no_enfermedad = 1 - prob_enfermedad
    prob_positivo = (prob_enfermedad * prob_positivo_dado_enfermedad) + (prob_no_enfermedad * (1 - prob_negativo_dado_no_enfermedad))
    return (prob_enfermedad * prob_positivo_dado_enfermedad) / prob_positivo

# Calculamos la probabilidad de tener la enfermedad dado un resultado positivo
probabilidad = prob_enfermedad_dado_positivo(prob_enfermedad, prob_positivo_dado_enfermedad, prob_negativo_dado_no_enfermedad)

print("La probabilidad de tener la enfermedad dado un resultado positivo en la prueba es:", probabilidad)
