import pygame
import math
import time
import os
import re

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


class rect(pygame.Rect):

    def __init__(self, X, Y, W, L, window, Color):
        super().__init__(X, Y, W, L)
        self.c = Color
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, self.c, self)


class ArrayVisualizer():
    def __init__(self):
        pass

    def DrawArray(self, window, color, arr, currentBar):
        BarWidth = window.get_size()[1] / len(arr)
        Height = window.get_size()[0]

        IncrementSize = Height // (max(arr) - min(arr))

        for i in range(len(arr)):
            if i == currentBar:
                Bar = rect(i * BarWidth,
                           Height - (arr[i] * IncrementSize), BarWidth, arr[i] * IncrementSize, window, BLUE)
            else:

                Bar = rect(i * BarWidth,
                           Height - (arr[i] * IncrementSize), BarWidth, arr[i] * IncrementSize, window, color)
            Bar.draw()

        pygame.display.update()
