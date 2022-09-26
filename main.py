from re import A
from codigo import Punto, Rectangulo

if __name__ == '__main__':
    #Experimentacion
    A = Punto.constructor(2, 3); Punto.string(A)
    B = Punto.constructor(5, 5); Punto.string(B)
    C = Punto.constructor(-3, -1); Punto.string(C)
    D = Punto.constructor(); Punto.string(D)
    Punto.cuadrante(A); Punto.cuadrante(C); Punto.cuadrante(D)
    print("El vector AB es "+str(Punto.vector(A, B)))
    print("El vector BA es "+str(Punto.vector(B, A)))
    print("La distancia AB es "+str(Punto.distancia(A, B)))
    print("La distancia BA es "+str(Punto.distancia(B, A)))
    distancia1 = Punto.distancia(A, D)
    distancia2 = Punto.distancia(B, D)
    distancia3 = Punto.distancia(C, D)
    d = [distancia1, distancia2, distancia3]
    if max(d) == distancia1:
        print("El vector que está a máxima distancia del origen de coordenadas es "+str(A))
    elif max(d) == distancia2:
        print("El vector que está a máxima distancia del origen de coordenadas es "+str(B))
    elif max(d) == distancia3:
        print("El vector que está a máxima distancia del origen de coordenadas es "+str(C))
    A, B, C, D = Rectangulo.constructor(A[0], A[1], B[0], B[1])
    print("Puntos del rectángulo = "+str(A)+str(C)+str(B)+str(D))
    altura = Rectangulo.altura(A, B)
    area = Rectangulo.area(A, B)
    a, b = Rectangulo.base(A, B)
    base = Punto.distancia(a,b)
    print("El área del rectángulo es "+str(area))
    print("La altura del rectángulo es "+str(altura))
    print("La base del rectángulo es "+str(base))