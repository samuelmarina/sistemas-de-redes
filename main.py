from variables import cities, flights, visas, cityName, msgs as M, adjList
from helpers import checkWrongAnswer, hasVisa, checkWrongAnswer2
from BFS import getShortestDistance
from dijkstra import getShortestDijkstra


def printCities():
    """ Imprimir el arreglo de ciudades
    """
    for x in range(len(cities)):
        print(str(x) + ' - ' + cities[x])


def printWelcomeMessage():
    """ Imprimir el mensaje de bienvenida
    """
    print(M['msg1'] + '\n' + M['msg2'])
    printCities()


def requestInput():
    """ Pedir al usuario la información para su vuelo
    Returns:
        diccionario con los índices de las ciudades escogidas, si el usuario
        cuenta o no con visa, y la ruta que desea escoger
    """
    L = len(cities)
    origin = input()
    origin = checkWrongAnswer2(origin)
    target = input(M['msg3'] + '\n')
    target = checkWrongAnswer2(target)
    visa_res = input(M['msg4'] + '\n')
    visa = hasVisa(visa_res)
    route = input(M['msg5'] + '\n')
    route = checkWrongAnswer(route, 1, 2)
    return {'origin': origin, 'target': target, 'visa': visa, 'route': route}


def start():
    printWelcomeMessage()
    response = requestInput()
    origin = response['origin']
    target = response['target']
    visa = response['visa']
    route = response['route']
    if route == 1:
        getShortestDistance(adjList, origin, target, 11, visa)
    else:
        getShortestDijkstra(origin, target, 11, visa)


start()
