class UnionFind:
    """
    Implementa la estructura de datos Union-Find (Disjoint Set Union - DSU) con optimizaciones.
    Permite gestionar conjuntos disjuntos de nodos y realizar las operaciones de unión y búsqueda.

    :param n: El número de nodos (enteros positivos) en el conjunto.
        - n debe ser un entero positivo que representa la cantidad de nodos.

    :return: No retorna ningún valor. Inicializa la estructura con n nodos.

    Condiciones Previas:
    - n debe ser un entero positivo.
    """

    def __init__(self, n):
        if n <= 0:
            raise ValueError("El número de nodos debe ser un entero positivo.")
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """
        Encuentra el representante (raíz) del conjunto al que pertenece el nodo x,
        con compresión de caminos para mejorar la eficiencia.

        :param x: Nodo del cual se quiere encontrar el representante.
        :return: El índice del representante del conjunto que contiene a x.

        Condiciones Previas:
        - x debe ser un entero dentro del rango [0, n-1].
        """
        if self.parent[x] != x:
            # Comprimir el camino durante la búsqueda
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Une los conjuntos de los nodos x y y utilizando la técnica de unión por rango.

        :param x: Nodo 1 a unir.
        :param y: Nodo 2 a unir.
        :return: True si se realizó la unión (es decir, x y y estaban en conjuntos diferentes).
                 False si los nodos ya están en el mismo conjunto.

        Condiciones Previas:
        - x y y deben ser enteros dentro del rango [0, n-1].
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Unión por rango: el conjunto con menor altura se convierte en hijo del conjunto con mayor altura
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False


def kruskal(grafo):
    """
    Implementa el algoritmo de Kruskal para encontrar el Árbol Generador Mínimo (AGM) de un grafo no dirigido ponderado.

    :param grafo: Lista de tuplas (Nodo1, Nodo2, Peso), cada tupla representa una arista.
        - El grafo es no dirigido, es decir, (Nodo1, Nodo2, Peso) es equivalente a (Nodo2, Nodo1, Peso).
        - Las aristas deben estar ponderadas con un valor numérico entero no negativo.

    :return: Lista de tuplas (Nodo1, Nodo2, Peso) que representan las aristas del Árbol Generador Mínimo.

    Lanza:
    - ValueError si el grafo no es válido:
        - No es una lista.
        - Alguna tupla no tiene tres elementos.
        - Los nodos o el peso no son enteros o son negativos.
        - El grafo no es conexo.

    Condiciones Previas:
    - El grafo debe ser conexo y estar representado como una lista de aristas con nodos numerados a partir de 1.

    Condiciones Posteriores:
    - Se retorna una lista de aristas que forman el Árbol Generador Mínimo.
    """
    # Validación del formato del grafo
    if not isinstance(grafo, list):
        raise ValueError("El grafo debe ser una lista.")

    if len(grafo) == 0:
        return []

    # Validar que todas las aristas son tuplas de tres elementos
    for arista in grafo:
        if not isinstance(arista, tuple) or len(arista) != 3:
            raise ValueError("Cada arista debe ser una tupla (Nodo1, Nodo2, Peso).")
        if not all(isinstance(x, int) for x in arista):
            raise ValueError("Cada elemento de la arista debe ser un número entero.")
        nodo1, nodo2, peso = arista
        if nodo1 <= 0 or nodo2 <= 0 or peso < 0:
            raise ValueError("Los nodos y el peso deben ser enteros positivos.")

    # Determinar el número total de nodos a partir de las aristas
    nodos = set()
    for nodo1, nodo2, _ in grafo:
        nodos.add(nodo1)
        nodos.add(nodo2)

    n = len(nodos)  # Número de nodos distintos en el grafo

    # Si el grafo tiene solo un nodo, no necesita aristas
    if n == 1:
        return []

    # Si el grafo no tiene suficientes aristas para ser conexo, no puede haber un AGM
    if len(grafo) < n - 1:
        raise ValueError("El grafo no es conexo, no se puede obtener un Árbol Generador Mínimo.")

    # Crear el objeto Union-Find
    uf = UnionFind(n)

    # Ordenar las aristas por peso (de menor a mayor)
    grafo.sort(key=lambda x: x[2])

    resultado = []
    for nodo1, nodo2, peso in grafo:
        # Usar Union-Find para agregar las aristas sin formar ciclos
        if uf.union(nodo1 - 1, nodo2 - 1):  # Restamos 1 porque los nodos son positivos
            resultado.append((nodo1, nodo2, peso))

    # Verificar si el grafo es conexo
    if len(resultado) != n - 1:
        raise ValueError("El grafo no es conexo, no se puede obtener un Árbol Generador Mínimo.")

    return resultado
