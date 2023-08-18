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
    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        
        sky = pygame.image.load('python_class/pygame example/backgrounds/Background.png')
        player = pygame.image.load('python_class/pygame example/backgrounds/Player_Attack_R.png')
        castle = pygame.image.load('python_class/pygame example/backgrounds/castle.png')
        ground = pygame.image.load('python_class/pygame example/backgrounds/Ground.png')
        
        sky = pygame.transform.scale(sky, (400, 300))
        screen.blit(sky, (0,0))

        ground = pygame.transform.scale(ground, (400, 150))
        screen.blit(ground, (0, 300))

        castle = pygame.transform.scale(castle, (200, 150))
        screen.blit(castle, (200, 150))

        heart = pygame.image.load('python_class/pygame example/backgrounds/heart.png')
        heart = pygame.transform.scale(heart, (50, 50))
        screen.blit(heart, (0, 0))

        player = pygame.transform.scale(player, (50, 50))
        screen.blit(player, (100, 250))

        pygame.display.update()

runGame()
pygame.quit()