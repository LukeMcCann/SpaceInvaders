import pygame

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
playerX = WIN_WIDTH/2-25
playerY = WIN_HEIGHT/2+180

def player():
    window.blit(playerImg, [playerX, playerY])


# Game Loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # window.fill((0,0,0))
    player()
    pygame.display.update()
