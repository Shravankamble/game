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
airplane = pygame.image.load('airplane.png')
cloud = pygame.image.load('cloudy.png')
extra_clouds = pygame.image.load('clouds.png')
extra_clouds_x = 900
cloud_x = 1100
airplane_x = 0
Tick = pygame.time.Clock()

# trying out co-ordinates to learn more about them 
# aquiring space is (100, 200) for that you use pygame.Surface
# this is just to have an idea that how work with co-ordinates
# no need of this just practicing.
testing = pygame.Surface((100, 200))
# the fill is just means adding color to it
testing.fill('white')

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
    if airplane_x > 1300:
        airplane_x = values.airplane_respawn_pos
    screen.blit(airplane, (airplane_x, 120))
    screen.blit(cloud, (cloud_x, 120))
    cloud_x -= 0.1
    if cloud_x < -185:
        cloud_x = values.cloud_x_respawn_pos
    screen.blit(extra_clouds, (extra_clouds_x, 129))
    extra_clouds_x -= 0.1
    if extra_clouds_x < -200:
        extra_clouds_x = values.extra_cloud_respawn_pos
    # pygame.display.update() is used to keep updating the screen or display
    pygame.display.update()
    # ths .tick() function is used for the fps
    Tick.tick(88)
