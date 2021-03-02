def promptWrongAnswer():
    """ Pedir al usuario que reingrese su respuesta
    Returns:
        string obtenido del input
    """
    print('Respuesta inválida, por favor escoja un número de la lista')
    answer = input()
    return answer


def checkWrongAnswer(answer):
    """ Validar respuesta correcta
    Args:
        answer: respuesta del input
    Returns:
        integer indicando el índice de la ciudad
    """
    try:
        answer = int(answer)
        while answer < 0 or answer > 10:
            res = promptWrongAnswer()
            answer = int(res)
        return answer
    except:
        res = promptWrongAnswer()
        return checkWrongAnswer(res)


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
