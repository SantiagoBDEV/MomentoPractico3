class GrafoConPeso:
    def __init__(self, info: list[list]):
        """
        Constructor de la clase Grafo

        :param info: Contiene todas las conexiones del grafo en el formato [Origen, Destino, Peso]

        Condiciones previas:
        - info no puede ser vacío.
        - info debe almacenar listas, y estas listas deben almacenar 3 números enteros todos no negativos.
        - No se puede almacenar el vector 0, esto implica que no puede existir Origen o Destino con valor 0.

        Condiciones posteriores:
        - self.Grafo debe ser un diccionario de la forma {keys: values}
            keys: Cada vector mencionado.
            values: Lista de adyacencia con tuplas de la forma (Destino, Peso) por cada arista de llave (key) a un
                nodo Destino.


        Lanza:
        - Lanza ValueError si:
            - No cumple con las condiciones previas.


        Aclaraciones:
        - La forma de enumerar los nodos es arbitraria al usuario, pero si se usa un número anteriormente no usado se
            entenderá como un nodo nuevo.

        Ejemplo:
        info = [
            [1, 2, 4],  # Arista de 1 a 2 con peso 4
            [1, 3, 1],  # Arista de 1 a 3 con peso 1
            [2, 3, 2],  # Arista de 2 a 3 con peso 2
            [2, 4, 5],  # Arista de 2 a 4 con peso 5
            [3, 4, 8]  # Arista de 3 a 4 con peso 8
        ]

        print(Grafo(info).Grafo)
        > {1: [(2, 4), (3, 1)], 2: [(3, 2), (4, 5)], 3: [(4, 8)], 4: []}
        """
        # Comprobación de que info no está vacío y es una lista
        if not isinstance(info, list) or not info:
            raise ValueError("info debe ser una lista no vacía.")

        self.Grafo = {}

        for conexion in info:
            # Comprobación de que cada conexión es una lista de 3 elementos
            if not (isinstance(conexion, list) and len(conexion) == 3):
                raise ValueError("Cada conexión debe ser una lista de 3 elementos.")

            origen, destino, peso = conexion

            # Comprobación de que todos los elementos son enteros no negativos y que no son cero
            if not (isinstance(origen, int) and origen > 0 and
                    isinstance(destino, int) and destino > 0 and
                    isinstance(peso, int) and peso >= 0):  # El peso puede ser cero
                raise ValueError("Todos los elementos deben ser números enteros positivos, y el peso puede ser cero.")

            # Añadir origen y destino al grafo si no existen
            if origen not in self.Grafo:
                self.Grafo[origen] = []
            if destino not in self.Grafo:
                self.Grafo[destino] = []

            # Agregar la conexión (destino, peso) a la lista de adyacencia del origen
            self.Grafo[origen].append((destino, peso))

