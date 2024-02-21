from enum import Enum


class BoxType(Enum):
    UNSET = 0
    SOURCE = 1
    DESTINATION = 2
    WALL = 3
    VISITED = 4