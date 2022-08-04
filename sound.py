# import pygame

# pygame.init()

# # ninja_jump = pygame.mixer.Sound('ninja-jump.mp3')

# # ninja_hurt = pygame.mixer.Sound('hurt.mp3')

# # blast = pygame.mixer.Sound('blast.wav')

# # stab = pygame.mixer.Sound('stab.mp3')

# # win = pygame.mixer.Sound('winning.wav')

# def bgmusic():
#     music = pygame.mixer.music.load('bgmusic.mp3')
#     pygame.mixer.music.play(-1)

# def stop():
#     pygame.mixer.music.stop()
import pygame

pygame.init()

def bgm():
    music = pygame.mixer.music.load('bgm.mp3')
    pygame.mixer.music.play(-1)