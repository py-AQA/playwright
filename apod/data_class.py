import json
import os
from dataclasses import dataclass
from typing import NamedTuple


def save_json(data, filename: str):
    with open(filename, 'w') as file:
        json.dump(data, file)
    assert os.path.exists(filename), "File was not created successfully"
    return filename


def read_json(filename) -> dict:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


@dataclass
class Settings:
    availableMinutesLate: dict
    workingDays: list
    weekendsDays: list
    locations: [dict]
    schedule: str
    weekendsType: str
    timeSchedules: [dict]
    createdTimeSchedules: [dict]
    defaultTimeSchedule: None
    monthMaxOverwork: str
    dayMaxOverwork: str
    vacationDays: str
    vacationPeriod: str
    maxAbsenceDays: str
    deletedLocations: list
    updatedLocations: list
    createdLocations: list


class Coordinates(NamedTuple):
    name: str
    latitude: float
    longitude: float
    radius: float


def locations() -> Coordinates:
    """Returns coordinates"""
    return Coordinates(name="name1", latitude=1.0, longitude=2.0, radius=3.0)


coordinates = locations()
print(coordinates.longitude)
print(coordinates.latitude)
print(coordinates.radius)

"-------------------------------------------------------------------"
# 2-й Вариант записи
"""class Coordinates2, данные считываются с json файла , строка  "locations": """


class Coordinates2(NamedTuple):
    location = read_json('hand_get_settings.json')['locations']


def locations() -> Coordinates2:
    """Returns coordinates"""
    return Coordinates2.location


coordinates = locations().location
print(coordinates.longitude)
print(coordinates.latitude)
print(coordinates.radius)
"-----------------------------------------------------------------------------------------------------"


def available_minutes_late() -> dict[str, int]:
    time_late = {"availableMinutesLate": 15}
    return time_late


print(available_minutes_late())

"-------------------------------------------------------------------------"


# def working_days() -> list:
"=================================Не лучший вариант ==============================================================="
@dataclass
class Settings2:
    availableMinutesLate: int = 5
    workingDays: list = '["18.06.2024", "19.06.2024"]'
    weekendsDays: list = '["21.06.2024", "27.07.2019"]'
    locations: dict = '"name": "name1", "latitude": 1, "longitude": 2, "radius": 3'
    schedule: str = "5-2"
    weekendsType: str = "customWeekends"
    timeSchedules: dict = ('"id": "aMU2s5Sf", "label": "02:00-05:30", "selected": False, '
                           '\n"id": "x3waPrVE", "label": "02:00-05:30", "selected": False, '
                           '\n"id": "cdPN6eDa", "label": "02:00-05:30", "selected": False, '
                           '\n"id": "VyPmDLMz", "label": "02:00-01:00", "selected": False')

    createdTimeSchedules: dict = ('"id": "aMU2s5Sf", "label": "02:00-05:30", "selected": False, "id": "x3waPrVE", '
                                  '\n"label": "02:00-05:30", "selected": False,'
                                  '\n "id": "cdPN6eDa", "label": "02:00-05:30", "selected": False,'
                                  '\n "id": "VyPmDLMz", "label": "02:00-01:00", "selected": False')
    defaultTimeSchedule: None = None
    monthMaxOverwork: str = "16"
    dayMaxOverwork: str = "17"
    vacationDays: str = "17"
    vacationPeriod: str = "19"
    maxAbsenceDays: str = "20"

    # deletedLocations: list = []  # пустой лист подсвечен ошибкой
    # updatedLocations: list = []
    # createdLocations: list = []


print(Settings2)
