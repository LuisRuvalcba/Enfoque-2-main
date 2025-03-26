import cv2

# Cargar una imagen en escala de grises
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar umbralizado adaptativo
umbralizado = cv2.adaptiveThreshold(imagen, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Mostrar la imagen original y la imagen umbralizada
cv2.imshow('Imagen original', imagen)
cv2.imshow('Umbralizado adaptativo', umbralizado)
cv2.waitKey(0)
cv2.destroyAllWindows()
