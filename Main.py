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

ArrayElements = 1000

win = pygame.display.set_mode((600, 600))
A = ArrayVisualizer()


def BubbleSortVisualized(arr, Visualizer):
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i + 1], arr[i]
                if not i % 10:
                    win.fill((255, 255, 255))
                    Visualizer.DrawArray(win, MAGENTA, arr, i + 1)
                    pygame.display.update()
    win.fill((255, 255, 255))
    Visualizer.DrawArray(win, MAGENTA, arr, i + 1)
    pygame.display.update()
    return arr


def InsertionSortVisualized(arr, Visualizer):
    '''
        Time Complexity: O(n^2)
    '''

    frame = 1

    sInx = 1
    n = len(arr)
    for i in range(1, n):  # main loop
        if arr[i] < arr[i-1]:  # detecting unordered pairs
            j = 0
            temp = arr[i]
            # finding index j where the item at i can be inserted
            while j < sInx-1 and arr[j] < arr[i]:
                j += 1

            # shifting all items from j to the end of the sorted partion one index to make room for arr[i]
            arr[j+1:sInx + 1] = arr[j:sInx]
            arr[j] = temp  # assigning arr[i] to arr[j] after storing it in a temp var
            sInx += 1  # increasing size of sorted partition
            if not i % frame:
                win.fill((255, 255, 255))
                Visualizer.DrawArray(win, MAGENTA, arr, i + 1)
                pygame.display.update()
        else:
            sInx += 1
            if not i % frame:
                win.fill((255, 255, 255))
                Visualizer.DrawArray(win, MAGENTA, arr, i + 1)
                pygame.display.update()
    win.fill((255, 255, 255))
    Visualizer.DrawArray(win, MAGENTA, arr, 0)
    pygame.display.update()

    return arr


# print(BubbleSortVisualized([random.randint(1, 100)
#                             for i in range(ArrayElements)], A))
print(InsertionSortVisualized([random.randint(1, 100)
                               for i in range(ArrayElements)], A))
time.sleep(5)
