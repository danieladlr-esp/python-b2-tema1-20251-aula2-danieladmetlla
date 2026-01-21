"""
Enunciado:
Desarrolla un sistema de gestión de tareas simple en Python, utilizando `Enum` para definir estados de las tareas y
`typing.NamedTuple` para modelar las tareas y tipado estático.

Funciones a desarrollar:
- `create_task(title: str) -> int`:
    Descripción:
    Añade una nueva tarea al sistema con un estado inicial "Pendiente". La función genera un ID único para cada tarea,
    lo asigna junto con el título proporcionado, y retorna el ID de la tarea creada, mantiene la siguiente estructura:
    `tasks[id] = Task(id, title, TaskStatus.PENDING)`.
    Parámetros:
        - `title` (str): El título de la tarea a crear.

- `change_task_status(task_id: int, new_status: TaskStatus) -> bool`:
    Descripción:
    Actualiza el estado de una tarea existente basándose en su ID. Retorna `True` si la operación es exitosa, o `False`
    si la tarea no se encuentra realizada.
    Parámetros:
        - `task_id` (int): El ID de la tarea a actualizar.
        - `new_status` (TaskStatus): El nuevo estado asignado a la tarea.

- `list_tasks() -> None`:
    Descripción:
    Imprime una lista de todas las tareas registradas, manteniendo el siguiente formato: "ID: {task.id},
    Title: {task.title}, Status: {task.status.value}".


Clases y Enums:
- `TaskStatus(Enum)`: Define los posibles estados de una tarea, incluyendo "Pendiente", "En Progreso" y "Completada".
- `Task(typing.NamedTuple)`: Modelo de una tarea, incluyendo campos para ID, título y estado.

Ejemplo:
    id1 = create_task("Learn Python")
    id2 = create_task("Read Enum documentation")
    change_task_status(id1, TaskStatus.IN_PROGRESS)
    change_task_status(id2, TaskStatus.COMPLETED)
    list_tasks()

Salida esperada:
- Creación y actualización exitosa de tareas en el sistema, seguida por una impresión de todas las tareas, mediante
`Enum` para estados de tarea y `typing.NamedTuple` para la estructura de datos de tarea.
"""

from enum import Enum
from typing import NamedTuple, Dict


class TaskStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class Task(NamedTuple):
    id: int
    title: str
    status: TaskStatus
    
    
tasks: Dict[int, Task] = {}
next_id = 1

def create_task(title: str) -> int:
    global next_id, tasks
    new_task = Task(id=next_id, title=title, status=TaskStatus.PENDING)
    task[next_id] = new_task
    current_id = next_id
    next_id += 1
    return current_id

def change_task_status(task_id: int, new_status: TaskStatus) -> bool:
    global tasks
    if task_id not in tasks:
        return False

    current_task = tasks[task_id]
    updated_task = Task(
        id=current_task.id,
        title=current_task.title,
        status=new_status
    )
    tasks[task_id] = updated_task
    return True


def list_tasks() -> None:
    global tasks
    if not tasks:
        print("No hay tareas registradas.")
        return

    print("\n== Lista de tareas ===")
    print("_" * 40)

    for task_id, task in sorted(tasks.items()):
        print(f"ID: {task.id}, Title: {task.title}, status: {task.status.value}")

    print("_" * 40)
    status_counts = {}
    for task in tasks.values():
        status = task.status.value
        status_counts[status] = status_counts.get(status, 0) + 1

    print("\nEstadísticas:")
    for status, count in status_counts.items():
        print(f" {status}: {count} tareas(s)")

# Para probar el código, descomenta las siguientes líneas 
if __name__ == "__main__":
    print("=== Sistema de Gestión de Tareas ===\n")
    
    # Crear tareas
    print("Creando tareas...")
    id1 = create_task("Learn Python")
    print(f"  Tarea creada: ID={id1}, 'Learn Python'")
    
    id2 = create_task("Read Enum documentation")
    print(f"  Tarea creada: ID={id2}, 'Read Enum documentation'")
    
    id3 = create_task("Complete project")
    print(f"  Tarea creada: ID={id3}, 'Complete project'")
    
    id4 = create_task("Write documentation")
    print(f"  Tarea creada: ID={id4}, 'Write documentation'")
    
    # Actualizar estados de tareas
    print("\nActualizando estados de tareas...")
    
    # Cambiar tarea 1 a "En Progreso"
    result1 = change_task_status(id1, TaskStatus.IN_PROGRESS)
    print(f"  Tarea {id1} -> 'In Progress': {'Éxito' if result1 else 'Fallo'}")
    
    # Cambiar tarea 2 a "Completada"
    result2 = change_task_status(id2, TaskStatus.COMPLETED)
    print(f"  Tarea {id2} -> 'Completed': {'Éxito' if result2 else 'Fallo'}")
    
    # Cambiar tarea 3 a "En Progreso"
    result3 = change_task_status(id3, TaskStatus.IN_PROGRESS)
    print(f"  Tarea {id3} -> 'In Progress': {'Éxito' if result3 else 'Fallo'}")
    
    # Intentar cambiar una tarea que no existe
    result4 = change_task_status(999, TaskStatus.COMPLETED)
    print(f"  Tarea 999 -> 'Completed': {'Éxito' if result4 else 'Fallo'} (tarea inexistente)")
    
    # Listar todas las tareas
    print("\nListando todas las tareas:")
    list_tasks()
    
    # Ejemplo adicional: completar más tareas
    print("\nCompletando más tareas...")
    change_task_status(id1, TaskStatus.COMPLETED)
    change_task_status(id3, TaskStatus.COMPLETED)
    change_task_status(id4, TaskStatus.IN_PROGRESS)
    
    # Listar tareas después de cambios
    print("\nListando tareas después de cambios:")
    list_tasks()

