import cv2
import numpy as np

# Cargar una imagen
imagen = cv2.imread('imagen.jpg')
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar un umbral para obtener una imagen binaria
_, binaria = cv2.threshold(imagen_gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Aplicar la transformada de Watershed para segmentar la imagen
transformada = cv2.distanceTransform(binaria, cv2.DIST_L2, 5)
_, etiquetas = cv2.connectedComponents(binaria)
etiquetas = etiquetas + 1
etiquetas[binaria == 255] = 0

segmentos = cv2.watershed(imagen, etiquetas)

# Superponer los segmentos en la imagen original
imagen[segmentos == -1] = [0, 0, 255]

# Mostrar la imagen original con la segmentación
cv2.imshow('Segmentacion', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
