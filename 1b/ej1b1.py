"""
Enunciado:
Desarrolla un conjunto de funciones matemáticas para calcular el máximo común divisor (MCD) y el mínimo común múltiplo
(MCM) de un conjunto de números enteros, mediante la estrategia algoritmica Bottom up.

Funciones a desarrollar:
- `mcd(a: int, b: int) -> int`:
    Descripción:
    Calcula el máximo común divisor de dos números enteros utilizando el algoritmo de Euclides.
    Parámetros:
        - `a` (int): Primer número entero.
        - `b` (int): Segundo número entero.

- `mcd_list(numbers: List[int]) -> int`:
    Descripción:
    Extiende el cálculo del máximo común divisor a una lista de números enteros, aplicando secuencialmente el MCD a
    pares de números de la lista.
    Parámetros:
        - `numbers` (List[int]): Lista de números enteros.

- `mcm(a: int, b: int) -> int`:
    Descripción:
    Determina el mínimo común múltiplo de dos números enteros.
    Parámetros:
        - `a` (int): Primer número entero.
        - `b` (int): Segundo número entero.

- `mcm_list(numbers: List[int]) -> int`:
    Descripción:
    Calcula el mínimo común múltiplo de una lista de números enteros.
    Parámetros:
        - `numbers` (List[int]): Lista de números enteros.

Ejemplo:
    numbers = [4, 6, 8, 20]
    print(f"The GCD of {numbers} is {gcd_list(numbers)}.")
    print(f"The LCM of {numbers} is {lcm_list(numbers)}.")


Salida esperada:
- Cálculo del máximo común divisor y del mínimo común múltiplo de un conjunto de números enteros.
"""

from typing import List


def mcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
        
    return a


def mcd_list(numbers: List[int]) -> int:
    if not numbers:
        return 0
    result =  numbers[0]
    for number in numbers[1:]:
        result = mcd(result, number)
    return result


def mcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)
    


def mcm_list(numbers: List[int]) -> int:
    if not numbers:
        return 0
    result = numbers[0]
    for number in numbers[1:]:
        result = mcm(result, number)
    return result


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    # Pruebas básicas
    print("=== Pruebas de MCD y MCM ===\n")
    
    # Test 1: Dos números
    a, b = 48, 18
    print(f"MCD({a}, {b}) = {mcd(a, b)}")
    print(f"MCM({a}, {b}) = {mcm(a, b)}")
    
    # Test 2: Lista de números
    numbers1 = [12, 18, 24]
    print(f"\nMCD de {numbers1} = {mcd_list(numbers1)}")
    print(f"MCM de {numbers1} = {mcm_list(numbers1)}")
    
    # Test 3: Ejemplo del enunciado
    numbers2 = [4, 6, 8, 20]
    print(f"\nPara {numbers2}:")
    print(f"  MCD = {mcd_list(numbers2)}")
    print(f"  MCM = {mcm_list(numbers2)}")
    
    # Test 4: Casos especiales
    numbers3 = [0, 5, 10]
    print(f"\nCaso especial {numbers3}:")
    print(f"  MCD = {mcd_list(numbers3)}")
    print(f"  MCM = {mcm_list(numbers3)} (0 significa indefinido)")
    
    # Test 5: Números primos
    numbers4 = [7, 13, 19]
    print(f"\nNúmeros primos {numbers4}:")
    print(f"  MCD = {mcd_list(numbers4)} (son primos relativos)")
    print(f"  MCM = {mcm_list(numbers4)} = {7*13*19}")
