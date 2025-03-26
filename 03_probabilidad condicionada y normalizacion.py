# Probabilidades
prob_aprobar = 0.7
prob_estudiar = 0.6
prob_aprobar_dado_estudiar = 0.8

# Calculamos la probabilidad condicionada usando la fórmula de Bayes
prob_estudiar_dado_aprobar = (prob_aprobar_dado_estudiar * prob_estudiar) / prob_aprobar

print(f"La probabilidad de que un estudiante haya estudiado dado que aprueba es: {prob_estudiar_dado_aprobar}")
