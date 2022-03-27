import retosProgramacion as retos
from LibreriaComplejos import LibEspacioVectorial as lev
from LibreriaComplejos import Libcplx as lc
from math import sqrt

def main():
    #Ejercicio 4.4.1
    U1 = [[(0,0), (1,0)], [(1,0), (0,0)]]
    U2 = [[(sqrt(2)/2, 0), (sqrt(2)/2, 0)],[(sqrt(2)/2, 0), (-sqrt(2)/2, 0)]]
    print("U1 "+lev.unitaria(U1)+"\n"+"U2 "+lev.unitaria(U2))
    Product = lev.multiplicacionMatrices(U1,U2)
    print("El producto de U1 y U2: "+ lev.unitaria(Product))

    #Ejercicio 4.4.2
    map = [[(0, 0), (1/sqrt(2), 0), (1/(sqrt(2)), 0), (0, 0)],
           [(0, 1/sqrt(2)), (0, 0), (0, 0), (1/sqrt(2), 0)],
           [(1/sqrt(2), 0), (0, 0), (0, 0), (0, 1/sqrt(2))],
           [(0, 0), (1/sqrt(2), 0), (-1/sqrt(2), 0), (0, 0)]]
    state = [[(1,0)],[(0,0)],[(0,0)],[(0,0)]]
    time = 3
    finalstate = retos.ExperimentMarbles(map, state, time)
    print("estado final = "+str(finalstate))
    prob = retos.ProbParticleInLine(3, finalstate)
    print("La probabilidad es de: "+str(prob))

    #Ejercicio 4.5.2
    #Sistema con n particulas con spin
    #|ψ> = C0,0 |X0> (x) |Y0> (x) C0,1 |X0> (x) |Y1> (x)
    #      C1,0 |X1> (x) |X0> (x) C1,1 |X1> (x) |X1 > (x) ... (x)
    #      C0,n-1 | X0 > (x) | Yn-1 > (x) C0,n-1 |X0> (x) |Yn-1> (x)
    #      Cn-1,0 |Xn-1> (x) |X0> (x) Cn-1,n-1 |Xn-1> (x) |Xn-1 >


    #Ejercicio 4.5.3
    # El estado sí es separable, debido a que al hacer la simplificación al dejarlo
    # en la forma de producto tensor, el sistema sí tiene solución, dejando a
    # C0' = 0. Se supone que para la solución, el vector está en el orden de la expresión
    # dada en el ejemplo 4.5.2 del libro

main()