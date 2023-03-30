import pygame

# initialize game
pygame.init()

# colors in RGB (red green blue)
red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
lime = (128, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
l_blue = (0, 128, 255)
blue = (0, 0, 255)
purple = (128, 0, 255)
pink = (255, 0, 255)
deep_pink = (255, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and caption
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/icon_rocket.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('images/player.png')
playerX = 370
playerY = 480
speedX = 0.3
speedY = 0

# draws player
def draw_player(x, y):
    screen.blit(playerImg, (x, y))


# state of the game (Active / not Active)
gameActive = True
# game loop
while gameActive:
    # getting user made events
    for event in pygame.event.get():
        # close window event handling
        if event.type == pygame.QUIT:
            gameActive = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedX = -0.2
                speedY = 0
            elif event.key == pygame.K_RIGHT:
                speedX = 0.2
                speedY = 0
            elif event.key == pygame.K_UP:
                speedX = 0
                speedY = -0.2
            elif event.key == pygame.K_DOWN:
                speedX = 0
                speedY = 0.2

    playerX += speedX
    playerY += speedY

    # set background color
    screen.fill(black)

    # draw player
    draw_player(playerX, playerY)

    # update changes on the screen
    pygame.display.update()
