import pygame
from node import Node
from assets.colors import *
from operator import itemgetter

pygame.init()
win_size = 600
node_size = 15
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption("A* algorithm visualization")

run = True

grid = []
start = ()
end = ()

heuristic = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def a_star():
    open_list = []
    closed_list = []
    g = 0
    open_list.append((heuristic(start, end) + g, grid[start[0]][start[1]]))
    while open_list:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        g += 1
        open_list.sort(key=itemgetter(0))
        current = open_list.pop(0)

        if current[1] == grid[end[0]][end[1]]:
            break

        for x in current[1].neighbors:
            if not x in closed_list:
                open_list.append((heuristic((x.x // node_size, x.y // node_size), end) + g, x))
                if not x == grid[start[0]][start[1]] and not x == grid[end[0]][end[1]]:
                    x.make_open()

        closed_list.append(current[1])
        if not current[1] == grid[start[0]][start[1]] and not current[1] == grid[end[0]][end[1]]:
            current[1].make_closed()

        draw()

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
        if event.type == pygame.KEYDOWN and start and end:
            for x in grid:
                for y in x:
                    y.set_neighbors(grid)
            a_star()
    
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
