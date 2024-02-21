from tkinter import Tk, messagebox

import pygame

from config import (
    BOX_HEIGHT,
    BOX_TYPE_TO_COLOR,
    BOX_WIDTH, 
    COLS,
    ROWS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)

from domain.enums.box_type import BoxType
from domain.models.grid import Grid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()
running = True

# create new grid
grid = Grid()
grid.set_matrix()
matrix = grid.get_matrix()

# set source to first cell
source = matrix[0][0]
source.set_box_type(BoxType.SOURCE)

queue = []
queue.append(source)
source.queued = True

start_search  = False
destination_set = False
searching = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            cur_box = matrix[x // BOX_WIDTH][y // BOX_HEIGHT]

            # Draw wall on left click
            if event.buttons[0]:    
                cur_box.set_box_type(BoxType.WALL)
            
            # Set destination on right click
            elif event.buttons[2] and not destination_set:
                cur_box.set_box_type(BoxType.DESTINATION)
                destination_set = True
        
        # Start pathfinder on any key pressed if destination has been set
        if event.type == pygame.KEYDOWN and destination_set:
            start_search = True

    if start_search:
        # Dijkstra's Algorithm to find shortest path between source and destination
        if queue and searching:            
            cur_box = queue.pop(0)
            if cur_box.get_box_type() not in [BoxType.SOURCE, BoxType.DESTINATION]:
                cur_box.set_box_type(BoxType.VISITED)

            if cur_box.get_box_type() == BoxType.DESTINATION:
                searching = False
                while cur_box.prev != source:
                    grid.add_box_to_path(cur_box.prev)
                    cur_box = cur_box.prev
                grid.set_path_found(True)
            else:
                for nei_coord in cur_box.get_neighbor_coords():
                    x, y = nei_coord
                    nei = matrix[x][y]
                    if not nei.queued and not nei.get_box_type() == BoxType.WALL:
                        nei.queued = True
                        nei.prev = cur_box
                        queue.append(nei)
        else:
            if searching:
                Tk().wm_withdraw() # to hide the main window
                messagebox.showinfo('No Solution','No solution exists!')            
                searching =  False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    path = grid.get_path()

    for i in range(ROWS):
        for j in range(COLS):
            cur_box = matrix[i][j]
            cur_box.color(screen, BOX_TYPE_TO_COLOR[cur_box.get_box_type()]) 
            if cur_box in path:
                cur_box.color(screen, "lawngreen") 

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()