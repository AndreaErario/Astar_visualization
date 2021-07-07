import pygame
from assets.colors import *


class Node(object):
    def __init__(self, win, x, y, size):
        self.win = win
        self.x = x
        self.y = y
        self.size = size
        self.color = WHITE
        self.neighbors = []
        self.came_from = None

    def make_start(self):
        self.color = YELLOW

    def make_end(self):
        self.color = BLUE

    def make_obstacle(self):
        self.color = BLACK

    def reset(self):
        self.color = WHITE

    def make_open(self):
        self.color = GREEN

    def make_closed(self):
        self.color = RED

    def make_path(self):
        self.color = ORANGE

    def is_start(self):
        return self.color == YELLOW

    def is_end(self):
        return self.color == BLUE

    def is_obstacle(self):
        return self.color == BLACK

    def set_neighbors(self, grid):
        col, row = self.x // self.size, self.y // self.size

        if col > 0 and not grid[col - 1][row].is_obstacle():
            self.neighbors.append(grid[col - 1][row])

        if col < len(grid) - 1 and not grid[col + 1][row].is_obstacle():
            self.neighbors.append(grid[col + 1][row])

        if row < len(grid) - 1 and not grid[col][row + 1].is_obstacle():
            self.neighbors.append(grid[col][row + 1])

        if row > 0 and not grid[col][row - 1].is_obstacle():
            self.neighbors.append(grid[col][row - 1])

    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.size, self.size))
        pygame.draw.rect(self.win, GREY, (self.x, self.y, self.size, self.size), 1)
