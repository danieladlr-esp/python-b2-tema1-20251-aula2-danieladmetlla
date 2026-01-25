"""
Enunciado:
Implementa y compara el rendimiento de dos algoritmos de ordenamiento clásicos con Quicksort y Mergesort, en Python.

Funciones a desarrollar:
- `quicksort(arr: List[int]) -> List[int]`:
    Descripción:
    Ordena una lista de números enteros utilizando el algoritmo Quicksort, dividiendo la lista en subconjuntos menores,
    mayores o iguales a un elemento pivote, y luego ordenando esos subconjuntos recursivamente.
    Parámetros:
        - `arr` (List[int]): Lista de números enteros a ordenar.

- `mergesort(arr: List[int]) -> List[int]`:
    Descripción:
    Ordena una lista de números enteros utilizando el algoritmo Mergesort, dividiendo la lista en mitades hasta obtener
    subconjuntos que se consideran ordenados, para luego mezclar esos subconjuntos de manera ordenada.
    Parámetros:
        - `arr` (List[int]): Lista de números enteros a ordenar.

- `merge(left: List[int], right: List[int]) -> List[int]`:
    Descripción:
    Función auxiliar para el Mergesort que mezcla dos sublistas ordenadas en una sola lista ordenada.
    Parámetros:
        - `left` (List[int]): Sublista izquierda ordenada.
        - `right` (List[int]): Sublista derecha ordenada.

Ejemplo:
    start = time.time()
    sorted_array_quicksort = quicksort(test_array.copy())
    end_time = time.time() - start
    print(f"Quicksort on {size} elements took: {end_time:.5f} seconds.")
    print("First 10 elements after Quicksort:", sorted_array_quicksort[:10])

Salida esperada:
- Demostración del proceso de ordenación de una lista de números enteros con Quicksort y Mergesort, incluyendo la
visualización del tiempo que cada algoritmo toma para ordenar la misma lista.
"""

import random
import time
from typing import List


def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def mergesort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = mergesort(arr[:middle])
    right = mergersort(arr[middle:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000, 10000]  # Diferentes tamaños para comparar
    
    print("=== COMPARACIÓN DE ALGORITMOS DE ORDENAMIENTO ===\n")
    
    for size in sizes:
        # Generar array aleatorio
        test_array = [random.randint(1, 10000) for _ in range(size)]
        
        print(f"\n{'='*60}")
        print(f"Tamaño del array: {size} elementos")
        print(f"{'='*60}")
        
        # Imprimir primeros elementos del array original
        if size <= 100:
            print(f"Array original (primeros 10): {test_array[:10]}")
        
        # Quicksort
        test_copy = test_array.copy()
        start = time.time()
        sorted_quicksort = quicksort(test_copy)
        quicksort_time = time.time() - start
        
        # Verificar que esté ordenado
        is_sorted_q = all(sorted_quicksort[i] <= sorted_quicksort[i+1] 
                         for i in range(len(sorted_quicksort)-1))
        
        # Mergesort
        test_copy = test_array.copy()
        start = time.time()
        sorted_mergesort = mergesort(test_copy)
        mergesort_time = time.time() - start
        
        # Verificar que esté ordenado
        is_sorted_m = all(sorted_mergesort[i] <= sorted_mergesort[i+1] 
                         for i in range(len(sorted_mergesort)-1))
        
        # Mostrar resultados
        print(f"\nQUICKSORT:")
        print(f"  Tiempo: {quicksort_time:.6f} segundos")
        print(f"  Correctamente ordenado: {'✓' if is_sorted_q else '✗'}")
        if size <= 100:
            print(f"  Resultado (primeros 10): {sorted_quicksort[:10]}")
        
        print(f"\nMERGESORT:")
        print(f"  Tiempo: {mergesort_time:.6f} segundos")
        print(f"  Correctamente ordenado: {'✓' if is_sorted_m else '✗'}")
        if size <= 100:
            print(f"  Resultado (primeros 10): {sorted_mergesort[:10]}")
        
        # Comparación
        time_diff = mergesort_time - quicksort_time
        if time_diff > 0:
            print(f"\nQuicksort fue {time_diff/quicksort_time:.2f}x más rápido")
        else:
            print(f"\nMergesort fue {-time_diff/mergesort_time:.2f}x más rápido")
    
    # Comparación adicional con Python built-in
    print(f"\n{'='*60}")
    print("COMPARACIÓN CON SORTED() DE PYTHON")
    print(f"{'='*60}")
    
    size = 10000
    test_array = [random.randint(1, 10000) for _ in range(size)]
    
    start = time.time()
    python_sorted = sorted(test_array.copy())
    python_time = time.time() - start
    
    print(f"Python sorted() en {size} elementos: {python_time:.6f} segundos")
    print("(Basado en Timsort, un algoritmo híbrido)")
