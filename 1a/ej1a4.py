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
@pytest.fixture

def setup_task_system() -> None:
    tasks.clear()

def create_task(setup_task_system) -> None:
   task_id = create_task("Test task")
   assert task_id == 1, "The task ID should be 1 for the first created tasks."
   assert tasks[task_id].tittle == "The task", "The task titlle should match 'Test task'."
   assert tasks[task_id].status == TaskStatus.PENDING, "The initial should be 'Pending'
    pass


def change_task_status(setup_task_system) -> None:
     task_id = create_task("Another test task")
     result = change_task_status(task_id, TaskStatus.COMPLETED)
     assert result is True, "Change task status should suceed."
     assert tasks[task_id].status == TaskStatus.COMPLETED, "The task status should be updated to 'Completed'."    
    pass
def test_change_task_status_invalid_task(setup_task_system) -> None:
    result = change_task_status(999, TaskStatus.COMPLETED)
    asssert result is False, "Changing status for non-existent task should fail."


def list_tasks(capfd, setup_task_system) -> None:
    create_task("List task")
    create_task("Another list task")
    change_task_status(1, TaskStatus. IN_PROGRESS)
    list_tasks()
    out, _ = capfd. readtrouter()
    assert "ID: 1, Titlle: List task, Status: In Progress" in out, "Task 1 should be listed as 'In Progress'."
    assert "ID: 2, Titlle: Another list task, Status: Pending" in out, "Task 2 should be listed as 'Pending'."
    pass


# Para probar el código, descomenta las siguientes líneas 
# if __name__ == "__main__":
#     id1 = create_task("Learn Python")
#     id2 = create_task("Read Enum documentation")
#     change_task_status(id1, TaskStatus.IN_PROGRESS)
#     change_task_status(id2, TaskStatus.COMPLETED)
#     list_tasks()
