'''Libreria Complejos CNYT
Andrea Durán Vivas'''

#Recordar que las operaciones que incluyan la fase
#se harán en radianes

import math

#Suma de complejos
def sumacplx (c1, c2):
    '''Función que retorna la suma de dos números complejos
       (tuple, tuple) --> tuple'''
    return (c1[0]+c2[0], c1[1]+c2[1])


#Resta de complejos
def restacplx (c1, c2):
    '''Función que retorna la resta de dos números complejos
       (tuple, tuple) --> tuple'''
    return (c1[0] - c2[0], c1[1] - c2[1])


#Multiplicacion de complejos
def multiplicacioncplx (c1, c2):
    '''Función que retorna la multiplicación de dos números complejos
        (tuple, tuple) --> tuple'''
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginario = c1[0] * c2[1] + c2[0] * c1[1]

    return (real, imaginario)


#Division de complejos
def divisioncplx (c1, c2):
    '''Función que retorna la división de dos números complejos
       (tuple, tuple) --> tuple'''
    real = (c1[0] * c2[0] + c1[1] * c2[1]) / (c2[0] ** 2 + c2[1] ** 2)
    imaginario = (c2[0] * c1[1] - c1[0] * c2[1]) / (c2[0] ** 2 + c2[1] ** 2)
    return (real, imaginario)

#Modulo
def modulo (c1):
    '''Función que retorna el módulo de un número complejo
        (tuple) --> int or float'''
    return (c1[0] ** 2 + c1[1] ** 2)**(1/2)

#Modulo cuadrado
def moduloCuad(c):
    """Función que retorna el módulo al cuadrado de un valor complejo"""
    return (c[0]**2) + (c[1]**2)

#Conjugado
def conjugado (c1):
    '''Función que retorna el conjugado de un número complejo
        (tuple) --> tuple'''
    real = c1[0]
    imaginario = -c1[1]
    return (real, imaginario)

#Fase
def fase (c1):
    '''Función que retorna la fase de un número complejo
       (tuple) --> float'''
    return math.atan2(c1[1],c1[0])

#Cartesiano a polar
def conv_cartesiana_a_polar (c1):
    '''Función que retorna la conversión de coordenadas cartesianas
       a polares
        (tuple) --> tuple'''
    return (modulo(c1), fase(c1))

#Polar a cartesiano
def conv_polar_a_cartesiano (c1):
    '''Función que retorna la conversión de coordenadas polares
       a cartesianas
       (tuple) --> tuple'''
    x = c1[0] * math.cos(c1[1])
    y = c1[0] * math.sin(c1[1])
    return (x, y)

#Multiplicacion coordenadas polares
def multiplicacioncmplx_polar (c1, c2):
    '''Función que retorna la multiplicacion entre coordenadas polares
       (tuple) --> tuple'''
    magnitud = c1[0] * c2[0]
    phase = c1[1] + c2[1]
    return (magnitud, phase)


if __name__ == '__main__':
    print(sumacplx((3.5, 7), (4.2, 8))) #(3.5 + 7i) + (4.2 + 8i) = (7.7 + 15i)
    print(restacplx((3.5, 7), (4, 5))) #(3.5 + 7i) + (4.1 + 5i) = (-0.5 + 2i)
    print(multiplicacioncplx((3.5, 7), (4, 5)))  # (3.5 + 7i) x (4.1 + 5i) = (-21, 45.5)
    print(divisioncplx((-2, 1), (1, 2)))  #(-2 + 1i)/(1 + 2i) = (0, 1)
    print(divisioncplx((4, -7), (1.4, 9))) #(-0.6918997107039537, -0.5520732883317261)
    print(modulo((8,4))) # + sqrt(64 + 16) = 8.94427190999916
    print(conjugado((4, -2))) #(4, -2) = (4, 2)
    print(fase((9, 5))) # 0.507098504392337
    print(conv_cartesiana_a_polar((4,5))) #(6.4031242374328485, 0.8960553845713439)
    print(conv_polar_a_cartesiano((4,5))) #(1.134648741852905, -3.835697098652554)
    print()
    print(multiplicacioncplx((0,-1), (0, 1/(2**(1/2)))))
