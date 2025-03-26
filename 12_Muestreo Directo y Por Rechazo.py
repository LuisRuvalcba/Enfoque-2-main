import numpy as np
import matplotlib.pyplot as plt

# Función de densidad de probabilidad (PDF) de la distribución objetivo (por ejemplo, una distribución normal)
def pdf_objetivo(x):
    return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

# Función de densidad de probabilidad (PDF) de la distribución de propuesta (por ejemplo, una distribución uniforme)
def pdf_propuesta(x):
    return 1 / 2  # Distribución uniforme en el rango [-1, 1]

# Función para generar muestras utilizando muestreo por rechazo
def muestreo_por_rechazo(num_muestras):
    muestras = []
    max_pdf = 1  # Máximo valor de la PDF de la distribución objetivo en el rango [-1, 1]
    for _ in range(num_muestras):
        aceptado = False
        while not aceptado:
            x = np.random.uniform(-1, 1)
            y = np.random.uniform(0, max_pdf)
            if y < pdf_objetivo(x) / pdf_propuesta(x):
                muestras.append(x)
                aceptado = True
    return muestras

# Generamos 1000 muestras utilizando muestreo por rechazo
muestras = muestreo_por_rechazo(1000)

# Graficamos las muestras
plt.hist(muestras, bins=30, density=True, alpha=0.6, color='g')
x = np.linspace(-3, 3, 100)
plt.plot(x, pdf_objetivo(x), color='r', linestyle='--', linewidth=2)
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.title('Muestreo por Rechazo')
plt.grid(True)
plt.show()
