import unittest
import time
from modulo.kruskal import kruskal

class TestKruskal(unittest.TestCase):

    def test_valid_graph(self):
        # Caso estándar con un grafo válido
        grafo = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (1, 4, 4)]
        resultado = kruskal(grafo)
        self.assertEqual(len(resultado), 3, "El AGM debe tener 3 aristas")
        self.assertTrue(all(isinstance(arista, tuple) and len(arista) == 3 for arista in resultado))

    def test_empty_graph(self):
        # Caso de grafo vacío
        grafo = []
        resultado = kruskal(grafo)
        self.assertEqual(resultado, [], "El AGM de un grafo vacío debe ser vacío")

    def test_single_edge_graph(self):
        # Grafo con una sola arista
        grafo = [(1, 2, 10)]
        resultado = kruskal(grafo)
        self.assertEqual(resultado, [(1, 2, 10)], "El AGM con una sola arista debe ser la misma arista")

    def test_invalid_graph_format(self):
        # Caso en el que la arista no tiene la estructura correcta
        grafo = [(1, 2, 10), (2, 3)]  # Arista inválida (falta peso)
        with self.assertRaises(ValueError):
            kruskal(grafo)

    def test_non_integer_values(self):
        # Caso en el que la arista tiene valores no enteros
        grafo = [(1, 'b', 10)]  # Nodo2 no es un entero
        with self.assertRaises(ValueError):
            kruskal(grafo)

    def test_invalid_graph_elements(self):
        # Caso en el que algún nodo o peso es <= 0
        grafo = [(0, 1, 10)]  # Nodo1 no es válido (<= 0)
        with self.assertRaises(ValueError):
            kruskal(grafo)

    def test_disconnected_graph(self):
        # Caso de un grafo desconectado
        grafo = [(1, 2, 10), (3, 4, 20)]
        with self.assertRaises(ValueError):
            kruskal(grafo)

    def test_performance(self):
        # Prueba de rendimiento con un grafo grande
        n = 1000  # Número de nodos
        grafo = [(i, i + 1, 1) for i in range(1, n)]  # Grafo en cadena de 1000 nodos
        start_time = time.time()
        kruskal(grafo)
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 1, "La ejecución debería ser más rápida que 1 segundo para 1000 nodos")

    def test_multiple_components(self):
        # Caso de múltiples componentes
        grafo = [(1, 2, 10), (2, 3, 20), (4, 5, 5)]  # No es conexo
        with self.assertRaises(ValueError):
            kruskal(grafo)

    def test_edge_case(self):
        # Caso borde con una tupla no válida (solo un nodo sin aristas)
        grafo = [(1, 2, 1), (1, 3, 1), (2, 3, 1)]  # Grafo en forma de triángulo
        resultado = kruskal(grafo)
        self.assertEqual(len(resultado), 2, "El AGM de un triángulo debe tener 2 aristas")

    def test_sorted_graph(self):
        # Caso con un grafo ya ordenado por peso
        grafo = [(1, 2, 1), (2, 3, 2), (1, 3, 3)]
        resultado = kruskal(grafo)
        self.assertEqual(resultado, [(1, 2, 1), (2, 3, 2)], "El AGM debe ser el esperado después de aplicar Kruskal")

    def test_reverse_sorted_graph(self):
        # Caso con un grafo ordenado inversamente
        grafo = [(1, 3, 3), (2, 3, 2), (1, 2, 1)]
        resultado = kruskal(grafo)
        self.assertEqual(resultado, [(1, 2, 1), (2, 3, 2)], "El AGM debe ser el esperado después de aplicar Kruskal")

    def test_graph_with_cycle(self):
        # Caso con un ciclo (Kruksal no debe incluirlo)
        grafo = [(1, 2, 1), (2, 3, 2), (3, 1, 3)]  # Esto forma un ciclo
        resultado = kruskal(grafo)
        self.assertEqual(len(resultado), 2, "El AGM no debe contener ciclos, debe tener 2 aristas")

    def test_graph_with_identical_weights(self):
        # Caso con aristas con pesos idénticos
        grafo = [(1, 2, 1), (2, 3, 1), (1, 3, 1)]
        resultado = kruskal(grafo)
        self.assertEqual(len(resultado), 2, "El AGM con pesos idénticos debe tener 2 aristas")

    def test_single_node_graph(self):
        # Grafo con un solo nodo y sin aristas
        grafo = []  # Un solo nodo sin aristas
        resultado = kruskal(grafo)
        self.assertEqual(resultado, [], "Un grafo con un solo nodo no tiene aristas")


if __name__ == '__main__':
    unittest.main()
