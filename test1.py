import pygame
import time
import random
import serial
import threading

pygame.init()


# Serial port initialization
# serial_port = serial.Serial('COM3', 9600)  # Replace with your Arduino port and baud rate

print('pygame.USEREVENT', pygame.USEREVENT)

ser = serial.Serial('/dev/tty.usbmodem101', 9600)

# while True:
#     if ser.in_waiting > 0:
#         data = ser.readline().decode().rstrip()
#         values = data.split(",")
#         if len(values) == 3:
#             try:
#                 sensorValue1 = float(values[0])
#                 sensorValue2 = float(values[1])
#                 sensorValue3 = float(values[2])
#                 print("Sensor 1:", sensorValue1)
#                 print("Sensor 2:", sensorValue2)
#                 print("Sensor 3:", sensorValue3)
#             except ValueError:
#                 print("Invalid float values received")
#         else:
#             print("Invalid data format received")

def arduino_thread():
    global shared_x, shared_y, shared_z
    ser = serial.Serial('/dev/tty.usbmodem101', 9600)
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().rstrip()
            values = data.split(',')
            if len(values) == 3:
                shared_x = float(values[0])
                shared_y = float(values[1])
                shared_z = float(values[2])


# Pygame event types
CUSTOM_EVENT_LEFT = pygame.USEREVENT + 1
CUSTOM_EVENT_RIGHT = pygame.USEREVENT + 2
CUSTOM_EVENT_UP = pygame.USEREVENT + 3
CUSTOM_EVENT_DOWN = pygame.USEREVENT + 4


# Create custom events
custom_event_left = pygame.event.Event(CUSTOM_EVENT_LEFT)
custom_event_right = pygame.event.Event(CUSTOM_EVENT_RIGHT)
custom_event_up = pygame.event.Event(CUSTOM_EVENT_UP)
custom_event_down = pygame.event.Event(CUSTOM_EVENT_DOWN)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])



def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def game_thread():
    pygame.init()
    

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 600
    dis_height = 400

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Eat Up Snakey By Anupam')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 3

    font_style = pygame.font.SysFont("bahnschrift", 27)
    score_font = pygame.font.SysFont("comicsansms", 37)


    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0+100, dis_width - snake_block-100) / 10.0) * 10.0
    foody = round(random.randrange(0+100, dis_height - snake_block-100) / 10.0) * 10.0


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle custom events
            elif event.type == CUSTOM_EVENT_1:
                print("Custom Event 1 occurred")
            elif event.type == CUSTOM_EVENT_2:
                print("Custom Event 2 occurred")
            elif event.type == CUSTOM_EVENT_3:
                print("Custom Event 3 occurred")
            elif event.type == CUSTOM_EVENT_4:
                print("Custom Event 4 occurred")

        # Access the shared data in the game loop
        if shared_x is not None and shared_y is not None and shared_z is not None:
            x = shared_x
            y = shared_y
            z = shared_z

            # Define conditions for custom events based on (x, y, z) values
            if x > 0 and y > 0 and z > 0:
                pygame.event.post(pygame.event.Event(CUSTOM_EVENT_1))
            elif x < 0 and y < 0 and z < 0:
                pygame.event.post(pygame.event.Event(CUSTOM_EVENT_2))
            elif x > 0 and y < 0 and z < 0:
                pygame.event.post(pygame.event.Event(CUSTOM_EVENT_3))
            elif x < 0 and y > 0 and z < 0:
                pygame.event.post(pygame.event.Event(CUSTOM_EVENT_4))

        # Update game visuals or perform game logic
        # ...

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0+100, dis_width - snake_block-100) / 10.0) * 10.0
    foody = round(random.randrange(0+100, dis_height - snake_block-100) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press P-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()