import cv2
import numpy as np

# Cargar una imagen en escala de grises
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar detección de bordes usando Canny
bordes = cv2.Canny(imagen, 50, 150, apertureSize=3)

# Aplicar la transformada de Hough para detectar líneas
lineas = cv2.HoughLines(bordes, 1, np.pi/180, 200)

# Dibujar las líneas detectadas en la imagen original
for linea in lineas:
    rho, theta = linea[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(imagen, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Mostrar la imagen con las líneas detectadas
cv2.imshow('Lineas detectadas', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
