from variables import cities


def promptWrongAnswer(msg):
    """ Pedir al usuario que reingrese su respuesta
    Returns:
        string obtenido del input
    """
    print(msg)
    answer = input()
    return answer


def checkWrongAnswer(answer, start, stop):
    """ Validar respuesta correcta de selección de lista
    Args:
        answer: string respuesta del input
        start: integer indicando el mínimo valor de la respuesta
        stop: integer indicando el máximo valor de la respuesta
    Returns:
        integer indicando el índice de la ciudad
    """
    try:
        answer = int(answer)
        while answer < start or answer > stop:
            res = promptWrongAnswer(
                'Respuesta inválida, por favor escoja un número de la lista')
            answer = int(res)
        return answer
    except:
        res = promptWrongAnswer(
            'Respuesta inválida, por favor escoja un número de la lista')
        return checkWrongAnswer(res, start, stop)


def checkWrongAnswer2(answer):
    """ Validar respuesta correcta de selección de una ciudad
    Args:
        answer: string respuesta del input
    Returns:
        integer indicando el índice de la ciudad
    """
    if answer.upper() not in cities:
        res = promptWrongAnswer(
            'Respuesta inválida, por favor escriba una ciudad válida')
        return checkWrongAnswer2(res)
    return getCityIndex(answer.upper())


def getCityIndex(city):
    """ Conseguir el índice de la ciudad en el arreglo
    Returns:
        integer indicando el índice de la ciudad
    """
    return cities.index(city)


def isSameCity(origin, target):
    """ Verificar si las respuestas son iguales
    Args:
        origin: integer indicando el índice de la ciudad de origen
        target: integer indicando el índice de la ciudad de destino
    Returns:
        True si origin == target, False si lo contrario
    """
    return True if origin == target else False


def hasVisa(res):
    """ Conocer si la persona tiene o no VISA
    Args:
        res: string 'y' ó 'n'
    Returns:
        boolean indicando la respuesta
    """
    res = res.lower()
    return True if res == 's' else False
