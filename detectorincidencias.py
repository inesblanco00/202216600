import cv2
from Rastreador import *

# Objeto de seguimiento
seguimiento = Rastreador()

# Lectura del video
cap = cv2.VideoCapture('RoboPersonas.mp4')

# Importante la cámara debe estar estática
# Extraemos los objetos en movimiento de una cámara estable
deteccion = cv2.createBackgroundSubtractorMOG2(history=10000, varThreshold=20)
# Es un substractor de fondo (deja el fondo en negro y los objetos en mvto en blanco)
while True:
    ret, frame = cap.read()

    # Redimensionamos el video
    #frame = cv2.resize(frame,(1280,720))
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    #Creamos una mascara para que los objetos sean blancos y el fondo negro
    mascara = deteccion.apply(frame)
    #Eliminamos los pixeles grises
    _, mascara = cv2.threshold(mascara, 254, 255, cv2.THRESH_BINARY)
    #Detectamos el contorno de los objetos
    contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Lista donde almacenar la info
    detecciones = []

    # Dibujamos los contornos
    for cont in contornos:
        # Eliminamos los contornos pequeños
         area = cv2.contourArea(cont)
         # if area > 20 and area < 50: #Si el area es mayor a 50 pixeles
         if area > 100: #Si el area es mayor a 50 pixeles
              x, y, ancho, alto = cv2.boundingRect(cont)
              # Dibujamos el rectangulo
              cv2.rectangle(frame, (x, y), (x + ancho, y + alto), (255,255,0), 3)
              # Almacenamos la info de las detecciones
              detecciones.append([x, y, ancho, alto])

   # print(detecciones)    
    # Seguimiento de objetos
  #  info_id = seguimiento.rastreo(detecciones)          

   # for inf in info_id:
    #     x, y, ancho, alto, id = inf
         # Escribimos el ID
     #    cv2.putText(frame,str(id), (x, y -15), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 2)
         # Dibujamos el rectangulo
      #   cv2.rectangle(frame, (x, y), (x + ancho, y + alto), (255,255,0), 3)


   # print(info_id)

    cv2.imshow("Video", frame)
    cv2.imshow("Mascara", mascara)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
