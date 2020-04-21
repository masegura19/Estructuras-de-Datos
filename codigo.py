"Daniel Alejandro Pacheco Zúñiga"
"Miguel Angel Segura Manrique"
import json

with open('prueba.json') as file:
    data = json.load(file)

for x in data['Transmilenio']:
  a = x['Nombre_Troncal']
  b = x['Numero_Troncal']
  name = [a, b]
  print(name)
  for y in x['Estaciones']:
    c = y['nombre']
    d = y['latitud']
    e = y['longitud']
    f = y['tipo']
    lista = [c, d, e, f]
    print(lista)

  print("\n")
print(lista)



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



# PEDIR LAS ESTACIONES #
aa = input("Introdusca el nombre de la estacion A: ")

print("A:", aa)
bb = input("Introdusca el nombre de la estacion B: ")

print("B:", bb)



for x in data['Transmilenio']:
  for y in x['Estaciones']:
    c = y['nombre']
    d = y['latitud']
    e = y['longitud']
    f = y['tipo']
    
    if aa == c:
      Dato1 = c
      lat01 = d
      lon01 = e
        
    if bb == c:
      dato2 = c
      lat02 = d
      lon02 = e



print("dato 1 es: ", lat01,"dato 2 es:",lat02)


import math
# CALCULAR LA DISTANCIA APROXIMADA#
rad = math.pi / 180
distancia1 = (lat02 - lat01)
distancia2 = (lon02 - lon01)
R = 6372.795477598
a = (math.sin(rad * distancia1 / 2)) **2 + math.cos(rad * lat01) * math.cos(rad * lat02) * (math.sin(rad * distancia2 / 2)) **2
dis = 2 * R * math.asin(math.sqrt(a))
 
print("distancia aproximada",dis)

'''
#CALCULAR DISTANCIAS ENTRE ESTACIONES
d01 = -1 #En esta linea sale error
d02 = 
d1 = int(d01)
d2 = int(d02-1)
pp = 0
while d1 <= d2:
    lat01 = ("Latitud")[d1]
    lon01 = solicitar_Trasmi("Longitud")[d1]
    lat02 = solicitar_Trasmi.getElementsByTagName("Latitud")[d1+1]
    lon02 = solicitar_Trasmi.getElementsByTagName("Longitud")[d1+1]

    Dato001 = solicitar_Trasmi.getElementsByTagName("nombre")[d1]
    Dato002 = solicitar_Trasmi.getElementsByTagName("nombre")[d1+1]


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
'''''
