import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080),pygame.FULLSCREEN)

on = True

while on:
    screen.fill("white")

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False


pygame.quit()