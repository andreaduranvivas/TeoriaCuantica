'''Pruebas Libreria Complejos CNYT
Andrea Durán Vivas'''

import Libcplx as lc
import unittest

class TestCplxOperations (unittest.TestCase):
    def testSumacplx (self):
        suma = lc.sumacplx((3.5, 7), (4.2, 8))
        self.assertAlmostEqual(suma[0], 7.7)
        self.assertAlmostEqual(suma[1], 15)

        suma2 = lc.sumacplx((3,5), (-2.6,6.8))
        self.assertAlmostEqual(suma2[0], 0.4)
        self.assertAlmostEqual(suma2[1], 11.8)

    def testRestacplx (self):
        resta = lc.restacplx((3.5, 7), (4, 5))
        self.assertAlmostEqual(resta[0], -0.5)
        self.assertAlmostEqual(resta[1], 2)

        resta2 = lc.restacplx((0.1, 7), (4, -1))
        self.assertAlmostEqual(resta2[0], -3.9)
        self.assertAlmostEqual(resta2[1], 8)

    def testProductocplx (self):
        producto = lc.multiplicacioncplx((3.5, 7), (4, 5))
        self.assertAlmostEqual(producto[0], -21)
        self.assertAlmostEqual(producto[1], 45.5)

        producto2 = lc.multiplicacioncplx((2, 5), (6, 7))
        self.assertAlmostEqual(producto2[0], -23)
        self.assertAlmostEqual(producto2[1], 44)

    def testDivisioncplx (self):
        division = lc.divisioncplx((-2, 1), (1, 2))
        self.assertAlmostEqual(division[0], 0)
        self.assertAlmostEqual(division[1], 1)

        division2 = lc.divisioncplx((4, -7), (1.4, 9))
        self.assertAlmostEqual(division2[0], -0.6918997107039537)
        self.assertAlmostEqual(division2[1], -0.5520732883317261)

    def testModulo (self):
        modulo = lc.modulo((8,4))
        self.assertAlmostEqual(modulo, 8.94427190999916)

        modulo2 = lc.modulo((4, -3))
        self.assertAlmostEqual(modulo2, 5)

    def testConjugado (self):
        conjugado = lc.conjugado((4, -2))
        self.assertAlmostEqual(conjugado[0], 4)
        self.assertAlmostEqual(conjugado[1], 2)

        conjugado2 = lc.conjugado((-3, 1))
        self.assertAlmostEqual(conjugado2[0], -3)
        self.assertAlmostEqual(conjugado2[1], -1)

    def testFase (self):
        fase = lc.fase((9, 5))
        self.assertAlmostEqual(fase, 0.507098504392337)

        fase2 = lc.fase((4, 1))
        self.assertAlmostEqual(fase2, 0.24497866312686414)

    def testPolartoCartesian (self):
        cartesian = lc.conv_polar_a_cartesiano((4, 5))
        self.assertAlmostEqual(cartesian[0], 1.134648741852905)
        self.assertAlmostEqual(cartesian[1], -3.835697098652554)

        cartesian2 = lc.conv_polar_a_cartesiano((5, 0.52))
        self.assertAlmostEqual(cartesian2[0], 4.3390958983882495)
        self.assertAlmostEqual(cartesian2[1], 2.484400689218684)

    def testCartesiantoPolar (self):
        polar = lc.conv_cartesiana_a_polar((4,5))
        self.assertAlmostEqual(polar[0], 6.4031242374328485)
        self.assertAlmostEqual(polar[1], 0.8960553845713439)

        polar2 = lc.conv_cartesiana_a_polar((4, 90))
        self.assertAlmostEqual(polar2[0], 90.08884503644167)
        self.assertAlmostEqual(polar2[1], 1.5263811115479857)


if __name__ == '__main__':
    unittest.main()