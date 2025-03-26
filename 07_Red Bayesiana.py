from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura de la red bayesiana
modelo = BayesianNetwork([('Enfermedad', 'Sintomas'), ('Sintomas', 'Resultado')])

# Definimos las probabilidades condicionales
cpd_enfermedad = TabularCPD(variable='Enfermedad', variable_card=2, values=[[0.01], [0.99]])
cpd_sintomas = TabularCPD(variable='Síntomas', variable_card=2, values=[[0.95, 0.2], [0.05, 0.8]], evidence=['Enfermedad'], evidence_card=[2])
cpd_resultado = TabularCPD(variable='Resultado', variable_card=2, values=[[0.9, 0.2], [0.1, 0.8]], evidence=['Síntomas'], evidence_card=[2])

# Asociamos las probabilidades condicionales con el modelo
modelo.add_cpds(cpd_enfermedad, cpd_sintomas, cpd_resultado)

# Verificamos la validez del modelo
print("Es valido el modelo?:", modelo.check_model())

# Realizamos inferencia utilizando Variable Elimination
inference = VariableElimination(modelo)

# Calculamos la probabilidad de tener la enfermedad dado los síntomas observados
resultado = inference.query(variables=['Enfermedad'], evidence={'Síntomas': 1})['Enfermedad']
print("Probabilidad de tener la enfermedad dado los sintomas observados:", resultado.values)
