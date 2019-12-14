import pygame
import random

# initialize pygame
pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600

window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("images/player.png")

playerX = WIN_WIDTH / 2 - 25
playerY = WIN_HEIGHT / 2 + 180

PLAYER_SPEED = 0.3


def player(x, y):
    window.blit(playerImg, [x, y])


# Invader
invaderImg = pygame.image.load("images/invader.png")
invaderX = random.randint(0, WIN_WIDTH-64)
invaderY = random.randint(0, WIN_HEIGHT-140)

invaderX_change = 0.3


def invader(x, y):
    window.blit(invaderImg, [x, y])


# Game Loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    window.fill([0, 0, 51])

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= PLAYER_SPEED
        if event.key == pygame.K_RIGHT:
            playerX += PLAYER_SPEED

    if playerX <= 0:
        playerX = 0
    elif playerX >= WIN_WIDTH - 64:
        playerX = WIN_WIDTH - 64

    invaderX += invaderX_change
    if invaderX <= 0:
        invaderX_change = 0.3
    elif invaderX >= WIN_WIDTH - 64:
        invaderX_change = -0.3

    player(playerX, playerY)
    invader(invaderX, invaderY)
    pygame.display.update()
