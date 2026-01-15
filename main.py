import pygame
import numpy as np

pygame.init()

WIDTH = 800
HEIGHT = 600

window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sorting Visualizer")

padding_x = 2
padding_y = 5

#bar_height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]
bar_height = np.random.randint(1, HEIGHT-padding_y+1, size=30)

bar_width = (WIDTH - padding_x) / len(bar_height) - padding_x

run = True

def show(bar_height):
    for i in range(len(bar_height)):
        pygame.draw.rect(
            surface=window, 
            color=(255, 255, 255), 
            rect=(
                padding_x + (bar_width + padding_x) * i, 
                HEIGHT - bar_height[i] - padding_y, 
                bar_width, 
                bar_height[i]
            ),
        )

def display(values):
    window.fill((0, 0, 0))
    show(values)
    pygame.time.delay(50)
    pygame.display.update()    

def bubble_sort(values):
    for i in range(len(values) - 1):
        for j in range(len(values) - i - 1):
            if values[j] > values[j + 1]:
                t = values[j]
                values[j] = values[j + 1]
                values[j + 1] = t
            display(values)

def selection_sort(values):
    for i in range(len(values) - 1):
        min_idx = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_idx]:
                min_idx = j
        values[i], values[min_idx] = values[min_idx], values[i]
        display(values)

while run:
    execute = False
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                execute = True

    if not execute:
        window.fill((0, 0, 0))
        show(bar_height)
        pygame.display.update()
    else:
        # start sorting using bubble sort technique
        #bubble_sort(values=bar_height)
        selection_sort(values=bar_height)

pygame.quit()