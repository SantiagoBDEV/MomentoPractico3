import unittest
from modulo.contiene_ciclo import contiene_ciclo


class TestGrafoCiclo(unittest.TestCase):

    # 1. Caso base: Grafo vacío
    def test_grafo_vacio(self):
        """El grafo vacío no debe tener ciclos."""
        graph = {}
        self.assertFalse(contiene_ciclo(graph))

    # 2. Caso de grafo con un solo nodo sin conexiones
    def test_un_nodo_sin_conexiones(self):
        """Un grafo con un solo nodo sin conexiones no tiene ciclos."""
        graph = {1: []}
        self.assertFalse(contiene_ciclo(graph))

    # 3. Caso de grafo con un solo nodo y una conexión a sí mismo (autociclo)
    def test_un_nodo_autociclo(self):
        """Un grafo con un solo nodo con un ciclo (conexión a sí mismo) debería detectarlo como ciclo."""
        graph = {1: [1]}
        self.assertTrue(contiene_ciclo(graph))

    # 4. Grafo con dos nodos conectados (sin ciclo)
    def test_dos_nodos_sin_ciclo(self):
        """Un grafo con dos nodos conectados (sin ciclo) no tiene ciclo."""
        graph = {1: [2], 2: [1]}
        self.assertFalse(contiene_ciclo(graph))

    # 5. Grafo con tres nodos conectados linealmente (sin ciclo)
    def test_tres_nodos_lineales_sin_ciclo(self):
        """Un grafo de tres nodos conectados linealmente no tiene ciclo."""
        graph = {1: [2], 2: [1, 3], 3: [2]}
        self.assertFalse(contiene_ciclo(graph))

    # 6. Grafo con tres nodos formando un ciclo
    def test_tres_nodos_con_ciclo(self):
        """Un grafo con tres nodos formando un ciclo debe detectarlo."""
        graph = {1: [2], 2: [1, 3], 3: [2, 1]}
        self.assertTrue(contiene_ciclo(graph))

    # 7. Grafo desconectado sin ciclo
    def test_grafo_desconectado_sin_ciclo(self):
        """Un grafo desconectado sin ciclos debe retornar False."""
        graph = {1: [2], 2: [1], 3: []}
        self.assertFalse(contiene_ciclo(graph))

     # 8. Grafo desconectado con un ciclo en una de sus componentes
    def test_grafo_desconectado_con_ciclo(self):
        """Un grafo desconectado con ciclo en una de sus componentes debe retornar True."""
        # Primer componente sin ciclo: 1-2
        # Segundo componente con ciclo: 4-5-6-4
        graph = {
            1: [2], 2: [1],  # Componente 1 sin ciclo
            4: [5], 5: [6], 6: [4]  # Componente 2 con ciclo (4-5-6-4)
        }
        self.assertTrue(contiene_ciclo(graph))  # El ciclo en el segundo componente debe ser detectado

    # 9. Grafo con múltiples ciclos
    def test_grafo_con_multiples_ciclos(self):
        """Un grafo con múltiples ciclos debe retornar True."""
        graph = {1: [2], 2: [1, 3], 3: [2, 1], 4: [5], 5: [4, 6], 6: [5, 4]}
        self.assertTrue(contiene_ciclo(graph))

    # 10. Grafo con un ciclo en el mismo nodo (autociclo)
    def test_autociclo_en_un_nodo(self):
        """Si un nodo se conecta a sí mismo, se debe detectar un ciclo."""
        graph = {1: [1]}
        self.assertTrue(contiene_ciclo(graph))

    # 11. Grafo con conexiones a nodos inexistentes (debe lanzar ValueError)
    def test_conexiones_a_nodos_inexistentes(self):
        """Si el grafo tiene conexiones a nodos inexistentes, se debe lanzar un ValueError."""
        graph = {1: [2], 2: [1], 3: [4]}  # Nodo 4 no existe
        with self.assertRaises(ValueError):
            contiene_ciclo(graph)

    # 12. Grafo con claves que no son enteros positivos (debe lanzar ValueError)
    def test_claves_no_enteros_positivos(self):
        """Si las claves del grafo no son enteros positivos, debe lanzar ValueError."""
        graph = {"a": [1], 2: [3]}  # "a" no es un número entero positivo
        with self.assertRaises(ValueError):
            contiene_ciclo(graph)

    # 13. Grafo con listas de adyacencia que contienen valores no enteros positivos (debe lanzar ValueError)
    def test_valores_no_enteros_positivos_en_lista(self):
        """Si las listas de adyacencia contienen valores no enteros positivos, debe lanzar ValueError."""
        graph = {1: [2, "a"], 2: [1]}  # "a" no es un número entero positivo
        with self.assertRaises(ValueError):
            contiene_ciclo(graph)

    # 14. Grafo que no es un diccionario (debe lanzar ValueError)
    def test_no_es_diccionario(self):
        """Si el grafo no es un diccionario, debe lanzar ValueError."""
        graph = [(1, [2])]  # No es un diccionario
        with self.assertRaises(ValueError):
            contiene_ciclo(graph)

    # 15. Grafo con ciclos en una estructura compleja (ciclo dentro de un ciclo)
    def test_ciclo_compuesto(self):
        """Un grafo con ciclos dentro de otros ciclos debe retornar True."""
        graph = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 1]}  # Ciclo 1-2-3-4-5-1
        self.assertTrue(contiene_ciclo(graph))

    # 16. Grafo con un ciclo en un componente no conectado con el resto del grafo
    def test_ciclo_en_componente_no_conectado(self):
        """Un ciclo en un componente desconectado debe ser detectado."""
        graph = {1: [2], 2: [1], 3: [4], 4: [3]}  # Dos componentes: (1-2) y (3-4), sin ciclos
        self.assertFalse(contiene_ciclo(graph))

    # 17. Grafo con un ciclo pero no es completamente conectado
    def test_grafo_no_completamente_conectado_con_ciclo(self):
        """Un grafo con ciclos, pero desconectado en algún componente."""
        graph = {1: [2, 3], 2: [1], 3: [1, 2]}  # 1-2-3 (ciclo)
        self.assertTrue(contiene_ciclo(graph))

    # 18. Grafo con grandes componentes, solo para evaluar rendimiento (con ciclo)
    def test_grafo_grande_con_ciclo(self):
        """Evaluamos el rendimiento de la función con un grafo grande con un ciclo."""
        # Crear un grafo no dirigido con 1000 nodos
        graph = {i: [] for i in range(1, 1001)}  # Crear todas las claves de 1 a 1000, inicializadas con listas vacías

        # Conectar cada nodo i con i + 1
        for i in range(1, 1000):  # Hasta el nodo 999
            graph[i].append(i + 1)  # Conectar i a i + 1
            graph[i + 1].append(i)  # Conectar i + 1 a i para que sea no dirigido

        # Agregar el ciclo entre 998 y 1000
        graph[1000].append(998)  # Conectar 1000 a 998
        graph[998].append(1000)  # Conectar 998 a 1000

        # Ahora el grafo tiene un ciclo entre 998, 999, 1000

        self.assertTrue(contiene_ciclo(graph))

    # 19. Grafo desconectado sin ciclo con varias componentes.
    def test_grafo_desconectado_sin_ciclo_varias_componentes(self):
        # Grafo desconectado con múltiples componentes sin ciclo
        grafo = {
            1: [2],  # Componente 1: 1 -> 2
            2: [1, 3],  # Componente 1: 2 -> 1 -> 3
            3: [2],  # Componente 1: 3 -> 2
            4: [5],  # Componente 2: 4 -> 5
            5: [4]  # Componente 2: 5 -> 4
        }
        self.assertFalse(contiene_ciclo(grafo))  # No tiene ciclo


if __name__ == '__main__':
    unittest.main()
