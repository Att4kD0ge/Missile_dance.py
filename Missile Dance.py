import pygame
import random
import math
import sys
from Player import Player
from Button import Button


# initialize Pygame
pygame.init()
window_size = (800, 800)
clock = pygame.time.Clock()

#Screen
bg_img = pygame.image.load('Sprites/BG.jpeg')
screen = pygame.display.set_mode((window_size))
Background = pygame.transform.scale(bg_img, (window_size))

#Caption and Icon
pygame.display.set_caption("Dance of Missiles")
icon = pygame.image.load('Sprites/ufo.png')
pygame.display.set_icon(icon)

#Images
mimg = pygame.image.load("Sprites/bomb.png")
missile_image = pygame.transform.scale(mimg, (30, 30))
pimg = pygame.image.load("Sprites/ufo.png")
player_image = pygame.transform.scale(pimg, (30, 30))
startbutton = pygame.image.load("Sprites/Start_Button.png")
player_rect = player_image.get_rect()



#Variables
missile_speed = 3
tracking_speed = 0.05
score = 0
score_increment = 10
alive = 1
missile_spawn_timer = 0
missile_spawn_delay = 60
missile_rect = missile_image.get_rect()
window_height = 800
window_width = 800
initalmissile = 0


start = Button(
    (100, 100),
    image=startbutton,
    screen=screen

)
#Functions


def spawn_missile():

    global missile_rect
    global missile_spawn_timer

    if missile_spawn_timer > 0:
        missile_spawn_timer -= 1

    if missile_spawn_timer == 0:
        missile_pos = (
            random.randint(0, 800),
            random.choice([0, window_size[1]])
        )
        missile_rect.center = missile_pos

    player_distance = math.sqrt(
        (missile_rect.center[0] - player_rect.center[0]) ** 2 +
        (missile_rect.center[1] - player_rect.center[1]) ** 2
    )
    if player_distance > 0:
        tracking_direction = (
            (player_rect.center[0] - missile_rect.center[0]) / player_distance,
            (player_rect.center[1] - missile_rect.center[1]) / player_distance
        )
        missile_rect.center = (
            missile_rect.center[0] + tracking_direction[0] * missile_speed,
            missile_rect.center[1] + tracking_direction[1] * missile_speed
        )

        missile_angle = math.atan2(-tracking_direction[1], tracking_direction[0]) * 180 / math.pi
        missile_rotated = pygame.transform.rotate(missile_image, missile_angle)
        missile_rect = missile_rotated.get_rect(center=missile_rect.center)
        screen.blit(missile_rotated, missile_rect)


def draw_screen():
    screen.blit(Background, (0, 0))


def update_screen():
    screen.blit(Background, (0, 0))
    activate_player()
    spawn_missile()

    pygame.display.update()


def menu():
    start.show()
    clock.tick(30)
    pygame.display.update()

def activate_player():
    player_rect = player_image.get_rect()
    mx, my = pygame.mouse.get_pos()
    screen.blit(player_image, (mx, my))
    player_rect.centerx = window_width // 2
    player_rect.bottom = window_height - 20


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        start.click(event)

    if start.get_value() == 0:
        menu()

    elif start.get_value() == 1:

        alive = 1

        pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

        clock = pygame.time.Clock().tick(60)

        draw_screen()

        update_screen()

        pygame.time.wait(10)
