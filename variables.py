import math

# Arreglo de ciudades
cities = ['CCS', 'AUA', 'BON', 'CUR', 'SXM',
          'SDQ', 'SBH', 'POS', 'BGI', 'FDF', 'PTP']

# Matriz de Adyacencia de precio de vuelos
flights = [
    [0, 40, 60, 35, math.inf, 180, math.inf, 150, 180, math.inf, math.inf],
    [40, 0, 15, 15, 85, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
    [60, 15, 0, 15, math.inf, math.inf, math.inf,
        math.inf, math.inf, math.inf, math.inf],
    [35, 15, 15, 0, 100, math.inf, math.inf,
        math.inf, math.inf, math.inf, math.inf],
    [math.inf, 85, math.inf, 100, 0, 50, 45, 90, 70, math.inf, 100],
    [180, math.inf, math.inf, math.inf, 50, 0,
        math.inf, math.inf, math.inf, math.inf, math.inf],
    [math.inf, math.inf, math.inf, math.inf, 45,
        math.inf, 0, math.inf, math.inf, math.inf, 80],
    [150, math.inf, math.inf, math.inf, 90, math.inf, math.inf, 0, 35, 75, 80],
    [180, math.inf, math.inf, math.inf, 70, math.inf,
        math.inf, 35, 0, math.inf, math.inf],
    [math.inf, math.inf, math.inf, math.inf,
        math.inf, math.inf, math.inf, 75, math.inf, 0, math.inf],
    [math.inf, math.inf, math.inf, math.inf, 100,
        math.inf, 80, 80, math.inf, math.inf, 0]
]

# Diccionario de Visas
visas = {
    'CCS': False,
    'AUA': True,
    'BON': True,
    'CUR': True,
    'SXM': True,
    'SDQ': True,
    'SBH': False,
    'POS': False,
    'BGI': False,
    'FDF': False,
    'PTP': False
}

# Diccionario de nombres de Ciudades
cityName = {
    'CCS': 'Caracas',
    'AUA': 'Aruba',
    'BON': 'Bonaire',
    'CUR': 'Curazao',
    'SXM': 'San Martín',
    'SDQ': 'Santo Domingo',
    'SBH': 'San Bartolomé',
    'POS': 'Puerto España (Trinidad)',
    'BGI': 'Barbados',
    'FDF': 'Fort de France (Martinica)',
    'PTP': 'Point a Pitre (Guadalupe)'
}

# Diccionario de mensajes
msgs = {
    'msg1': 'Bienvenido a la agencia de viajes Metro Travel',
    'msg2': 'Seleccione la ciudad de origen de su vuelo',
    'msg3': 'Seleccione la ciudad destino de su vuelo',
    'msg4': 'Cuenta usted con VISA?',
    'msg5': 'Qué tipo de ruta desea escoger?'
}
