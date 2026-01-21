"""
Enunciado:
Desarrolla un conjunto de funciones para gestionar eventos en diferentes zonas horarias, facilitando la creación,
manipulación y consulta de eventos programados utilizando Python, con especial énfasis en el manejo de fechas, horas y
zonas horarias mediante datetime y pytz.

Funciones a desarrollar:
- `create_event(name: str, datetime_start: datetime, timezone_str: str) -> Dict[str, str]`:
    Descripción:
    Crea un diccionario representando un evento, incluyendo su nombre, fecha y hora de inicio, y zona horaria.
    Parámetros:
        - `name` (str): Nombre del evento.
        - `datetime_start` (datetime): Fecha y hora de inicio del evento.
        - `timezone_str` (str): Identificador de la zona horaria del evento.

- `time_until_event(event: Dict[str, str]) -> timedelta`:
    Descripción:
    Calcula el tiempo restante hasta el inicio de un evento dado.
    Parámetros:
        - `event` (Dict[str, str]): Evento para calcular el tiempo restante.

- `change_event_timezone(event: Dict[str, str], new_timezone_str: str) -> Dict[str, str]`:
    Descripción:
    Cambia la zona horaria de un evento existente a una nueva especificada.
    Parámetros:
        - `event` (Dict[str, str]): Evento a modificar.
        - `new_timezone_str` (str): Nueva zona horaria.

- `find_next_event(events: List[Dict[str, str]]) -> Optional[Dict[str, str]]`:
    Descripción:
    Identifica el próximo evento entre una lista de eventos, considerando la fecha y hora actual.
    Parámetros:
        - `events` (List[Dict[str, str]]): Lista de eventos entre los cuales buscar el próximo evento.

Ejemplo:

    event1 = create_event("Global Meeting", datetime(2024, 9, 10, 10, 0), "UTC")
    
    time_to_event = time_until_event(event)
    print(f"Time until '{event['name']}':", time_to_event)

    changed_event1 = change_event_timezone(event1, "America/New_York")
    print(f"Event after timezone change: {changed_event1}")

    next_event = find_next_event(events)
    print("\nThe next event is:", next_event["name"])

Salida esperada:
- Crear eventos con sus respectivas zonas horarias.
     {'name': 'Global Meeting', 'datetime_start': datetime.datetime(2024, 9, 10, 10, 0), 'timezone': 'UTC'}

- Mostrar el tiempo restante hasta el inicio de cada uno de los eventos.
    "Time until 'Global Meeting': 1 day, 20:00:00"

- Cambiar dinámicamente la zona horaria de un evento.
    "Event after timezone change: {'name': 'Global Meeting', 'datetime_start': datetime.datetime(2024, 9, 10, 6, 0,
        tzinfo=<DstTzInfo 'America/New_York' EDT-1 day, 20:00:00 DST>), 'timezone': 'America/New_York'}"

- Calcular cuál será el siguiente evento.
    "The next event is: Global Meeting"
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pytz


def create_event(name: str, datetime_start: datetime, timezone_str: str) -> Dict[str, str]:
    timezone = pytz.timezone(timezone_str)
    localized_datetime = datetime_start.replace(tzinfo=timezone)
    return {
        "name": name,
        "datetime_start": localized_datetime,
        "timezone": timezone_str


def time_until_event(event: Dict[str, str]) -> timedelta:
    event_timezone = pytz.timezone(event["timezone"])
    event_datetime = event["datetime_start"]
    if event_datetime.tzinfo is none:
        event_datetime = event_timezone.localize(event_datetime)

    current_datetime = datetime.now(event_timezone)
    
    return event_datetime - current_datetime


def change_event_timezone(event: Dict[str, str], new_timezone_str: str) -> Dict[str, str]:
    new_event = event.copy()
    
    old_timezone = pytz.timezone(event["timezone"])
    new_timezone = pytz.timezone(new_timezone_str)

    event_datetime = event["datetime_start"]

    if event_datetime.tzinfo is None:
        event_datetime = old_timezone.localize(event_datetime)

    new_datetime = event_datetime.astimezone(new_timezone)
    new_event["datatime_start"] = new_datetime
    new_event["timezone"] = new_timezone-str

    return new_event


def find_next_event(events: List[Dict[str, str]]) -> Optional[Dict[str, str]]:
    current_utc = datetime.now(pytz.UTC)

    next_event = None
    min_time_diff = None

    for event in events:
        event_datetime = event["datetime_start"]
        if event_datetime.tzinfo is not None:
            event_utc = event_datetime.astimezone(pytz.UTC)

        else:

            timezone = pytz.timezone(event["timezone"])
            event_utc = timezone.localize(event_datetime).astimezone(pytz.UTC)

    time_diff = event_utc - current_utc
    if time_diff.total_seconds() > 0:
        if min_time_diff is None or time_diff < min_time_diff:
            min_time_diff = time_diff
            next_event = event
            
    return next_event

# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    # Crear eventos de ejemplo
    event1 = create_event("Global Meeting", datetime(2024, 9, 10, 10, 0), "UTC")
    event2 = create_event("Python Talk", datetime(2024, 9, 10, 18, 30), "America/New_York")
    event3 = create_event("Data Science Workshop", datetime(2024, 9, 10, 12, 0), "Europe/London")

    print("Eventos creados:")
    for event in [event1, event2, event3]:
        print(f"  {event['name']}: {event['datetime_start']} ({event['timezone']})")
    
    print("\nTiempo hasta cada evento:")
    for event in [event1, event2, event3]:
        time_to_event = time_until_event(event)
        print(f"Time until '{event['name']}': {time_to_event}")

    print("\nCambio de zona horaria:")
    changed_event1 = change_event_timezone(event1, "America/New_York")
    print(f"Event after timezone change: {changed_event1}")

    print("\nBuscar próximo evento:")
    events = [event1, event2, event3]
    next_event = find_next_event(events)
    if next_event:
        print(f"The next event is: {next_event['name']}")
        print(f"  Scheduled at: {next_event['datetime_start']} ({next_event['timezone']})")
    else:
        print("There are no future events.")


