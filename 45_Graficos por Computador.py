import cv2
import numpy as np

# Cargar una imagen
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Detectar esquinas usando el algoritmo de Harris
dst = cv2.cornerHarris(imagen, 2, 3, 0.04)

# Dilatar los puntos detectados para mostrarlos mejor
dst = cv2.dilate(dst, None)

# Marcar los puntos detectados en la imagen original
imagen[dst > 0.01 * dst.max()] = [0, 0, 255]

# Mostrar la imagen original con las esquinas detectadas
cv2.imshow('Esquinas detectadas', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
