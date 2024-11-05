def contiene_ciclo(grafo):
    """
    Verifica si un grafo no dirigido contiene ciclos.

    La función utiliza una búsqueda en profundidad (DFS) para detectar ciclos en un grafo no dirigido.
    Realiza la DFS desde cada nodo no visitado y verifica si existe algún ciclo en el grafo.

    Condiciones Previas:
    - El grafo debe ser representado como un diccionario (dict) donde las claves son enteros mayores que 0
      (representando los nodos) y los valores son listas de enteros mayores que 0, que representan los nodos
      a los que el nodo correspondiente está conectado.
    - El grafo debe ser no dirigido, es decir, si existe una conexión de x a y, también debe existir una
      conexión de y a x. En otras palabras, las listas de adyacencia deben ser simétricas.
    - El grafo puede ser desconectado, por lo que la función realizará una DFS en cada componente conexo.

    Condiciones Posteriores:
    - Retorna True si el grafo contiene al menos un ciclo.
    - Retorna False si el grafo no contiene ciclos.

    Excepciones:
    - Lanza ValueError si el grafo no cumple con las condiciones previas. Esto incluye:
        - Si el grafo no es un diccionario.
        - Si las claves del diccionario no son enteros positivos.
        - Si las listas de adyacencia no contienen solo enteros positivos.
        - Si el grafo contiene conexiones a nodos inexistentes.

    :param grafo: dict
        Un diccionario que representa un grafo no dirigido, donde las claves son nodos (enteros positivos)
        y los valores son listas de nodos (enteros positivos) representando los nodos a los que cada nodo está conectado.

    :return: bool
        Retorna True si el grafo contiene un ciclo, False de lo contrario.
    """

    # Validación del grafo
    if not isinstance(grafo, dict):
        raise ValueError("El grafo debe ser un diccionario.")  # El grafo debe ser un diccionario

    for nodo, vecinos in grafo.items():
        if not isinstance(nodo, int) or nodo <= 0:
            raise ValueError("Las claves del grafo deben ser enteros positivos.")  # El nodo debe ser un número positivo
        if not all(isinstance(vecino, int) and vecino > 0 for vecino in vecinos):
            raise ValueError(
                "Las listas de adyacencia deben contener solo enteros positivos.")  # Las conexiones deben ser enteros positivos
        if any(vecino not in grafo for vecino in vecinos):
            raise ValueError(
                "El grafo contiene conexiones a nodos inexistentes.")  # El grafo no debe tener conexiones inválidas

    # Conjunto de nodos visitados para el recorrido DFS
    visitados = set()

    # Iteramos sobre todos los nodos del grafo
    for nodo in grafo:
        if nodo not in visitados:  # Si el nodo no ha sido visitado aún, iniciamos el recorrido DFS desde él
            pila = [(nodo, None)]  # Usamos una pila para simular el recorrido DFS iterativo
            while pila:
                nodo_actual, padre = pila.pop()  # Extraemos el nodo actual y su nodo padre
                visitados.add(nodo_actual)  # Marcamos el nodo actual como visitado
                for vecino in grafo[nodo_actual]:  # Recorremos los vecinos del nodo actual
                    if vecino not in visitados:  # Si el vecino no ha sido visitado
                        pila.append((vecino, nodo_actual))  # Lo añadimos a la pila para recorrerlo más tarde
                    elif vecino != padre:  # Si encontramos un vecino que ya fue visitado y no es el padre, encontramos un ciclo
                        return True  # Se ha detectado un ciclo
    return False  # Si hemos recorrido todo el grafo sin encontrar ciclos, retornamos False
