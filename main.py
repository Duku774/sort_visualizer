import pygame
from algorithms import *
from visualizer import *

pygame.init()

pygame.display.set_caption("Sorting Visualizer")

run = True    
sorted_flag = False

while run:
    execute = False
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and not sorted_flag:
            if event.key == pygame.K_SPACE:
                execute = True

    if not execute:
        window.fill((0, 0, 0))
        if sorted_flag:
            show(bar_height, colors=(0,255,0))
        else:
            show(bar_height)
        pygame.display.update()
    else:
        #bubble_sort(values=bar_height)
        #selection_sort(values=bar_height)
        #insertion_sort(values=bar_height)
        quick_sort(values=bar_height, low=0, high=len(bar_height)-1)
        sorted_flag = True

pygame.quit()