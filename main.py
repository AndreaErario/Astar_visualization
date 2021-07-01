import pygame
from node import Node

pygame.init()
win_size = 600
node_size = 20
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption("A* algorithm visualization")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for x in range(win_size//node_size):
        for y in range(win_size//node_size):
            Node(win, x * node_size, y * node_size, node_size).draw()
    pygame.display.update()

pygame.quit()