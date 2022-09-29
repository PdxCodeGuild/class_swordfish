
import pygame
from fighter_characters import character_models
from numpy import character

pygame.init()

pygame.display.set_caption('Cosmic Chaos')

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

background_image = pygame.image.load('space_background.jpg').convert_alpha()

def background_rendering():

    scaled_background = pygame.transform.scale(background_image,(SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_background,(0,0))

character_1 = character_models(200, 400)
character_2 = character_models(700, 400)

game_running = True

while game_running:

    clock.tick(FPS)

    background_rendering()

    character_1.character_movement(SCREEN_WIDTH)
    # character_2.character_movement()


    character_1.display_character(screen)
    character_2.display_character(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_running = False

    pygame.display.update()
pygame.quit()