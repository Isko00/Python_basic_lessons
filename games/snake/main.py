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


def is_close_command(event):
    if event.type == pygame.QUIT:
        return True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            return True
    else:
        return False


def show_game_over_menu(length_of_snake):
    print("Game OVER!")
    dis.fill(black)
    display_message("You Lost! Press C-Play Again or Q-Quit", red)
    show_score(length_of_snake - 1)
    pygame.display.update()

            
def get_speed(event):
    if event.key == pygame.K_LEFT:
        x1_speed = -block_length
        y1_speed = 0
    elif event.key == pygame.K_RIGHT:
        x1_speed = block_length
        y1_speed = 0
    elif event.key == pygame.K_UP:
        y1_speed = -block_length
        x1_speed = 0
    elif event.key == pygame.K_DOWN:
        y1_speed = block_length
        x1_speed = 0
    return x1_speed, y1_speed


def game_loop():
    # starting position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # speed of the snake
    x1_speed = 0
    y1_speed = 0

    # snake parameters
    snake_list = []
    length_of_snake = 1

    # position of food
    food_x = random.randrange(0, dis_width - block_length, 10)
    food_y = random.randrange(0, dis_height - block_length, 10)

    close = False
    game_over = False

    while not close:
        # fill display
        dis.fill(black)

        if game_over:
            show_game_over_menu(length_of_snake)

        # get speed from control keys
        for event in pygame.event.get():
            if is_close_command(event):
                close = True
            if event.type == pygame.KEYDOWN:
                x1_speed, y1_speed = get_speed(event)

        # movement of the snake
        x1 += x1_speed
        y1 += y1_speed

        pygame.draw.rect(dis, red, [food_x, food_y, block_length, block_length])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        draw_snake(block_length, snake_list)
        show_score(length_of_snake - 1)

        # food eating
        if x1 == food_x and y1 == food_y:
            # create new food
            food_x = random.randrange(0, dis_width - block_length, 10)
            food_y = random.randrange(0, dis_height - block_length, 10)

            print(snake_list)
            length_of_snake += 1

        # update display
        pygame.display.update()
        # FPS
        clock.tick(snake_speed)

        # game over scenarios
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

    # close game
    pygame.quit()
    quit()

game_loop()