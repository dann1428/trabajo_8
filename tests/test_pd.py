"""Pruebas: python -m unittest discover tests  (desde la raíz del proyecto)."""
import itertools, os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from escaleras import contar_formas
from monedas import cambio_minimo


def formas_fuerza_bruta(n):
    """Cuenta composiciones de n con 1 y 2 de forma recursiva (verificación)."""
    return 1 if n <= 1 else formas_fuerza_bruta(n - 1) + formas_fuerza_bruta(n - 2)


class Escaleras(unittest.TestCase):
    def test_enunciado(self):
        self.assertEqual(contar_formas(4)[0], 5)
        self.assertEqual(contar_formas(5), (8, [1, 1, 2, 3, 5, 8]))
        self.assertEqual(contar_formas(7)[1], [1, 1, 2, 3, 5, 8, 13, 21])

    def test_bordes(self):
        self.assertEqual(contar_formas(0), (1, [1]))
        self.assertEqual(contar_formas(1), (1, [1, 1]))
        with self.assertRaises(ValueError):
            contar_formas(-1)

    def test_vs_recursivo(self):
        for n in range(15):
            self.assertEqual(contar_formas(n)[0], formas_fuerza_bruta(n))


class Monedas(unittest.TestCase):
    def test_enunciado(self):
        m, comb, t = cambio_minimo([1, 3, 4], 6)
        self.assertEqual((m, comb, t), (2, [3, 3], [0, 1, 2, 1, 1, 2, 2]))
        m, comb, t = cambio_minimo([1, 2, 5], 11)
        self.assertEqual((m, sum(comb)), (3, 11))
        self.assertEqual(t, [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3])

    def test_imposible_y_cero(self):
        self.assertEqual(cambio_minimo([2], 3)[0], -1)
        self.assertEqual(cambio_minimo([5], 0)[:2], (0, []))

    def test_greedy_falla(self):  # greedy daría 4+1+1; el óptimo es 3+3
        self.assertEqual(cambio_minimo([1, 3, 4], 6)[0], 2)

    def test_vs_fuerza_bruta(self):
        for monedas in ([1, 3, 4], [2, 5, 7], [1, 5, 10, 25], [3, 7]):
            for obj in range(0, 25):
                m, comb, _ = cambio_minimo(monedas, obj)
                mejor = None
                for k in range(0, obj + 1):
                    if any(sum(c) == obj for c in itertools.combinations_with_replacement(monedas, k)):
                        mejor = k; break
                self.assertEqual(m, -1 if mejor is None else mejor)
                if m != -1:
                    self.assertEqual(sum(comb), obj); self.assertEqual(len(comb), m)


if __name__ == "__main__":
    unittest.main()
