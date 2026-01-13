import pygame

pygame.init()

WIDTH = 500
HEIGHT = 400

window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Bubble sort")

# initial position
initial_x = 40
initial_y = 40

bar_width = 20

bar_height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]

run = True

def show(bar_height):
    for i in range(len(bar_height)):
        pygame.draw.rect(surface=window, color=(255, 255, 255), rect=(initial_x + 30 * i, initial_y, bar_width, bar_height[i]))

while run:
    execute = False
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # start sorting after pressing spacebar
    if keys[pygame.K_SPACE]:
        execute = True

    if not execute:
        window.fill((0, 0, 0))
        show(bar_height)
        pygame.display.update()
    else:
        # start sorting using bubble sort technique
        for i in range(len(bar_height) - 1):
            for j in range(len(bar_height) - i - 1):
                if bar_height[j] > bar_height[j + 1]:
                    t = bar_height[j]
                    bar_height[j] = bar_height[j + 1]
                    bar_height[j + 1] = t

                window.fill((0, 0, 0))
                show(bar_height)
                pygame.time.delay(50)
                pygame.display.update()

        execute = False

pygame.quit()