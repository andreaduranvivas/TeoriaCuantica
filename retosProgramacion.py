'''Retos de programación CNYT
Andrea Durán Vivas'''

from LibreriaComplejos import LibEspacioVectorial as lev
from LibreriaComplejos import Libcplx as lc

import random
from math import sqrt
from matplotlib import pyplot
import numpy as np

"""================================ Capitulo 3 ======================================"""
def ExperimentMarbles(A, V, clic):
    '''Función que simula los estados del sistema según los clicks para el experimento 
        de la canicas con coeficientes booleanos
        (list, list, int --> list'''
    vector = V
    index = 0
    while index < clic:
        vector_click = lev.accion(A, vector)
        vector = vector_click
        index += 1
    return vector

def ExperimentSlitsMatrix(matrizAdyacencia, clic):
    '''Función que simula el experimento de las múltiples rendijas clásico probabilístico y
        cuántico, con más de dos rendijas. Generador de la matriz resultante
        (list --> list)'''
    veces = 1
    resultante = matrizAdyacencia
    while veces < clic:
        resultante = lev.multiplicacionMatrices(resultante, matrizAdyacencia)
        veces += 1
    return resultante

def ExperimentSlitsVector(resultante, state):
    '''Función que simula el experimento de las múltiples rendijas clásico probabilístico y 
        cuántico, con más de dos rendijas. Generador del vector de estado
        (list, list --> list)'''
    vector_click = lev.accion(resultante, state)
    return vector_click

def random_color():
    '''Función que genera colores al azar
        Función auxiliar para el graficador'''
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    return color

def graficador(vector_estados):
    '''Función que grafica con un diagrama de barras las probabilidades de un vector de estados.
       Guardar el gráfico en el computador con un formato png'''
    vertices = []
    colores = []
    for i in range(1, len(vector_estados) + 1):
        vertices += [i]
        colores += [random_color()]
    pyplot.title("probabilidades de un vector de estados")
    pyplot.bar(vertices, height = vector_estados, color = colores, width = 0.5)
    pyplot.ylabel("probabilidad")
    pyplot.savefig("probabilidades.png")
    pyplot.show()

"""================================ Capitulo 4 ======================================"""

"""================================Sección 4.1======================================"""
def ProbParticleInLine(p, ket):
    """Función que calcula la probabilidad de encontrar la partícula en una posición determinada.
    (int),(list) → (float)"""
    denominador = (lev.moduloCuadVec(ket))
    numerador = lc.moduloCuad(ket[p][0])
    prob = numerador/denominador
    return prob

def AmpliTransition(ket1, ket2):
    transition = lev.productoInterno(lev.normalizar(ket2),lev.normalizar(ket1))
    return transition

def ProbSpinUp(ket):
    return ProbParticleInLine(0, ket)

def ProbSpinDown(ket):
    return ProbParticleInLine(1, ket)

def probabilidadTransitar(bi, ket):
    return lc.moduloCuad(AmpliTransition(bi, ket))

"""================================Sección 4.2======================================"""

def conmutador(sigma1, sigma2):
    return lev.restaMatrices(lev.multiplicacionMatrices(sigma1, sigma2), lev.multiplicacionMatrices(sigma2, sigma1))

def ExpectedValue(psi, sigma):
    sigmapsi = lev.multiplicacionMatrices(sigma, psi)
    return lev.productoInterno(sigmapsi, psi)

def delta(sigma, psi):
    return lev.restaMatrices(sigma, lev.multEscalarMatrices(ExpectedValue(psi, sigma),lev.identidad(sigma)))

def variance(sigma, psi):
    return ExpectedValue(psi, lev.multiplicacionMatrices(delta(sigma, psi), delta(sigma, psi)))


"""================================Sección 4.3======================================"""


def ChageNotation(A):
    '''Función que aplica notación de números complejos para librería Numpy'''
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = complex(A[i][j][0], A[i][j][1])
    return A


def UseNotationValue(A):
    '''Función que aplica notación de números complejos para librería la librería implementada'''
    real, imaginario, result = "", "", []
    for i in range(len(A)):
        pos = str(A[i]).find("+")
        if pos == -1:
            pos = str(A[i]).find("-")
            # if pos == 0:
            # pos = str(A[i])[1:].find("-")
            # new_pos = str(A[i])[pos + 1:].find("-")
            # if new_pos != -1:
            # else:
            # else:
            # real = str(A[i])[:pos]
            # imaginario = str(A[i])[pos+1:len(A[i]) - 2]

        else:
            real = str(A[i])[:pos]
            imaginario = str(A[i])[pos + 1:len(A[i]) - 2]

        result += [(float(real), float(imaginario))]
        real, imaginario = "", ""

    return result


def EigenValues(sigma):
    '''Genera todas las medidas que podría llegar a registrar respecto al observable (valores propios)'''
    mat = np.array(ChageNotation(sigma))
    eigenvalue, featurevector = np.linalg.eig(mat)

    eigenvalue = str(eigenvalue).replace("[", "").replace("]", "").split()
    print(eigenvalue)
    eigenvalue = UseNotationValue(eigenvalue)
    return eigenvalue


def EigenVectors(sigma):
    '''Genera todas las medidas que podría llegar a registrar respecto al observable (valores propios)'''
    mat = np.array(ChageNotation(sigma))
    eigenvalue, featurevector = np.linalg.eig(mat)
    # print(featurevector)
    # featurevector = str(featurevector).replace("[", "").replace("]", "").split()
    # eigenvalue = UseNotationValue(eigenvalue)
    return featurevector

def ProbTransition(psi, e):
    '''Retorna la probabilidad de transición'''
    #e = EigenVectors(sigma)
    return lc.moduloCuad(AmpliTransition(e, psi))

def FinalState(U, psi, t):
    '''Genera el estado final'''
    index = 1
    finaldin = U
    while index < t:
        din = lev.multiplicacionMatrices(U,U)
        finaldin = din
        index += 1
    return lc.AccionMatVec(finaldin, psi)

if __name__ == '__main__':
    matrizAdyacencia = [[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
    [(1/2,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
    [(1/2,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
    [(0,0), (-1/sqrt(6),1/sqrt(6)), (0,0), (1,0), (0,0), (0,0), (0,0), (0,0)],
    [(0,0), (-1/sqrt(6),-1/sqrt(6)), (0,0), (0,0), (1,0), (0,0), (0,0), (0,0)],
    [(0,0), (1/sqrt(6),-1/sqrt(6)), (-1/sqrt(6),1/sqrt(6)), (0,0), (0,0), (1,0), (0,0), (0,0)],
    [(0,0), (0,0), (-1/sqrt(6),-1/sqrt(6)), (0,0), (0,0), (0,0), (1,0), (0,0)],
    [(0,0), (0,0), (1/sqrt(6),-1/sqrt(6)), (0,0), (0,0), (0,0), (0,0), (1,0)]]

    estado = [[(1,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)]]

    print(ExperimentSlitsMatrix(matrizAdyacencia, 2))
    print()
    print(ExperimentSlitsVector(ExperimentSlitsMatrix(matrizAdyacencia, 2), estado))
    print()
    p = 7
    ket = [[(2, 1)], [(-1, 2)], [(0, 1)], [(1, 0)], [(3, -1)], [(2, 0)], [(0, -2)],
           [(-2, 1)], [(1, -3)], [(0, -1)]]
    print(ProbParticleInLine(p, ket))
    print()
    print()
    sigma = [[(0, 0), (0, -1)], [(0, 1), (0, 0)]]
    psi = [[(1 / sqrt(2), 0)], [(0, 1 / sqrt(2))]]
    varianza = variance(sigma, psi)


