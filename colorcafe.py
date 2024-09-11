import cv2
import numpy as np

# Función para definir el rango de color café en el espacio HSV
def detectar_cafe(frame):
    # Convertir la imagen de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir los rangos de color café en HSV
    cafe_bajo = np.array([10, 100, 20])
    cafe_alto = np.array([20, 255, 200])

    # Crear máscara para detectar el color café
    mascara_cafe = cv2.inRange(hsv, cafe_bajo, cafe_alto)

    return mascara_cafe

# Captura de video desde la webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo leer el fotograma.")
        break

    # Detectar el color café en el fotograma
    mascara_cafe = detectar_cafe(frame)

    # Aplicar la máscara al fotograma original
    resultado = cv2.bitwise_and(frame, frame, mask=mascara_cafe)

    # Mostrar el fotograma original y el resultado
    cv2.imshow('Fotograma Original', frame)
    cv2.imshow('Detección de Color Café', resultado)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
