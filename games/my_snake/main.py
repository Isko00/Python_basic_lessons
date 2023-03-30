import pygame
import random

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

# initialize font
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# create the screen
screen = pygame.display.set_mode((800, 600))

# state clock
clock = pygame.time.Clock()

# title and caption
pygame.display.set_caption("Space Invaders")


# draws player
def draw_player(body):
    for i in body:
        pygame.draw.rect(screen, green, pygame.Rect(i[0], i[1], 20, 20))


# draws food
def draw_food(x, y):
    pygame.draw.rect(screen, red, pygame.Rect(x, y, 20, 20))


def game_loop():
    # food
    food_x = 380
    food_y = 80
    
    # player
    player_x = 380
    player_y = 480
    speed_x = 0
    speed_y = 0
    body = [[player_x, player_y]]
    
    # initialize score
    score = 0
    
    # state of the game (Active / not Active)
    game_active = True
    game_over = False
    # game loop
    while game_active:
        # set background color
        screen.fill(black)
    
        # draw player
        draw_player(body)
    
        # draw food
        draw_food(food_x, food_y)
    
        # draw score
        score_text = my_font.render(str(score), False, (0, 0, 255))
        screen.blit(score_text, (20, 0))
    
        # eating
        if player_x == food_x and player_y == food_y:
            score += 1
            food_x = random.randrange(0, 780, 20)
            food_y = random.randrange(0, 580, 20)
            if [food_x, food_y] in body:
                food_x = random.randrange(0, 780, 20)
                food_y = random.randrange(0, 580, 20)
    
        # getting user made events
        for event in pygame.event.get():
            # close window event handling
            if event.type == pygame.QUIT:
                game_active = False
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and speed_x != 20:
                    speed_x = -20
                    speed_y = 0
                elif event.key == pygame.K_RIGHT and speed_x != -20:
                    speed_x = 20
                    speed_y = 0
                elif event.key == pygame.K_UP and speed_y != 20:
                    speed_x = 0
                    speed_y = -20
                elif event.key == pygame.K_DOWN and speed_y != -20:
                    speed_x = 0
                    speed_y = 20
            # elif event.type == pygame.KEYUP:
            #     speed_x = 0
            #     speed_y = 0
    
        player_x += speed_x
        player_y += speed_y
    
        if player_x == 800:
            player_x = 0
        elif player_x == -20:
            player_x = 780
        elif player_y == 600:
            player_y = 0
        elif player_y == -20:
            player_y = 580
    
        if len(body) > 1 and [player_x, player_y] in body:
            game_over = True
            game_active = False
    
        body.append([player_x, player_y])
        if len(body) > score + 1:
            del body[0]
    
        # update changes on the screen
        pygame.display.update()
        clock.tick(10)

    if game_over:
        game_over_menu(score)


def game_over_menu(last_score):
    while True:
        # set background color
        screen.fill(black)

        # show game over message
        game_over_message = my_font.render("Game Over!", False, pink)
        screen.blit(game_over_message, (320, 100))

        # draw score
        score_text = my_font.render("Score" + str(last_score), False, (0, 0, 255))
        screen.blit(score_text, (350, 150))

        # show control
        control_text1 = my_font.render("Press 'Q' to quit", False, (0, 0, 255))
        control_text2 = my_font.render("Press 'R' to Restart", False, (0, 0, 255))
        screen.blit(control_text1, (270, 300))
        screen.blit(control_text2, (250, 350))

        for event in pygame.event.get():
            # close window event handling
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_loop()
                elif event.key == pygame.K_q:
                    quit()

        # update changes on the screen
        pygame.display.update()


game_loop()
