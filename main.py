import pygame
from node import Node

pygame.init()
win_size = 600
node_size = 20
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption("A* algorithm visualization")

run = True

grid = []

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
    
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        grid[pos[0] // node_size][pos[1] // node_size].make_obstacle()
    
    draw()

pygame.quit()
