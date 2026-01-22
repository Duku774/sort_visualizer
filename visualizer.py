import pygame
import numpy as np

WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
padding_x = 2
padding_y = 5

#bar_height = np.random.randint(1, HEIGHT-padding_y+1, size=100)
bar_height = np.random.permutation(np.arange(1, 101)) * HEIGHT / 100
bar_width = (WIDTH - padding_x) / len(bar_height) - padding_x

def show(bar_height, colors=(255,255,255)):
    for i in range(len(bar_height)):
        pygame.draw.rect(
            surface=window, 
            color=colors, 
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