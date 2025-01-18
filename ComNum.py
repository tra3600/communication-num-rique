def nbCaracteres(c: str, s: str) -> int:
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count

# Exemple d'utilisation
s = 'abaabaca'
print(nbCaracteres('a', s))  # Output: 4
print(nbCaracteres('b', s))  # Output: 2
print(nbCaracteres('c', s))  # Output: 1



def analyseTexte(s: str) -> dict:
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

# Exemple d'utilisation
print(analyseTexte('abracadabra'))  # Output: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

