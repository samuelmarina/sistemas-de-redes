from variables import cities, visas, flights


def BFS(adj, source, target, vertices, pred, flag):
    """ Algoritmo Breadth-First para conseguir si existe un camnino entre
    dos nodos
    Args:
        adj: lista de adyacencia
        source: integer del índice del nodo origen
        target: integer del índice del nodo destino
        vertices: integer de la cantidad de nodos
        pred: arreglo de enteros para archivar los predecesores
        flag: boolean que indica si una persona tiene o no VISA
    Returns
        boolean indicando si existe o no un camino
    """
    if not flag and needsVisa(target):
        return False

    visited = [False] * vertices
    queue = []

    for i in range(vertices):
        pred[i] = -1

    visited[source] = True
    queue.append(source)

    while queue:
        u = queue.pop(0)

        for i in range(len(adj[u])):
            curr = adj[u][i]

            if(not visited[curr]):
                visited[curr] = True
                if not flag and needsVisa(curr):
                    continue
                pred[curr] = u
                queue.append(curr)

                if curr == target:
                    return True

    return False


def needsVisa(index):
    """ Conocer si una ciudad requiere VISA para entrar
    Args:
        index: integer del índice de la ciudad
    Returns:
        boolean indicando si necesita o no VISA
    """

    return visas[cities[index]]


def printShortestDistance(path):
    """ Imprimir la ruta obtenida
    Args:
        path: arreglo de índices de la trayectoria
    """
    for i in range(len(path)):
        city = cities[path[i]]
        if i == len(path) - 1:
            print(city)
        else:
            print(city, end=' -> ')


def getTotalCost(path):
    """ Obtener el precio total al viajar por la trayectoria
    Args:
        path: arreglo de índices de la trayectoria
    Returns
        integer indicando el costo total
    """
    total_cost = 0
    for x in range(1, len(path)):
        total_cost += flights[path[x-1]][path[x]]
    return total_cost


def printResult(path, source, target):
    """ Imprimir el resultado de la trayectoria y el costo total
    Args:
        path: arreglo de índices de la trayectoria
        source: integer del índice del nodo origen
        target: integer del índice del nodo destino
    """
    total_cost = getTotalCost(path)
    print('La ruta más corta entre ' +
          cities[source] + ' y ' + cities[target] + ' es:\n')
    printShortestDistance(path)
    print('El precio de viajar por esta trayectoria es de $' + str(total_cost))


def getShortestDistance(adj, source, target, vertices, visa):
    """ Conseguir la distancia más corta (en cantidad de nodos) entre
    dos nodos
    Args:
        adj: lista de adyacencia
        source: integer del índice del nodo origen
        target: integer del índice del nodo destino
        vertices: integer de la cantidad de nodos
        visa: boolean que indica si una persona tiene o no VISA
    """
    pred = [0 for i in range(vertices)]
    if not BFS(adj, source, target, vertices, pred, visa):
        return print('No existe un camino entre ' +
                     cities[source] + ' y ' + cities[target])

    path = [target]
    dummy = target

    while pred[dummy] != -1:
        path.append(pred[dummy])
        dummy = pred[dummy]

    path.reverse()
    printResult(path, source, target)
