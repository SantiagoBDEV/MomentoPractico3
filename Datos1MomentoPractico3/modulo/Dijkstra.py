import heapq
from collections import deque

def validar_grafo(grafo, nodo_inicio):
    """
    Valida que el grafo tenga la estructura adecuada.

    La función valida que el grafo esté representado correctamente como un diccionario donde las claves son enteros
    positivos y los valores son listas de tuplas `(destino, peso)`, asegurándose de que el destino sea un nodo válido
    y el peso sea un número no negativo. También valida que el nodo de inicio esté presente en el grafo.

    Condiciones Previas:
    - El parámetro `grafo` debe ser un diccionario donde las claves son enteros positivos y los valores son listas de
      tuplas `(destino, peso)`, donde:
        - `destino` debe ser un entero positivo.
        - `peso` debe ser un número no negativo (entero o flotante).
        - Las tuplas deben estar correctamente formateadas, es decir, cada arista debe ser una tupla de longitud 2.
        - No puede haber aristas duplicadas entre el mismo par de nodos.
    - El parámetro `nodo_inicio` debe ser un entero positivo y debe existir como clave en el grafo.

    Condiciones Posteriores:
    - Lanza excepciones `ValueError` si alguna de las condiciones previas no se cumple. Las excepciones específicas se describen a continuación:
        - Si el grafo no es un diccionario.
        - Si las claves del grafo no son enteros positivos.
        - Si las aristas no están en formato de tupla `(destino, peso)`.
        - Si algún destino o peso no es un número positivo según la definición.
        - Si se encuentran aristas duplicadas entre nodos.
        - Si el nodo de inicio no está presente en el grafo.

    Excepciones:
    - Lanza `ValueError` si el grafo no cumple con las condiciones mencionadas o si el nodo de inicio no existe en el grafo.

    :param grafo: dict
        Un diccionario que representa el grafo, donde las claves son nodos (enteros positivos) y los valores son listas
        de aristas, cada una representada como una tupla `(destino, peso)`.
    :param nodo_inicio: int
        Un nodo de inicio en el grafo, el cual debe existir como una clave válida.

    :return: None
        La función no retorna ningún valor, pero lanza excepciones si el grafo es inválido.
"""

    if not isinstance(grafo, dict):
        raise ValueError("El grafo debe ser un diccionario.")

    for origen, aristas in grafo.items():
        if not isinstance(origen, int) or origen <= 0:
            raise ValueError(f"Las llaves del grafo deben ser enteros positivos. Error en el nodo: {origen}")

        if not isinstance(aristas, list):
            raise ValueError(f"Las aristas de cada nodo deben estar en una lista. Error en el nodo: {origen}")

        destinos_vistos = set()
        for elemento in aristas:
            if not isinstance(elemento, tuple) or len(elemento) != 2:
                raise ValueError(
                    f"Cada arista debe ser una tupla de 2 elementos (destino, peso). Error en la arista: ({origen}, {elemento})")
            destino, peso = elemento
            if not isinstance(destino, int) or destino <= 0:
                raise ValueError(f"El destino debe ser un entero positivo. Error en la arista: ({origen}, {destino})")
            if not isinstance(peso, (int, float)) or peso < 0:
                raise ValueError(
                    f"El peso de la arista debe ser un número no negativo. Error en la arista: ({origen}, {destino}, {peso})")
            if destino in destinos_vistos:
                raise ValueError(f"Existen múltiples aristas del nodo {origen} al nodo {destino}.")
            destinos_vistos.add(destino)

    if nodo_inicio not in grafo:
        raise ValueError(f"El nodo de inicio {nodo_inicio} debe ser una llave válida en el grafo.")


def verificar_conectividad(grafo, nodo_inicio):
    """
    Verifica que el grafo sea conexo desde un nodo de inicio dado.

    La función utiliza una búsqueda en amplitud (BFS) para verificar la conectividad del grafo desde el nodo de inicio.
    Si todos los nodos son alcanzables desde el nodo de inicio, se considera que el grafo es conexo.

    Condiciones Previas:
    - El parámetro `grafo` debe ser un diccionario de la forma descrita en `validar_grafo`.
    - El `nodo_inicio` debe existir como clave en el grafo.

    Condiciones Posteriores:
    - Retorna `True` si el grafo es conexo desde el nodo de inicio (es decir, si todos los nodos son alcanzables desde
      el nodo de inicio).
    - Retorna `False` si el grafo no es conexo, es decir, si existen nodos que no son alcanzables desde el nodo de inicio.

    Excepciones:
    - Lanza `ValueError` si el `nodo_inicio` no existe en el grafo.

    :param grafo: dict
        Un diccionario que representa el grafo, donde las claves son nodos y los valores son listas de aristas.
    :param nodo_inicio: int
        Un nodo de inicio desde el cual se verifica la conectividad.

    :return: bool
        Retorna `True` si el grafo es conexo desde el nodo de inicio, `False` de lo contrario.
"""

    if nodo_inicio not in grafo:
        raise ValueError(f"El nodo de inicio {nodo_inicio} no existe en el grafo.")

    # Usamos BFS (Búsqueda en amplitud) para verificar la conectividad
    visitados = set()
    cola = deque([nodo_inicio])  # Cola para BFS (búsqueda en amplitud)

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, _ in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

    # Si la cantidad de nodos visitados es igual al tamaño del grafo, es conexo
    return len(visitados) == len(grafo)


def dijkstra(grafo, nodo_inicio):
    """
    Calcula las distancias más cortas desde el nodo nodo_inicio a todos los demás nodos del grafo utilizando el
    algoritmo de Dijkstra.

    La función utiliza Dijkstra para calcular las distancias más cortas desde un nodo de inicio a todos los nodos
    alcanzables del grafo. Si el grafo no es conexo, se lanzará una excepción.

    Condiciones Previas:
    - El parámetro `grafo` debe ser un diccionario de la forma descrita en `validar_grafo`, con cada nodo mapeado a
      una lista de aristas representadas como tuplas `(destino, peso)`.
    - El `nodo_inicio` debe existir como clave en el grafo.

    Condiciones Posteriores:
    - Retorna un diccionario donde las claves son los nodos alcanzables desde el `nodo_inicio` y los valores son las
      distancias más cortas desde el nodo de inicio hasta esos nodos.
    - Si el grafo no es conexo, lanza una excepción `ValueError`.

    Excepciones:
    - Lanza `ValueError` si el grafo es disconexo, es decir, si no todos los nodos son alcanzables desde el nodo de inicio.

    :param grafo: dict
        Un diccionario que representa el grafo, donde las claves son nodos y los valores son listas de tuplas `(destino, peso)`.
    :param nodo_inicio: int
        El nodo desde el cual se calcularán las distancias más cortas.

    :return: dict
        Un diccionario donde las claves son los nodos alcanzables desde el nodo de inicio y los valores son las distancias más cortas a esos nodos.
"""

    # Validaciones
    validar_grafo(grafo, nodo_inicio)
    if not verificar_conectividad(grafo, nodo_inicio):
        raise ValueError("El grafo es disconexo; no todos los nodos son alcanzables desde el nodo de inicio.")

    # Inicialización de distancias y cola de prioridad
    distancias = {nodo: float('inf') for nodo in grafo}  # Inicialización con 'inf' para todos los nodos
    distancias[nodo_inicio] = 0  # Distancia al nodo de inicio es 0
    cola_prioridad = [(0, nodo_inicio)]  # Cola de prioridad con el nodo de inicio
    visitados = set()

    # Dijkstra con optimización (usando heap para cola de prioridad)
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Si el nodo ya fue visitado con una distancia más corta, continuamos
        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        for destino, peso in grafo[nodo_actual]:
            # Relajar las aristas
            distancia_nueva = distancia_actual + peso
            if distancia_nueva < distancias[destino]:
                distancias[destino] = distancia_nueva
                heapq.heappush(cola_prioridad, (distancia_nueva, destino))

    # Filtramos los nodos inalcanzables (con distancia infinita)
    return {nodo: dist for nodo, dist in distancias.items() if dist < float('inf')}

