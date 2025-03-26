import numpy as np

# Datos observados
datos = np.array([1.2, 2.5, 1.8, 3.3, 2.1])

# Función para calcular la verosimilitud de los parámetros dados los datos
def verosimilitud(media, desviacion):
    probabilidad_datos = np.prod(1 / (np.sqrt(2 * np.pi) * desviacion) * np.exp(-(datos - media) ** 2 / (2 * desviacion ** 2)))
    return probabilidad_datos

# Definimos una cuadrícula de posibles valores para la media y la desviación estándar
medias = np.linspace(0, 4, 100)
desviaciones = np.linspace(0.1, 2, 100)

# Calculamos la verosimilitud para cada combinación de media y desviación
verosimilitudes = np.array([[verosimilitud(media, desviacion) for media in medias] for desviacion in desviaciones])

# Normalizamos las verosimilitudes para obtener una distribución de probabilidad
verosimilitudes_normalizadas = verosimilitudes / np.sum(verosimilitudes)

# Graficamos la distribución de verosimilitud
import matplotlib.pyplot as plt
plt.imshow(verosimilitudes_normalizadas, extent=[0, 4, 0.1, 2], origin='lower', aspect='auto')
plt.xlabel('Media')
plt.ylabel('Desviacion Estandar')
plt.title('Ponderacion de Verosimilitud para una Distribucion Normal')
plt.colorbar(label='Densidad de Verosimilitud')
plt.show()
