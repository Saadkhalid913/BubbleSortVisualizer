import pygame
from ScreenInitialization import ArrayVisualizer
import time
import random
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

ArrayElements = 100

win = pygame.display.set_mode((600, 600))
A = ArrayVisualizer()


def BubbleSortVisualized(arr, Visualizer):
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i + 1], arr[i]
                win.fill((255, 255, 255))
                Visualizer.DrawArray(win, RED, arr, i + 1)
                pygame.display.update()
    return arr


print(BubbleSortVisualized([random.randint(1, 100)
                            for i in range(ArrayElements)], A))
while True:
    pass
