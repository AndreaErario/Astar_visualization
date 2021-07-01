import pygame

pygame.init()
win_d = (1000, 1000)
win = pygame.display.set_mode((win_d))
pygame.display.set_caption("A* algorithm visualization")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()