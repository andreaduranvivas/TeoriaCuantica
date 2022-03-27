'''
Libreria CNYT
Operaciones con Vectores y Matrices
Andrea Durán Vivas
'''

from LibreriaComplejos import Libcplx as lc
import math

#verificar que el tamaño de los vectores sean iguales
def verificacion (v,w):
    '''Función que verifica si dos vectores son del mismo tamaño
       (list, list) --> bool'''
    fila1 = len(v)
    fila2 = len(w)

    return fila1 == fila2


#Suma de vectores
def sumavec (v, w):
    '''Función que retorna la suma entre dos vectores
       (list, list) --> list'''
    if verificacion(v, w) == True:
        lon = len(v)
        res = [(0,0) for i in range(lon)]
        j = 0

        while j < lon:
            res[j] = lc.sumacplx(v[j], w[j])
            j += 1

        return res

    return 'Inconsistente: El tamaño de las matrices o los vectores no es igual'

def restavec (v, w):
    '''Función que retorna la resta entre dos vectores
       (list, list) --> list'''
    if verificacion(v, w) == True:
        lon = len(v)
        res = [(0,0) for i in range(lon)]
        j = 0

        while j < lon:
            res[j] = lc.restacplx(v[j], w[j])
            j += 1

        return res

    return 'Inconsistente: El tamaño de las matrices o los vectores no es igual'


#Inverso aditivo de un vector
def inverso (v):
    '''Función que retorna el inverso aditivo de un vector
       (list) --> list'''
    lon = len(v)
    res = [(0, 0) for i in range(lon)]
    j = 0
    while j < lon:
        res[j] = lc.multiplicacioncplx((-1, 0), v[j])
        j += 1
    return res


#Multiplicacion de un escalar por un vector complejo
def multiplicacionEscalar (num, v):
    '''Función que retorna la multiplicación entre un número complejo
       y un vector
       (tuple, list) --> list'''
    lon = len(v)
    res = [(0, 0) for i in range(lon)]
    j = 0
    while j < lon:
        res[j] = lc.multiplicacioncplx(num, v[j])
        j += 1
    return res


#Adicion de matrices complejas
def sumaMatrices (v, w):
    '''Función que retorna la suma entre dos matrices
           (list 2D, list 2D) --> list 2D'''
    if verificacion(v, w) == True and verificacion(v[0], w[0]) == True:
        filas = len(v)
        j = 0
        res = [[] for i in range(filas)]

        while j < filas:
            res[j] = sumavec(v[j], w[j])
            j += 1

        return res

    return 'Inconsistente: El tamaño de las matrices o los vectores no es igual'


#Resta de matrices complejas
def restaMatrices (v, w):
    '''Función que retorna la suma entre dos matrices
           (list 2D, list 2D) --> list 2D'''
    if verificacion(v, w) == True and verificacion(v[0], w[0]) == True:
        filas = len(v)
        j = 0
        res = [[] for i in range(filas)]

        while j < filas:
            res[j] = restavec(v[j], w[j])
            j += 1

        return res

    return 'Inconsistente: El tamaño de las matrices o los vectores no es igual'


#Inverso aditivo de una matriz compleja
def inversoMatrices (v):
    '''Función que retorna el inverso aditivo de una matriz
       (list 2D) --> list 2D'''
    filas = len(v)
    j = 0
    res = [[] for i in range(filas)]

    while j < filas:
        res[j] = inverso(v[j])
        j += 1

    return res


#Multiplicación de un escalar por una matriz compleja
def multEscalarMatrices(num, v):
    '''Función que retorna la multiplicaion entre un número complejo y
       una matriz
       (tuple, list 2D) --> list 2D'''
    filas = len(v)
    j = 0
    res = [[] for i in range(filas)]

    while j < filas:
        res[j] = multiplicacionEscalar(num, v[j])
        j += 1

    return res

#Transpuesta de una matriz/vector
def transpuesta (v):
    '''Función que retorna la transpuesta de un vector o una matriz
        (list) --> list'''
    res = []

    for k in range(len(v[0])):
        res.append([])
        for j in range(len(v)):
            res[k].append(v[j][k])

    return res


#Conjugado de una matriz/vector
def conjugadoMatVec(v):
    '''Función que retorna el conjugado de un vector o una matriz
       (list) --> list'''
    filas = [(0, 0)] * len(v[0])
    res = [filas] * len(v)

    for j in range(len(v)):
        filas = [(0, 0)] * len(v[0])
        res[j] = filas

        for k in range(len(v[0])):
            res[j][k] = lc.conjugado(v[j][k])

    return res


#Adjunta (daga) de una matriz/vector
def adjunta(v):
    '''Función que retorna la adjunta de un vector o una matriz
        (list) --> list'''

    return transpuesta(conjugadoMatVec(v))

#Producto de dos matrices de tamaños compatibles
def multiplicacionMatrices(A, B):
    '''Función que retorna la multiplicación entre dos matrices de tamaños
       compatibles
          (list 2D) --> list 2D'''

    filasA = len(A)
    columnasA = len(A[0])
    filasB = len(B)
    columnasB = len(B[0])

    if columnasA != filasB:
        raise Exception('Incompatible sizes')

    #inicialización de la matriz
    res = [[(0,0) for i in range(columnasB)] for j in range(filasA)]

    for j in range(filasA):
        for k in range(columnasB):#
            for h in range(columnasA):
                res[j][k] = lc.sumacplx(res[j][k], lc.multiplicacioncplx(A[j][h], B[h][k]))
    return res

#Acción de una matriz sobre un vector
def accion(A, v):
    '''Función que calcula la acción de una matriz sobre un vector
       (list 2D, list) --> list'''

    return multiplicacionMatrices(A, v)

#Producto interno
def productoInterno(v1, v2):
    '''Función que retorna el prodcuto interno entre dos vectores
       (list 2D, list 2D) --> list 2D'''
    #Este es el espacio vectorial C^n
    return multiplicacionMatrices(adjunta(v1), v2)[0][0]

#Norma
def norma(v):
    '''Función que retorna la norma de un vector
       (list) --> list'''
    pro = productoInterno(v, v)
    if pro[1] == 0:
        return math.sqrt(pro[0])
    else:
        v2 = lc.conv_cartesiana_a_polar(pro)
        return (math.sqrt(v2[0], v2[1]/2))

#Distancia
def distancia(v1, v2):
    '''Función que retorna la distancia entre dos vectores
       (list, list) --> list'''
    resta = restaMatrices(v1, v2)
    pro = productoInterno(resta, resta)

    if pro[1] == 0:
        return math.sqrt(pro[0])
    else:
        v3 = lc.conv_cartesiana_a_polar(pro)
        return (math.sqrt(v3[0]), v3[1]/2)

#Unitaria
def unitaria(A):
    '''Función que retorna si una matriz es unitaria
       (list 2D) --> bool'''
    B = multiplicacionMatrices(adjunta(A), A)
    for i in range(len(B)):
        for j in range(len(B[0])):
            if i == j:
                if B[i][j] != (1,0):
                    if (round(B[i][j][0], 10), round(B[i][j][1], 10)) != (1,0):
                        return "no es unitaria"
            else:
                if B[i][j] != (0,0):
                    return "no es unitaria"
                else:
                    return "es unitaria"

#Hermitiana
def hermitiana(A):
    '''Función que retorna si una matriz es hermitiana
       (list 2D ) --> bool'''
    adj = adjunta(A)
    if adj == A:
        return True
    return False

#Producto tensor
def productoTensor (A, B):
    '''Función que retorna el producto tensor entre vectores
       (list, list) --> list'''
    filasA = len(A)
    filasB = len(B)
    filasRes = filasA * filasB
    res = [(0,0)] * filasRes

    index = 0
    for i in range(filasA):
        for j in range(filasB):
            res[index] = lc.multiplicacioncplx(A[i], B[j])
            index += 1
    return res

def moduloCuadVec(vect):
    """Función que retorna el módulo al cuadrado de un Vector"""
    nv = len(vect)
    sqmodule = 0.0
    for j in range(nv):
        sqmodule += lc.moduloCuad(vect[j][0])
    return sqmodule

def moduloVec(vect):
    """Función que retorna el módulo de un Vector"""
    return math.sqrt(moduloCuadVec(vect))

def normalizar(vect):
    """Función que normaliza un vector"""
    escalar = 1/math.sqrt(moduloCuadVec(vect))
    return multEscalarMatrices((escalar, 0), vect)

def identidad(mat):
    result = [[(0,0) for i in range(len(mat[0]))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == j:
                result[i][j] = (1,0)
    return result

if __name__ == '__main__':
    print(sumavec([(0,3), (0,0), (2,8)], [(1,1), (2,1), (0,1)]))
    #[(0,3), (0,0), (2,8)] + [(1,1), (2,1), (0,1)] = [(1,4), (2,1), (2,9)]
    print(restavec([(0, 3), (0, 0), (2, 8)], [(1, 1), (2, 1), (0, 1)]))
    #[(-1, 2), (-2, -1), (2, 7)]
    print(inverso([(0,3), (0,0), (2,8)]))
    #[(0, -3), (0, 0), (-2, -8)]
    print(multiplicacionEscalar((1,2), [(0,3), (0,0), (2,8)]))
    #[(-6, 3), (0, 0), (-14, 12)]
    print(sumaMatrices([[(0,2), (0,1)], [(1,2), (2,4)]], [[(1,0), (1,1)], [(8,0), (0,0)]]))
    #[[(1, 2), (1, 2)], [(9, 2), (2, 4)]]
    print(restaMatrices([[(0, 2), (0, 1)], [(1, 2), (2, 4)]], [[(1, 0), (1, 1)], [(8, 0), (0, 0)]]))
    #[[(-1, 2), (-1, 0)], [(-7, 2), (2, 4)]]
    print(inversoMatrices([[(0,2), (0,1)], [(1,2), (2,4)]]))
    #[[(0, -2), (0, -1)], [(-1, -2), (-2, -4)]]
    print(multEscalarMatrices((1,2), [[(0,3), (0,0), (2,8)], [(0,3), (0,0), (2,8)]]))
    #[[(-6, 3), (0, 0), (-14, 12)], [(-6, 3), (0, 0), (-14, 12)]]
    print(transpuesta([[(0,2), (0,1)], [(1,2), (2,4)]]))
    #[[(0, 2), (1, 2)], [(0, 1), (2, 4)]]
    print(conjugadoMatVec([[(0,2), (0,1)], [(1,2), (2,4)]]))
    #[[(0, -2), (0, -1)], [(1, -2), (2, -4)]]
    print(adjunta([[(0,2), (0,1)], [(1,2), (2,4)]]))
    #[[(0, -2), (1, -2)], [(0, -1), (2, -4)]]
    print(multiplicacionMatrices([[(4, 0), (1, 0), (3, 0)], [(2, 0), (1, 0), (2, 0)], [(4, 0), (1, 0), (5, 0)]],
                                 [[(1, 0), (1, 0), (2, 0)], [(1, 0), (2, 0), (3, 0)], [(2, 0), (3, 0), (1, 0)]]))
    #[[(11, 0), (15, 0), (14, 0)], [(7, 0), (10, 0), (9, 0)], [(15, 0), (21, 0), (16, 0)]]
    print(accion([[(4, 0), (1, 0), (3, 0)], [(2, 0), (1, 0), (2, 0)], [(4, 0), (1, 0), (5, 0)]],
                 [[(2, 0)], [(3, 0)], [(1, 0)]]))
    #[[(14, 0)], [(9, 0)], [(16, 0)]]
    print(productoInterno([[(2, 0)], [(3, 1)], [(1, 4)]], [[(4, 1)], [(1, 2)], [(3, 3)]]))
    #(28, -2)
    print(norma([[(2, 0)], [(3, 1)], [(1, 4)]]))
    #5.5677643628300215
    print(distancia([[(2, 0)], [(3, 1)], [(1, 4)]], [[(4, 1)], [(1, 2)], [(3, 3)]]))
    #3.872983346207417
    print(unitaria([[(-5, 2), (1, -1), (7, -2)], [(2, 0), (3, 3), (-3, 5)], [(8, 10), (1, 0), (9, 5)]]))
    #False
    print(hermitiana([[(-1, 0), (0, -1)], [(0, 1), (1, 0)]]))
    #True
    print(productoTensor([(3, 0), (1, 0)], [(2,1), (0,1), (2,0)]))
    #[(6, 3), (0, 3), (6, 0), (2, 1), (0, 1), (2, 0)]
    print()