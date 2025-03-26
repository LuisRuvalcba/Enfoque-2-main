import numpy as np

class Perceptron:
    def __init__(self, n_entradas, tasa_aprendizaje=0.1, epocas=100):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = np.zeros(n_entradas + 1)  # +1 para el sesgo

    def funcion_activacion(self, entrada):
        return 1 if entrada >= 0 else 0

    def predict(self, entrada):
        suma = np.dot(entrada, self.pesos[1:]) + self.pesos[0]
        return self.funcion_activacion(suma)

    def entrenar(self, X, y):
        for _ in range(self.epocas):
            for entrada, etiqueta in zip(X, y):
                prediccion = self.predict(entrada)
                self.pesos[1:] += self.tasa_aprendizaje * (etiqueta - prediccion) * entrada
                self.pesos[0] += self.tasa_aprendizaje * (etiqueta - prediccion)
