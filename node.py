import pygame

class Node(object):
    def __init__(self, win, x, y, size):
        self.win = win
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 255, 255)

    def make_obstacle(self):
        self.color = (0, 0, 0)

    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.size, self.size))
        pygame.draw.rect(self.win, (96, 96, 96), (self.x, self.y, self.size, self.size), 1)
