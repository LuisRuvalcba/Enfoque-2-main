import cv2

# Cargar el clasificador en cascada de Haar para detección de rostros
cascada_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar una imagen
imagen = cv2.imread('imagen.jpg')

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar rostros en la imagen
rostros = cascada_rostros.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibujar rectángulos alrededor de los rostros detectados
for (x, y, w, h) in rostros:
    cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Mostrar la imagen con los rostros detectados
cv2.imshow('Deteccion de rostros', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
