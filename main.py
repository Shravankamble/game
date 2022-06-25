import pygame
import collision
import values
from sys import exit

pygame.init()
# size of the window or display
width = 1200
height = 600
screen = pygame.display.set_mode((width, height))
font_name = pygame.font.Font(None, 35)
score_render = font_name.render('SCORE', False, 'black')
score_rect = score_render.get_rect(center = (545, 20))
# the title of the game
pygame.display.set_caption('SpeedRunner')
# we are never gonna move the main image it gonna be where it was from the starting
pygame_logo = pygame.image.load('run.png')
pygame.display.set_icon(pygame_logo)
# background/sky
sky_image = pygame.image.load('sky_image.png')
# airplane
airplane = pygame.image.load('airplane.png').convert_alpha()
# cloud
cloud = pygame.image.load('cloudy.png').convert_alpha()
# extra cloud
extra_clouds = pygame.image.load('clouds.png').convert_alpha()
# sun
sun = pygame.image.load('contrast.png').convert_alpha()
# ground
ground = pygame.image.load('ground.png')
# extra ground
extra_ground = pygame.image.load('extra_ground.png')
# tree
tree = pygame.image.load('tree.png').convert_alpha()
#house
house = pygame.image.load('house.png').convert_alpha()
#family of that house
family_of_that_house = pygame.image.load('garden.png').convert_alpha()
# player
player = pygame.image.load('ninja.png').convert_alpha()
player_rect = player.get_rect(midbottom = (35, 500))
# car
car = pygame.image.load('car.png').convert_alpha()
car_rect = car.get_rect(bottomright = (1000, 545))
# black hole
black_hole = pygame.image.load('black-hole.png').convert_alpha()
black_hole_rect = black_hole.get_rect(midbottom = (700, 460))
# player_x and player_y
player_x = 35
player_y = 445
# family_of_that_house_x
family_of_that_house_x = 555
# house_x
house_x = 565
# tree_x
tree_x = 5
# ground_x
ground_y = 500
## car_x = 1300
# sun_x
sun_x = -10
# extra_clouds_x
extra_clouds_x = 900
# cloud_x
cloud_x = 1100
# airplane_x
airplane_x = 0
Tick = pygame.time.Clock()

# trying out co-ordinates to learn more about them 
# aquiring space is (100, 200) for that you use pygame.Surface
# this is just to have an idea that how work with co-ordinates
# no need of this just practicing.
# testing = pygame.Surface((100, 200))
# the fill is just means adding color to it
# testing.fill('white')

# this is the while loop to run display until the user quits means exiting the game.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # .blit() basically means adding additional surface on each other.
    #screen.blit(testing, (10, 500))
    screen.blit(sky_image, (0, 0))
    airplane_x += 1
    if airplane_x > 2000:
        airplane_x = values.airplane_respawn_pos
    screen.blit(airplane, (airplane_x, 120))
    screen.blit(cloud, (cloud_x, 120))
    cloud_x -= 0.1
    if cloud_x < -185:
        cloud_x = values.cloud_x_respawn_pos
    screen.blit(extra_clouds, (extra_clouds_x, 129))
    screen.blit(sun, (sun_x, 0))
    screen.blit(score_render, score_rect)
    screen.blit(ground, (0, ground_y))
    screen.blit(extra_ground, (800, ground_y))
    screen.blit(tree, (tree_x, 380))
    screen.blit(house, (house_x, 380))
    screen.blit(family_of_that_house, (family_of_that_house_x, 471))
    screen.blit(black_hole, black_hole_rect)
    screen.blit(car, car_rect)
    screen.blit(player, player_rect)
    # 67
    # print(player_rect.right)
    # print(car_rect.right)
    # player_rect.x += 3
    # if player_rect.left > 1300:
    #     player_rect.right = -100
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print("collision occured!")
    # house movement
    house_x += 4
    if house_x > 2000:
        house_x = values.house_x_respawn_pos

    # family_of_that_house movement
    family_of_that_house_x += 4
    if family_of_that_house_x > 2000:
        family_of_that_house_x = values.family_of_that_house_x_respawn_pos

    # tree movement
    tree_x += 4
    if tree_x > 5000:
        tree_x = values.tree_x_respawn_pos

    # car_x -= 4
    # if car_x < -100:
    #     car_x = values.car_x_respawn_pos
    # black_hole
    black_hole_rect.x += 1
    if black_hole_rect.right > 3000:
        black_hole_rect.left = -100

    # car mechanism
    car_rect.x -= 4
    if car_rect.right < -200:
        car_rect.left = 1300

    player_rect.x += 2
    if player_rect.right > 1200:
        player_rect.left = 35
    # cloud movement
    extra_clouds_x -= 0.1
    if extra_clouds_x < -200:
        extra_clouds_x = values.extra_cloud_respawn_pos
    # pygame.display.update() is used to keep updating the screen or display
    if black_hole_rect.colliderect(car_rect):
        car_rect.right = 1300
    pygame.display.update()
    # ths .tick() function is used for the games fps(frames per second)
    Tick.tick(88)