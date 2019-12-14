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

def player(x,y):
    window.blit(playerImg, [x,y])

# Game Loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= 0.05;
        if event.key == pygame.K_RIGHT:
            playerX += 0.05

    # window.fill((0,0,0))
    player(playerX,playerY)
    pygame.display.update()
