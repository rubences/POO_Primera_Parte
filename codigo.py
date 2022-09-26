import math
import re


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def constructor(a=0, b=0):
        punto = [a, b]
        return punto
    
    def string(Punto):
        print("("+str(Punto[0])+", "+str(Punto[1])+")")

    def cuadrante(punto):
        if punto[0]>0 and punto[1]>0:
            print("El punto "+str(punto)+" pertenece al cuadrante 1")
        elif punto[0]<0 and punto[1]>0:
            print("El punto "+str(punto)+" pertenece al cuadrante 2")
        elif punto[0]>0 and punto[1]<0:
            print("El punto "+str(punto)+" pertenece al cuadrante 3")
        elif punto[0]<0 and punto[1]<0:
            print("El punto "+str(punto)+" pertenece al cuadrante 4")
        elif punto[0]==0 and punto[1]!=0:
            print("El punto "+str(punto)+" está sobre el eje x")
        elif punto[1]==0 and punto[1]!=0:
            print("El punto "+str(punto)+" está sobre el eje y")
        elif punto[0]==0 and punto[1]==0:
            print("El punto "+str(punto)+" está en el eje de coordenadas")

    def vector(Punto1, Punto2):
        vector = [Punto2[0]-Punto1[0], Punto2[1]-Punto1[1]]
        return vector

    def distancia(Punto1, Punto2):
        return math.sqrt(Punto.vector(Punto1, Punto2)[0]**2+Punto.vector(Punto1, Punto2)[1]**2)

class Rectangulo:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def constructor(a=0, b=0, c=0, d=0):
        puntoinicial = [a, b]
        puntofinal = [c, d]
        puntoinicials = [c, b]
        puntofinals = [a, d]
        return puntoinicial, puntofinal, puntoinicials, puntofinals

    def base(Puntoinicial, Puntofinal): #Devuelve los puntos de la base
        if Puntoinicial[1]<Puntofinal[1]:
            a = Puntoinicial
            b = [Puntofinal[0], Puntoinicial[1]]
            return a, b
        else:
            a = Puntofinal
            b = [Puntoinicial[0], Puntofinal[1]]
            return a, b

    def altura(Puntoinicial, Puntofinal):
        return abs(Puntoinicial[1]-Puntofinal[1])

    def area(Puntoinicial, Puntofinal):
        a, b = Rectangulo.base(Puntoinicial, Puntofinal)
        return (Rectangulo.altura(Puntoinicial, Puntofinal)*Punto.distancia(a,b))