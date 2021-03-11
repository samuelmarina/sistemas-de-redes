import math
from variables import cities, visas, flights

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

def printResult(distance, source, target, path):
    """ Imprimir el resultado de la trayectoria y el costo total
    Args:
        distance: arreglo de enteros, cuya posicion coincide
        con la distancia mas corta conocida para llegar a el
        source: integer del índice del nodo origen
        target: integer del índice del nodo destino
        path: arreglo de índices de la trayectoria
    """
    total_cost = distance[target]

    if total_cost != math.inf:
        print('La ruta más corta entre ' +
            cities[source] + ' y ' + cities[target] + ' es:\n')
        printShortestDistance(path)
        print('El precio de viajar por esta trayectoria es de $' + str(total_cost))
    else:
        print('No es posible viajar de ' + cities[source] + ' hasta ' + cities[target])

def needsVisa(index):
    """ Conocer si una ciudad requiere VISA para entrar
    Args:
        index: integer del índice de la ciudad
    Returns:
        boolean indicando si necesita o no VISA
    """

    return visas[cities[index]]

def minDistance(distance, visited, vertices): 
    """ Conocer la menor distancia no visitada
    Args:
        distance: arreglo de enteros, cuya posicion coincide
        con la distancia mas corta conocida para llegar a el
        visited: arreglo booleano, cuya posicion determina
        si un vertice ha sido visitado 
        vertices: integer cantidad de nodos
    Returns:
        integer con la menor distancia 
    """
  
    min = math.inf
    min_distance = 0

    for v in range(vertices): 
        if distance[v] < min and visited[v] == False: 
            min = distance[v] 
            min_distance = v 
  
    return min_distance 
  
def dijkstra(flights, source, target, vertices, flag, pred): 
    """ Algoritmo de Dijkstra para conocer el camino 
    mas corto entre un vertice y otro, 
    para un grafo cuyas aristas tienen peso
    Args:
        flights: matriz de adyacencia
        source: integer del índice del nodo origen
        target: integer del índice del nodo destino
        vertices: integer de la cantidad de nodos
        pred: arreglo de enteros para archivar los predecesores
        flag: boolean que indica si una persona tiene o no VISA 
    Returns:
        arreglo de distancias 
    """

    distance = [math.inf] * vertices
    distance[source] = 0
    visited = [False] * vertices 

    for i in range(vertices):
        pred[i] = -1
  
    for cout in range(vertices):   
        u = minDistance(distance, visited, vertices) 
        visited[u] = True
  
        for v in range(vertices):             
            if not flag and needsVisa(v):                
                continue
            
            if flights[u][v] > 0 and flights[u][v] != math.inf and visited[v] == False and distance[v] > distance[u] + flights[u][v]: 
                distance[v] = distance[u] + flights[u][v] 
                pred[v] = u
  
    return(distance) 
  
def getShortestDijkstra(flights, source, target, vertices, visa):
    """ Construir la distancia mas corta (por peso de las aristas)
    entre dos nodos
    Args:
        flights: matriz de adyacencia
        source: integer del índice del nodo origen
        target: integer del índice del nodo destino
        vertices: integer de la cantidad de nodos
        visa: boolean que indica si una persona tiene o no VISA 
    Returns:
        arreglo de distancias 
    """

    pred = [0 for i in range(vertices)]

    visitedSet = dijkstra(flights, source, target, vertices, visa, pred)

    path = [target]
    dummy = target

    while pred[dummy] != -1:
        path.append(pred[dummy])
        dummy = pred[dummy]

    path.reverse()
    printResult(visitedSet, source, target, path)


getShortestDijkstra(flights, 1, 6, 11, False)