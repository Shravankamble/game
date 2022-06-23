import pygame
import values
from sys import exit

pygame.init()
# size of the window or display
width = 1200
height = 600
screen = pygame.display.set_mode((width, height))
# the title of the game
pygame.display.set_caption('SpeedRunner')
# we are never gonna move the main image it gonna be where it was from the starting
pygame_logo = pygame.image.load('run.png')
pygame.display.set_icon(pygame_logo)
sky_image = pygame.image.load('sky_image.png')
airplane = pygame.image.load('airplane.png').convert_alpha()
cloud = pygame.image.load('cloudy.png').convert_alpha()
extra_clouds = pygame.image.load('clouds.png').convert_alpha()
sun = pygame.image.load('contrast.png').convert_alpha()
ground = pygame.image.load('ground.png')
extra_ground = pygame.image.load('extra_ground.png')
car = pygame.image.load('car.png').convert_alpha()
tree = pygame.image.load('tree.png').convert_alpha()
house = pygame.image.load('house.png').convert_alpha()
family_of_that_house = pygame.image.load('garden.png')
family_of_that_house_x = 555
house_x = 565
tree_x = 5
ground_y = 500
car_x = 1300
sun_x = -10
extra_clouds_x = 900
cloud_x = 1100
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
    screen.blit(ground, (0, ground_y))
    screen.blit(extra_ground, (800, ground_y))
    screen.blit(tree, (tree_x, 380))
    screen.blit(house, (house_x, 380))
    screen.blit(family_of_that_house, (family_of_that_house_x, 471))
    screen.blit(car, (car_x, 420))
    house_x += 4
    if house_x > 2000:
        house_x = values.house_x_respawn_pos
    family_of_that_house_x += 4
    if family_of_that_house_x > 2000:
        family_of_that_house_x = values.family_of_that_house_x_respawn_pos
    tree_x += 4
    if tree_x > 5000:
        tree_x = values.tree_x_respawn_pos
    car_x -= 4
    if car_x < -100:
        car_x = values.car_x_respawn_pos
    extra_clouds_x -= 0.1
    if extra_clouds_x < -200:
        extra_clouds_x = values.extra_cloud_respawn_pos
    # pygame.display.update() is used to keep updating the screen or display
    pygame.display.update()
    # ths .tick() function is used for the fps
    Tick.tick(88)
