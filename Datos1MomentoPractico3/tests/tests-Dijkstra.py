import unittest
from modulo.Dijkstra import dijkstra
from modulo.grafoconpeso import GrafoConPeso
from modulo.contiene_ciclo import contiene_ciclo


"""class TestGrafoConPeso(unittest.TestCase):


    def test_grafoinit(self):
        # Evaluación de condiciones previas.
        # NO ES LISTA
        with self.assertRaises(ValueError):
            GrafoConPeso("unaString")

        # ES LISTA VACÍA
        with self.assertRaises(ValueError):
            GrafoConPeso([])

        # ES LISTA PERO NO DE LISTAS (COMPLETAMENTE)
        with self.assertRaises(ValueError):
            GrafoConPeso([[1, 2, 3], [2, 3, 4], "pepe"])

        # ES LISTA DE LISTAS QUE NO SON COMPUESTAS DE 3 ELEMENTOS
        with self.assertRaises(ValueError):
            GrafoConPeso([[1, 2, 3], [2, 1, 3], [3, 2, 3, 4], [2, 3, 1]])

        #ES LISTA DE LISTAS QUE NO SON COMPUESTAS DE 3 ELEMENTOS ENTEROS POSITIVOS
        with self.assertRaises(ValueError):
            GrafoConPeso([[1, 2, 3], [2, 7, 9], [2, 4, 2], [1, -2, 3]])

        #ES LISTA DE LISTAS QUE INCLUYEN AL VECTOR 0 COMO ORIGEN O DESTINO
        with self.assertRaises(ValueError):
            GrafoConPeso([[1, 2, 3], [2, 0, 3], [2, 3, 4]])


        # Evaluación de condiciones posteriores
        # CASO 1: Ejercicio 1
        info1 = [
            [1, 2, 4],  # Arista de 1 a 2 con peso 4
            [1, 3, 1],  # Arista de 1 a 3 con peso 1
            [2, 3, 2],  # Arista de 2 a 3 con peso 2
            [2, 4, 5],  # Arista de 2 a 4 con peso 5
            [3, 4, 8]  # Arista de 3 a 4 con peso 8
        ]

        grafo_esperado1 = {
            1: [(2, 4), (3, 1)],
            2: [(3, 2), (4, 5)],
            3: [(4, 8)],
            4: []
        }

        self.assertEqual(grafo_esperado1, GrafoConPeso(info1).Grafo)

"""


class TestDijkstra(unittest.TestCase):

    def test_grafo_vacio(self):
        # Debe lanzar ValueError si el grafo está vacío.
        with self.assertRaises(ValueError):
            dijkstra({}, 1)

    def test_vector_de_inicio_no_existe(self):
        # Debe lanzar ValueError si el nodo de inicio no está en el grafo.
        grafo = {1: [(2, 1)], 2: []}
        with self.assertRaises(ValueError):
            dijkstra(grafo, 3)

    def test_grafo_con_peso_negativo(self):
        # Debe lanzar ValueError si hay un peso negativo en el grafo.
        grafo = {1: [(2, -1)], 2: []}
        with self.assertRaises(ValueError):
            dijkstra(grafo, 1)

    def test_grafo_disconexo(self):
        # Debe lanzar ValueError si el grafo está desconectado.
        grafo = {
            1: [(2, 1)],
            2: [(3, 1)],
            3: [],
            4: []
        }
        with self.assertRaises(ValueError):
            dijkstra(grafo, 1)

    def test_grafo_con_mas_de_una_arista(self):
        # Debe lanzar ValueError si hay más de una arista entre dos nodos.
        grafo = {1: [(2, 1), (2, 2)], 2: [(3, 1)], 3: []}
        with self.assertRaises(ValueError):
            dijkstra(grafo, 1)

    def test_grafo_valores_correctos(self):
        # Debe lanzar ValueError si los valores no son listas de tuplas de exactamente 2 elementos.
        grafo = {1: [(2, 1)], 2: [(3, 2, 1)]}  # Segunda entrada no es una tupla de 2 elementos
        with self.assertRaises(ValueError):
            dijkstra(grafo, 1)

        grafo = {1: [(2, 1)], 2: [3]}  # Segunda entrada no es una tupla
        with self.assertRaises(ValueError):
            dijkstra(grafo, 1)

    def test_grafo_llaves_no_entero_positivo(self):
        # Debe lanzar ValueError si alguna llave no es un entero positivo.
        grafo = {"1": [(2, 1)]}  # Llave no es entero
        with self.assertRaises(ValueError):
            dijkstra(grafo, 1)

        grafo = {0: [(2, 1)]}  # Llave no es positivo
        with self.assertRaises(ValueError):
            dijkstra(grafo, 0)

    def test_tuplas_no_entero_positivo(self):
        # Debe lanzar ValueError si el destino de la tupla no es un entero positivo.
        grafo = {1: [(0, 1)], 2: []}  # Destino no es positivo
        with self.assertRaises(ValueError):
            dijkstra(grafo, 1)

    def test_peso_no_entero_o_negativo(self):
        # Debe lanzar ValueError si hay un peso no entero o negativo en el grafo.
        grafo = {1: [(2, "1")], 2: []}  # Peso no es entero
        with self.assertRaises(ValueError):
            dijkstra(grafo, 1)

    def test_unicidad_aristas(self):
        # Debe lanzar ValueError si hay aristas redundantes o no únicas.
        grafo = {1: [(2, 1), (2, 1)], 2: []}  # Arista redundante
        with self.assertRaises(ValueError):
            dijkstra(grafo, 1)

    def test_resultado_vacio(self):
        # Debe devolver un diccionario vacío cuando no hay nodos excepto el de inicio.
        grafo = {1: []}
        resultado = dijkstra(grafo, 1)
        self.assertEqual(resultado, {1: 0})

    def test_grafo_con_pesos_positivos(self):
        # Debe calcular correctamente las distancias en un grafo simple con pesos positivos.
        grafo = {1: [(2, 1), (3, 4)], 2: [(3, 2)], 3: []}
        resultado = dijkstra(grafo, 1)
        self.assertEqual({1: 0, 2: 1, 3: 3}, resultado)

    def test_multiples_rutas(self):
        # Debe elegir la ruta más corta con varias opciones.
        grafo = {1: [(2, 5), (3, 1)], 2: [(4, 2)], 3: [(2, 2), (4, 1)], 4: []}
        resultado = dijkstra(grafo, 1)
        self.assertEqual({1: 0, 2: 3, 3: 1, 4: 2}, resultado)

    def test_grafo_complejo(self):
        # Debe funcionar en un grafo más complicado con varios nodos.
        grafo = {
            1: [(2, 1), (3, 4)],
            2: [(3, 2), (4, 5)],
            3: [(4, 1)],
            4: []
        }
        resultado = dijkstra(grafo, 1)
        self.assertEqual({1: 0, 2: 1, 3: 3, 4: 4}, resultado)

    def test_grafo_completo(self):
        # Debe funcionar en un grafo donde todos los nodos están conectados.
        grafo = {
            1: [(2, 1), (3, 1)],
            2: [(1, 1), (3, 1)],
            3: [(1, 1), (2, 1)]
        }
        resultado = dijkstra(grafo, 1)
        self.assertEqual({1: 0, 2: 1, 3: 1}, resultado)

    def test_grafo_denso(self):
        grafo = {i: [(j, 1) for j in range(1, 6) if j != i] for i in range(1, 6)}
        resultado = dijkstra(grafo, 1)
        self.assertEqual(resultado, {1: 0, 2: 1, 3: 1, 4: 1, 5: 1})

    def test_grafo_ciclico(self):
        grafo = {1: [(2, 1)], 2: [(3, 1)], 3: [(1, 1)]}
        resultado = dijkstra(grafo, 1)
        self.assertEqual(resultado, {1: 0, 2: 1, 3: 2})

    def test_grafo_con_pesos_cero(self):
        grafo = {1: [(2, 0)], 2: [(3, 0)], 3: []}
        resultado = dijkstra(grafo, 1)
        self.assertEqual(resultado, {1: 0, 2: 0, 3: 0})

    def test_un_nodo_con_arista_a_si_mismo(self):
        grafo = {1: [(1, 0)]}
        resultado = dijkstra(grafo, 1)
        self.assertEqual(resultado, {1: 0})


    # RECOMENDACIÓN: La evaluación de este test se puede demorar un poco, es por eso la hemos desactivado
    # Puede descomentar las lineas y ejecutarlo, lo hemos probado sin alterar el módulo y ejecuta este test
    # en unos 2-3 minutos.
    """
    def test_tamano_limite_grafo(self):
        tamaño_base = 5000  # Comenzamos con un tamaño base
        incrementos = 1000  # Aumentamos el tamaño en incrementos de 1000
        max_tamaño = 10000  # Máximo tamaño que vamos a probar

        for tamaño in range(tamaño_base, max_tamaño + 1, incrementos):
            grafo = {i: [(j, 1) for j in range(1, tamaño + 1) if j != i] for i in range(1, tamaño + 1)}
            try:
                dijkstra(grafo, 1)
            except Exception as e:
                print(f"El algoritmo falló con un grafo de tamaño {tamaño}: {e}")
                break  # Salimos del bucle al primer error
"""

if __name__ == '__main__':
    unittest.main()

