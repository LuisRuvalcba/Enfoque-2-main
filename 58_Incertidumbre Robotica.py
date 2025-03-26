import numpy as np

# Función para actualizar la estimación utilizando el Filtro de Kalman
def filtro_kalman(estimacion_anterior, medicion, covarianza_proceso, covarianza_medicion):
    # Predicción
    prediccion_estado = estimacion_anterior
    prediccion_covarianza = covarianza_proceso + estimacion_anterior[2]
    
    # Corrección
    ganancia_kalman = prediccion_covarianza / (prediccion_covarianza + covarianza_medicion)
    nuevo_estado = prediccion_estado + ganancia_kalman * (medicion - prediccion_estado)
    nueva_covarianza = (1 - ganancia_kalman) * prediccion_covarianza
    
    return nuevo_estado, nueva_covarianza

# Parámetros del Filtro de Kalman
estimacion_inicial = np.array([0, 0, 0])  # Posición inicial y velocidad
covarianza_proceso = np.array([[0.1, 0, 0], [0, 0.1, 0], [0, 0, 0.1]])  # Covarianza del proceso (movimiento del robot)
covarianza_medicion = 0.1  # Covarianza de la medición (ruido en las mediciones)

# Mediciones de la posición del robot (simuladas)
mediciones = [1.2, 2.3, 3.4, 4.5]

# Estimación inicial
estado_estimado = estimacion_inicial
covarianza_estimada = covarianza_proceso

# Actualizar la estimación utilizando el Filtro de Kalman para cada medición
for medicion in mediciones:
    estado_estimado, covarianza_estimada = filtro_kalman(estado_estimado, medicion, covarianza_proceso, covarianza_medicion)
    print("Estimacion de posición:", estado_estimado[:2])
