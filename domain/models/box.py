from typing import List, Tuple

import pygame

from config import BOX_HEIGHT, BOX_WIDTH, COLS, ROWS
from domain.enums.box_type import BoxType


class Box:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.type = BoxType.UNSET
        self.neighbors = []
        self.queued = False
        # If this box is in the found path, what is the previous box in the path
        self.prev = None
        
    def color(self, surface: pygame.Surface, color: str) -> None:
        pygame.draw.rect(surface, color, pygame.Rect((self.x * BOX_WIDTH, self.y * BOX_HEIGHT), (BOX_WIDTH - 2, BOX_HEIGHT - 2)))

    def set_neighbor_coords(self) -> None:
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x = self.x + dx
            y = self.y + dy
            if x in range(ROWS) and y in range(COLS):
                self.neighbors.append((x, y))
    
    def get_neighbor_coords(self) -> List[Tuple[int, int]]:
        return self.neighbors

    def set_box_type(self, type: BoxType) -> None:
        self.type = type

    def get_box_type(self) -> None:
        return self.type
