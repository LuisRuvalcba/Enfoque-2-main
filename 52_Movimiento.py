import cv2

# Capturar el video desde la cámara
cap = cv2.VideoCapture(0)

# Leer la primera imagen
ret, frame1 = cap.read()

while True:
    # Leer la siguiente imagen
    ret, frame2 = cap.read()
    
    # Calcular la diferencia absoluta entre las dos imágenes
    diff = cv2.absdiff(frame1, frame2)
    
    # Convertir la diferencia a escala de grises
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # Aplicar un umbral para obtener una máscara de movimiento
    _, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    
    # Mostrar la máscara de movimiento
    cv2.imshow('Deteccion de movimiento', thresh)
    
    # Actualizar la imagen anterior
    frame1 = frame2
    
    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
