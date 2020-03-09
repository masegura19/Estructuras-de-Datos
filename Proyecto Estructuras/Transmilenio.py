import xml.etree.ElementTree as ET
archivo_xml = ET.parse('Trasmi.xml')
troncal = archivo_xml.getroot()

class estacion:
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.anterior = None
        self.siguiente = None
class Lista():
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0
    def agregarEstacion(self, nombre, latitud, longitud):
        nuevaEstacion = estacion(nombre, latitud, longitud)
        if self.cabeza is None:
            self.cabeza = nuevaEstacion
            self.cola = self.cabeza
        else:
            self.cola.siguiente =nuevaEstacion
            nuevaEstacion.anterior = self.cola
            self.cola = nuevaEstacion
        self.size +=1
    def imprimirLista(self):
        estacionactual = self.cabeza
        for i in range(self.size):
            print("Estacion", estacionactual.nombre)
            estacionactual = estacionactual.siguiente

objeto = Lista()

from xml.dom import minidom
solicitar_Trasmi = minidom.parse('Trasmi.xml')

i = -1
for x in troncal:
    for y in x:
            i += 1
            p1 = solicitar_Trasmi.getElementsByTagName("nombre")[i]
            p1 = p1.firstChild.data
            p2 = solicitar_Trasmi.getElementsByTagName("Latitud")[i]
            p2 = p2.firstChild.data
            p3 = solicitar_Trasmi.getElementsByTagName("Longitud")[i]
            p3 = p3.firstChild.data
            objeto.agregarEstacion(p1, p2, p3)
objeto.imprimirLista()

# PEDIR LAS ESTACIONES #
solicitar_user1 = int(input("Introdusca el numero de la estacion A: "))
Dato1 = solicitar_Trasmi.getElementsByTagName("nombre")[solicitar_user1-1]
print("A:", Dato1.firstChild.data)
solicitar_user2 = int(input("Introdusca el numero de la estacion B: "))
Dato2 = solicitar_Trasmi.getElementsByTagName("nombre")[solicitar_user2-1]
print("B:", Dato2.firstChild.data)


lat11 = solicitar_Trasmi.getElementsByTagName("Latitud")[solicitar_user1-1]
lon11 = solicitar_Trasmi.getElementsByTagName("Longitud")[solicitar_user1-1]
lat22 = solicitar_Trasmi.getElementsByTagName("Latitud")[solicitar_user2-1]
lon22 = solicitar_Trasmi.getElementsByTagName("Longitud")[solicitar_user2-1]

lat1 = float(lat11.firstChild.data)
lat2 = float(lat22.firstChild.data)
lon1 = float(lon11.firstChild.data)
lon2 = float(lon22.firstChild.data)

import math
# CALCULAR LA DISTANCIA APROXIMADA#
rad = math.pi / 180
distancia1 = (lat2 - lat1)
distancia2 = (lon2 - lon1)
R = 6372.795477598
a = (math.sin(rad * distancia1 / 2)) **2 + math.cos(rad * lat1) * math.cos(rad * lat2) * (math.sin(rad * distancia2 / 2)) **2
dis = 2 * R * math.asin(math.sqrt(a))



#CALCULAR DISTANCIAS ENTRE ESTACIONES
d01 = solicitar_user1 -1
d02 = solicitar_user2 -1
d1 = int(d01)
d2 = int(d02-1)
pp = 0
while d1 <= d2:
    lat01 = solicitar_Trasmi.getElementsByTagName("Latitud")[d1]
    lon01 = solicitar_Trasmi.getElementsByTagName("Longitud")[d1]
    lat02 = solicitar_Trasmi.getElementsByTagName("Latitud")[d1+1]
    lon02 = solicitar_Trasmi.getElementsByTagName("Longitud")[d1+1]

    Dato001 = solicitar_Trasmi.getElementsByTagName("nombre")[d1]
    Dato002 = solicitar_Trasmi.getElementsByTagName("nombre")[d1+1]

    lat011 = float(lat01.firstChild.data)
    lat022 = float(lat02.firstChild.data)
    lon011 = float(lon01.firstChild.data)
    lon022 = float(lon02.firstChild.data)

    distancia01 = (lat022 - lat011)
    distancia02 = (lon022 - lon011)
    b = (math.sin(rad * distancia01 / 2)) **2 + math.cos(rad * lat011) * math.cos(rad * lat022) * (math.sin(rad * distancia02 / 2)) **2
    dis01 = 2 * R * math.asin(math.sqrt(b))
    print("La distancia entre estaciones ",Dato001.firstChild.data,"y",  Dato002.firstChild.data, " es", dis01, "km")
    #print("La suma de las distancias es:", pp, "km")
    pp = dis01 + pp
    d1 = d1 + 1
print("\n")
print("La distancia de punto a punto es:", dis, "km")
print("La distancia del recorrido de estaciones entre", Dato1.firstChild.data, "y", Dato2.firstChild.data, "es de ", pp, "km")



