"""
Enunciado:
Desarrolla un sistema de inventario simple para una tienda, utilizando `dataclasses` para modelar los productos y un
diccionario para mantener el inventario. 

Funciones a desarrollar:
- `add_product(name: str, category: str, quantity: int, price: float) -> Product`:
    Descripción:
    Añade un nuevo producto al inventario o actualiza la cantidad y el precio de un producto existente en el
    inventario. Retorna el producto añadido o actualizado.
    Parámetros:
        - `name` (str): Nombre del producto.
        - `category` (str): Categoría del producto.
        - `quantity` (int): Cantidad de unidades del producto.
        - `price` (float): Precio por unidad del producto.

- `list_products() -> str`:
    Descripción:
    Genera y retorna una cadena de texto que lista todos los productos en el inventario, mostrando su nombre,
    categoría, cantidad y precio.
    
- `find_product(name: str, category: str) -> Optional[Product]`:
    Descripción:
    Busca en el inventario un producto por su nombre y categoría. Retorna el producto si se encuentra, o `None` si no
    existe en el inventario.
    Parámetros:
        - `name` (str): Nombre del producto a buscar.
        - `category` (str): Categoría del producto a buscar.

Ejemplo:
    add_product("Apples", "Fruits", 100, 0.50)
    add_product("Pears", "Fruits", 50, 0.70)
    add_product("Apples", "Fruits", 50, 0.55) 

Salida esperada:
- Creación y actualización de productos en el inventario mediante una lista detallada de todos los productos, con sus
nombres, categorías, cantidades y precios.

- Buscar productos específicos en el inventario de una tienda mediante `dataclasses`.
"""

from dataclasses import dataclass
from typing import Dict, Tuple, Optional, List


@dataclass
class Product:
    name: str
    category: str
    quantity: int
    price: float
    

inventory: Dict[Tuple[str, str], Product] = {}


def add_product(name: str, category: str, quantity: int, price: float) -> Product:
    # Complete the code
    
    key = (name, category)
    if key in inventory:
        existing_product = inventory[key]
        existing_product.quantity += quantity
        existing_product.price = price
        return existing_product
    else:
        new_product = Product(name=name, category=category, quantity=quantity, price=price)
        inventory[key] = new_product
        return new_product
    
def list_products() -> str:
    if not inventory:
        return "El inventario está vacío."

    result_lines = []
    
    for product in :
            (f"{product.name} ({product.category}) - {product.quantity} units at ${product.price:.2f} each")
    return "\n". join(result_lines)
        


def find_product(name: str, category: str) -> Optional[Product]:
    key = (name, category)
    return inventory.get(key)


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    print("=== SISTEMA DE INVENTARIO ===\n")
    
    # Añadir productos
    print("Añadiendo productos al inventario...")
    p1 = add_product("Apples", "Fruits", 100, 0.50)
    print(f"  Añadido: {p1.name} - {p1.quantity} unidades a ${p1.price:.2f}")
    
    p2 = add_product("Pears", "Fruits", 50, 0.70)
    print(f"  Añadido: {p2.name} - {p2.quantity} unidades a ${p2.price:.2f}")
    
    # Actualizar producto existente
    p3 = add_product("Apples", "Fruits", 50, 0.55)
    print(f"  Actualizado: {p3.name} - Ahora {p3.quantity} unidades a ${p3.price:.2f}")
    
    # Añadir más productos de diferentes categorías
    add_product("Bananas", "Fruits", 80, 0.30)
    add_product("Milk", "Dairy", 30, 1.20)
    add_product("Cheese", "Dairy", 20, 3.50)
    add_product("Bread", "Bakery", 40, 2.00)
    add_product("Croissant", "Bakery", 25, 1.80)
    
    # Añadir más unidades de un producto existente
    add_product("Milk", "Dairy", 20, 1.25)  # Precio actualizado
    
    print("\n" + list_products())
    
    # Buscar producto específico
    print("\n=== BUSQUEDA DE PRODUCTOS ===")
    found_product = find_product("Apples", "Fruits")
    if found_product:
        print(f"Producto encontrado: {found_product.name} ({found_product.category}) - "
              f"{found_product.quantity} unidades a ${found_product.price:.2f} cada una")
    else:
        print("Producto no encontrado.")
    
    # Buscar producto que no existe
    not_found = find_product("Oranges", "Fruits")
    if not not_found:
        print("Producto 'Oranges' no encontrado en el inventario.")
    
    # Mostrar productos por categoría
    print(list_products_by_category("Fruits"))
    print(list_products_by_category("Dairy"))
    print(list_products_by_category("Bakery"))
