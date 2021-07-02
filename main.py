import pygame
from node import Node
from assets.colors import *

pygame.init()
win_size = 600
node_size = 15
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption("A* algorithm visualization")

run = True

grid = []
start = ()
end = ()

def draw():
    win.fill((0, 0, 0))
    for column in grid:
        for node in column:
            node.draw()
    pygame.display.update()

for x in range(win_size//node_size):
        grid.append([])
        for y in range(win_size//node_size):
            grid[x].append(Node(win, x * node_size, y * node_size, node_size))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pos = pygame.mouse.get_pos()
    col, row = pos[0] // node_size, pos[1] // node_size
    
    if pygame.mouse.get_pressed()[0]:
        if grid[col][row].color == WHITE:
            grid[col][row].make_obstacle()
    
    elif pygame.mouse.get_pressed()[1]:
        if not start and (col, row) != end:
            grid[col][row].make_start()
            start = (col, row)
        elif not end and (col, row) != start:
            grid[col][row].make_end()
            end = (col, row)

    elif pygame.mouse.get_pressed()[2]:
        if (col, row) == start:
            grid[start[0]][start[1]].reset()
            start = ()
        elif (col, row) == end:
            grid[end[0]][end[1]].reset()
            end = ()
        else:
            grid[col][row].reset()
    
    draw()

pygame.quit()
