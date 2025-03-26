import numpy as np
from scipy.stats import multivariate_normal

# Datos de entrada (mezcla de dos distribuciones gaussianas)
np.random.seed(0)
n_muestras = 1000
media1 = [1, 1]
covarianza1 = [[1, 0.5], [0.5, 1]]
media2 = [4, 4]
covarianza2 = [[1, -0.5], [-0.5, 1]]

datos = np.concatenate([np.random.multivariate_normal(media1, covarianza1, n_muestras // 2),
                        np.random.multivariate_normal(media2, covarianza2, n_muestras // 2)])

# Inicialización de parámetros
media_inicial = np.array([[0, 0], [3, 3]])
covarianza_inicial = np.array([[[1, 0], [0, 1]], [[1, 0], [0, 1]]])
pesos_iniciales = np.array([0.5, 0.5])

# Función para el paso de Expectation (E)
def paso_expectation(datos, medias, covarianzas, pesos):
    n_muestras = len(datos)
    n_componentes = len(pesos)
    likelihoods = np.zeros((n_muestras, n_componentes))
    
    for i in range(n_componentes):
        likelihoods[:, i] = multivariate_normal.pdf(datos, mean=medias[i], cov=covarianzas[i])
    
    likelihoods_pesadas = likelihoods * pesos
    suma_likelihoods_pesadas = np.sum(likelihoods_pesadas, axis=1)
    responsabilidades = likelihoods_pesadas / suma_likelihoods_pesadas[:, np.newaxis]
    
    return responsabilidades

# Función para el paso de Maximization (M)
def paso_maximization(datos, responsabilidades):
    suma_responsabilidades = np.sum(responsabilidades, axis=0)
    pesos = suma_responsabilidades / len(datos)
    
    medias = np.dot(responsabilidades.T, datos) / suma_responsabilidades[:, np.newaxis]
    
    covarianzas = np.zeros((len(pesos), datos.shape[1], datos.shape[1]))
    for i in range(len(pesos)):
        diff = datos - medias[i]
        covarianzas[i] = np.dot(responsabilidades[:, i] * diff.T, diff) / suma_responsabilidades[i]
    
    return pesos, medias, covarianzas

# Función EM
def algoritmo_EM(datos, medias_iniciales, covarianzas_iniciales, pesos_iniciales, n_iteraciones):
    medias = medias_iniciales
    covarianzas = covarianzas_iniciales
    pesos = pesos_iniciales
    
    for _ in range(n_iteraciones):
        responsabilidades = paso_expectation(datos, medias, covarianzas, pesos)
        pesos, medias, covarianzas = paso_maximization(datos, responsabilidades)
    
    return pesos, medias, covarianzas

# Ejecución del algoritmo EM
pesos_estimados, medias_estimadas, covarianzas_estimadas = algoritmo_EM(datos, media_inicial, covarianza_inicial, pesos_iniciales, n_iteraciones=100)

print("Pesos estimados:", pesos_estimados)
print("Medias estimadas:", medias_estimadas)
print("Covarianzas estimadas:", covarianzas_estimadas)
