from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura de la red bayesiana
modelo = BayesianNetwork([('A', 'B'), ('B', 'C')])

# Definimos las probabilidades condicionales
cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_B_dado_A = TabularCPD(variable='B', variable_card=2, values=[[0.8, 0.3], [0.2, 0.7]], evidence=['A'], evidence_card=[2])
cpd_C_dado_B = TabularCPD(variable='C', variable_card=2, values=[[0.9, 0.2], [0.1, 0.8]], evidence=['B'], evidence_card=[2])

# Asociamos las probabilidades condicionales con el modelo
modelo.add_cpds(cpd_A, cpd_B_dado_A, cpd_C_dado_B)

# Realizamos inferencia utilizando eliminación de variables
inference = VariableElimination(modelo)

# Calculamos la probabilidad de que A sea verdadero dado que C es verdadero
resultado = inference.query(variables=['A'], evidence={'C': 1}, elimination_order='MinFill')
print("Probabilidad de que A sea verdadero dado que C es verdadero:", resultado.values)
