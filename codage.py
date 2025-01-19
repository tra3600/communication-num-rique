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