import pygame
from assets.colors import *

class Node(object):
    def __init__(self, win, x, y, size):
        self.win = win
        self.x = x
        self.y = y
        self.size = size
        self.color = WHITE

    def make_obstacle(self):
        self.color = BLACK

    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.size, self.size))
        pygame.draw.rect(self.win, GREY, (self.x, self.y, self.size, self.size), 1)
