# import libraries
import random
import pygame

# initialize all modules
pygame.init()

# define colors as tuples in RGB format
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# define size of display as integers
dis_width = 600
dis_height = 400

# define display with pre-written size
# creating new surface, which will be counted as main
dis = pygame.display.set_mode((dis_width, dis_height))
# define caption for display
pygame.display.set_caption('Snake Game')

# define clock
clock = pygame.time.Clock()

block_length = 10
snake_speed = 15

# define fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# displays score
def show_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# displays snake
def draw_snake(in_block_length, in_snake_list):
    for x in in_snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], in_block_length, in_block_length])


# displays message
def display_message(msg, color):
    # create new surface with message
    rendered_msg = font_style.render(msg, True, color)
    # overlay daughter surface over main surface
    dis.blit(rendered_msg, [dis_width / 6, dis_height / 3])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = random.randrange(0, dis_width - block_length, 10)
    food_y = random.randrange(0, dis_height - block_length, 10)

    while not game_over:
        while game_close:
            dis.fill(black)
            display_message("You Lost! Press C-Play Again or Q-Quit", red)
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_length
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_length
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_length
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_length
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(black)

        pygame.draw.rect(dis, red, [food_x, food_y, block_length, block_length])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(block_length, snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = random.randrange(0, dis_width - block_length, 10)
            food_y = random.randrange(0, dis_height - block_length, 10)
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
