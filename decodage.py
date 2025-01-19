def codeCar(car: str, g: float, d: float) -> (float, float):
    # Table des fréquences et intervalles
    intervals = {
        'a': (0.0, 0.2),
        'b': (0.2, 0.3),
        'c': (0.3, 0.5),
        'd': (0.5, 0.9),
        'e': (0.9, 1.0)
    }
    
    # Longueur de l'intervalle actuel
    length = d - g
    
    # Calcul des nouvelles bornes
    new_g = g + length * intervals[car][0]
    new_d = g + length * intervals[car][1]
    
    return new_g, new_d

def codage(s: str) -> (float, float):
    g, d = 0.0, 1.0
    
    for car in s:
        g, d = codeCar(car, g, d)
    
    return g, d

# Exemple d'utilisation
s = 'bac'
interval = codage(s)
print(f"Interval for '{s}' is: {interval}")


def decodeCar(x: float, g: float, d: float) -> str:
    intervals = {
        'a': (0.0, 0.2),
        'b': (0.2, 0.3),
        'c': (0.3, 0.5),
        'd': (0.5, 0.9),
        'e': (0.9, 1.0),
        '#': (0.0, 0.0)  # Assuming '#' is at the start
    }
    
    for car, (start, end) in intervals.items():
        if g + (d - g) * start <= x < g + (d - g) * end:
            return car
    return '#'

def decodage(x: float) -> str:
    result = ''
    g, d = 0.0, 1.0
    
    while True:
        car = decodeCar(x, g, d)
        if car == '#':
            break
        result += car
        g, d = codeCar(car, g, d)
    
    return result

# Exemple d'utilisation
x = 0.123
decoded_string = decodage(x)
print(f"Decoded string for x = {x}: {decoded_string}")