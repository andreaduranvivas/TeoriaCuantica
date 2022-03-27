
import retosProgramacion as retos
from LibreriaComplejos import LibEspacioVectorial as lev
from math import sqrt
import unittest


class TestStringMethods(unittest.TestCase):

    def test_canicas_coefbool(self):
        matriz_adj = [[(0, 0), (1 / 6, 0), (5 / 6, 0)],
                      [(1 / 3, 0), (1 / 2, 0), (1 / 6, 0)],
                      [(2 / 3, 0), (1 / 3, 0), (0, 0)]]

        vector = [[(1 / 2, 0)], [(0, 0)], [(1 / 2, 0)]]
        tiempo = 1
        click = retos.ExperimentMarbles(matriz_adj, vector, tiempo)
        self.assertAlmostEqual(click, [[(0.4166666666666667, 0.0)],
                                       [(0.25, 0.0)], [(0.3333333333333333, 0.0)]])

    def test_ProbParticleInLine(self):
        ket = [[(-3, -1)], [(0, -2)], [(0, 1)], [(2, 0)]]
        p = 2
        probabilidad = retos.ProbParticleInLine(p, ket)
        self.assertAlmostEqual(probabilidad, 0.05263157894736842)

    def test_normalizedket(self):
        psi1 = [[(1, 1)], [(2, -1)]]
        normpsi1 = lev.normalizar(psi1)
        self.assertAlmostEqual(normpsi1, [[(0.3779644730092272, 0.3779644730092272)],
                                          [(0.7559289460184544, -0.3779644730092272)]])

    def test_AmpliTransition(self):
        psi = lev.multEscalarMatrices((sqrt(2) / 2, 0), [[(1, 0)], [(0, 1)]])
        pfi = lev.multEscalarMatrices((sqrt(2) / 2, 0), [[(0, 1)], [(-1, 0)]])
        ampli = retos.AmpliTransition(psi, pfi)
        self.assertAlmostEqual(ampli, (0.0, -1.0000000000000002))

    def test_ExpectedValue(self):
        sigma = [[(0, 0), (0, -1)], [(0, 1), (0, 0)]]
        psi = [[(1 / sqrt(2), 0)], [(0, 1 / sqrt(2))]]
        media = retos.ExpectedValue(psi, sigma)
        real, imaginario = round(media[0]), round(media[1])
        media = (real, imaginario)
        self.assertAlmostEqual(media, (1, 0))

    def test_varianza(self):
        sigma = [[(0, 0), (0, -1)], [(0, 1), (0, 0)]]
        psi = [[(1 / sqrt(2), 0)], [(0, 1 / sqrt(2))]]
        varianza = retos.variance(sigma, psi)
        self.assertAlmostEqual(varianza, (0.0, 0))

    def test_EigenValues(self):
        sigma = [[(-1, 0), (0, -1)], [(0, 1), (1, 0)]]
        PossibleValues = retos.EigenValues(sigma)
        self.assertAlmostEqual(
            PossibleValues, [(-1.41421356, 0.0), (1.41421356, 0.0)])
        sigma = [[(1, 0), (0, -1)], [(0, 1), (2, 0)]]
        PossibleValues = retos.EigenValues(sigma)
        self.assertAlmostEqual(
            PossibleValues, [(0.38196601, 0.0), (2.61803399, 0.0)])
        # sigma = [[(-1, 0), (0, -1), (1, 0)],[(0, 1), (1, 0), (1, 0)],[(0, 1), (1, 0), (1, 0)]]
        # print(q.EigenValues(sigma))

    def test_ProbTransition(self):
        e = [[(0, -0.923)], [(-0.382, 0)]]
        psi = [[(1 / 2, 0)], [(1 / 2, 0)]]
        prob = retos.ProbTransition(psi, e)
        prob = round(prob, 2)
        self.assertAlmostEqual(prob, 0.5)


if __name__ == '__main__':
    unittest.main()