from typing import List

from config import COLS, ROWS
from domain.models.box import Box


class Grid:
    def __init__(self) -> None:
        self.matrix = []
        self.path = []
        self.path_found = False
    
    def set_matrix(self) -> None:
        for i in range(ROWS):
            cur_row = []
            for j in range(COLS):
                cur_box = Box(i, j)
                cur_box.set_neighbor_coords()
                cur_row.append(cur_box)
            self.matrix.append(cur_row)

    def get_matrix(self) -> List:
        return self.matrix

    def add_box_to_path(self, box: Box) -> None:
        self.path.append(box)

    def get_path(self) -> List:
        return self.path if self.path_found else []

    def set_path_found(self, path_found: bool) -> None:
        self.path_found = path_found
    
    def get_path_found(self) -> bool:
        return self.path_found