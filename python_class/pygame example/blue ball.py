import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    global done
    draw_circle = False
    x = 0
    y = size[1]
    to_x = 5
    to_y = -18
    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        x += to_x
        y += (to_y + 0.5)
        if y <= 0 or y >= size[1]:
            to_y = to_y * -1
        if x <= 0 or x >= size[0]:
            to_x = to_x * -1

        pygame.draw.circle(screen, (0, 0, 255), (x, y), 5)
        pygame.display.update()

runGame()
pygame.quit()
