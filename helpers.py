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
