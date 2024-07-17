import cv2
from ultralytics import YOLO
import os 

# Cargar el modelo preentrenado de YOLOv8n
model_path = os.path.join('C:/Users/inesb/Desktop/YOLO/YOLOv8/runs/detect/train/weights','last.pt')
model = YOLO(model_path)

# Iniciar la captura de video desde la cámara del ordenador
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se puede acceder a la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se puede recibir el frame (el flujo de video se ha terminado?). Saliendo...")
        break

    # Realizar detección de objetos en el frame
    results = model(frame)

    # Dibujar las detecciones en el frame
    annotated_frame = results[0].plot()

    # Mostrar el frame anotado
    cv2.imshow('Detección en Tiempo Real', annotated_frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
