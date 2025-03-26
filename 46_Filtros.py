import cv2
import numpy as np

# Cargar una imagen
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar un filtro Laplaciano para resaltar los bordes
filtro_laplaciano = cv2.Laplacian(imagen, cv2.CV_64F)

# Convertir la imagen de vuelta a valores de píxeles en el rango de 0 a 255
filtro_laplaciano = np.uint8(np.absolute(filtro_laplaciano))

# Mostrar la imagen original y la imagen con los bordes resaltados
cv2.imshow('Imagen original', imagen)
cv2.imshow('Bordes resaltados', filtro_laplaciano)
cv2.waitKey(0)
cv2.destroyAllWindows()
