import math

#Creamos nuestro seguidor de objetos
class Rastreador: 
    #Inicializacion de variables
    def __init__(self):
        #Almacenamiento de posiciones centrales de los objetos
        self.centro_puntos = {}
        #Contador de objetos
        self.id_count = 1

    def rastreo(self,objetos):
        #Almacenamiento de objetos identificados
        objetos_id = []

        #Obtención del punto central del objeto
        for rect in objetos:
            x, y, w, h = rect
            cx = ( x + x + w ) // 2
            cy = ( y + y + h ) // 2

            #Comprobamos si el objeto ya ha sido detectado
            objeto_det = False
            for id, pt in self.centro_puntos.items():
                dist = math.hypot( cx - pt[0], cy - pt[1])

                if dist < 25:
                    self.centro_puntos[id] = (cx, cy)
                    print(self.centro_puntos)
                    objetos_id.append([x, y, w, h, id])
                    objeto_det = True
                    break 

            #Si detecta un nuevo objeto, se le asigna un ID
            if objeto_det is False:
                #Almacenamos las coordenadas 
                self.centro_puntos[self.id_count] = (cx, cy)
                #Unimos objeto con su ID
                objetos_id.append([x, y, w, h, self.id_count])
                #Aumentamos el ID
                self.id_count = self.id_count + 1

        #Limpiar la lista de los IDs que ya no se usan
        new_center_points = {}
        for obj_bb_id in objetos_id:
            _, _, _, _, object_id = obj_bb_id
            center = self.centro_puntos[object_id]
            new_center_points[object_id] = center

        #Actualizar la lista con los ID eliminados
        self.centro_puntos = new_center_points.copy()
        return objetos_id