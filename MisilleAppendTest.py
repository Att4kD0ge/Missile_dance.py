import pygame
import random
import math
import sys
from Missile import Missile

#Variablles
window_size = (800, 800)

#Missile Image
mimg = pygame.image.load("Sprites/bomb.png")
missile_image = pygame.transform.scale(mimg, (30, 30))

#Background
bg_img = pygame.image.load('Sprites/BG.jpeg')
screen = pygame.display.set_mode((window_size))
Background = pygame.transform.scale(bg_img, (window_size))

#Functions

missiles = []




def update():
    screen.blit(Background, (0, 0))




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

        update()
        for i in range(3):
            missile = Missile(10, 1, (i * 200 + 100, 400))
            screen.blit(missile.image, missile.rect.center)
            missiles.append(missile)
        pygame.display.update()
        clock = pygame.time.Clock().tick(60)
        pygame.time.wait(30)

