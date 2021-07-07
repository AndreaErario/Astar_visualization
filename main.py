import pygame
from node import Node
from assets.colors import *
from operator import itemgetter

pygame.init() # Initialize pygame module
win_size = 600
node_size = 15
win = pygame.display.set_mode((win_size, win_size)) # Sets the window
pygame.display.set_caption("A* algorithm visualization") # Sets the caption

run = True

grid = []
start = ()
end = ()

heuristic = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) # A function to search the diretion


def a_star():
    open_list = []
    closed_list = []
    path = []
    g = {node: float("inf") for col in grid for node in col} # Assign an infinite value to all nodes
    g[grid[start[0]][start[1]]] = 0
    open_list.append((heuristic(start, end), grid[start[0]][start[1]]))
    while open_list:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        open_list.sort(key=itemgetter(0)) # Sort to nearest values
        current = open_list.pop(0)[1]

        if current == grid[end[0]][end[1]]: # If end reached 
            path.append(current)
            while True:
                x = path[-1].came_from
                if x == None:
                    break
                path.append(x)
            for x in path: # Draws the path
                if not x.is_start() and not x.is_end():
                    x.make_path()
                    draw()
            break

        for x in current.neighbors:
            gt = g[current] + 1
            if gt < g[x]:
                x.came_from = current # Update the path
                g[x] = gt
            if not x in closed_list and not x in open_list:
                open_list.append(
                    (heuristic((x.x // node_size, x.y // node_size), end) + g[x], x)
                ) # Append in the open list
                if not x.is_start() and not x.is_end():
                    x.make_open() # If not start or end make open

        closed_list.append(current)
        if not current.is_start() and not current.is_end():
            current.make_closed() # If not start or end make closed

        draw()


def draw():
    win.fill((0, 0, 0)) # Reset the screen
    for column in grid:
        for node in column:
            node.draw() # Draw all the nodes in the grid
    pygame.display.update()


for x in range(win_size // node_size):
    grid.append([]) # Creates columns
    for y in range(win_size // node_size):
        grid[x].append(Node(win, x * node_size, y * node_size, node_size)) # Fills the columns with nodes

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # Exit the loop
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_s, pygame.K_SPACE]:
                for x in grid:
                    for y in x:
                        y.set_neighbors(grid) # Sets the neighbors for the nodes
                a_star() # Start the algorithm
            if event.key == pygame.K_r:
                start = ()
                end = ()
                for col in grid:
                    for node in col:
                        node.reset() # Reset the grid
            if event.key == pygame.K_c:
                for col in grid:
                    for node in col:
                        if node.color in [RED, GREEN, ORANGE]:
                            node.reset() # Reset the algorithm

    pos = pygame.mouse.get_pos()
    col, row = pos[0] // node_size, pos[1] // node_size

    if pygame.mouse.get_pressed()[0]: # Mouse left button
        if grid[col][row].color == WHITE:
            grid[col][row].make_obstacle()

    elif pygame.mouse.get_pressed()[1]: # Mouse wheel
        if not start and (col, row) != end:
            grid[col][row].make_start()
            start = (col, row)
        elif not end and (col, row) != start:
            grid[col][row].make_end()
            end = (col, row)

    elif pygame.mouse.get_pressed()[2]: # Mouse right button
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
