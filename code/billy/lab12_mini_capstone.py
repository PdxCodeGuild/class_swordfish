import pygame
from pygame import mixer
from fighter_characters import character_models
from numpy import character

mixer.init()
pygame.init()

pygame.display.set_caption('Krusty Krab Chaos')

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # loads background image.

'''sets frames per second'''
clock = pygame.time.Clock()
FPS = 120

'''define colors'''
WHITE = (255, 255, 255)
GREEN = (0, 150, 0)
RED = (230, 0, 0)

score = [0, 0]
end_of_round = False
ROUND_COOLDOWN = 5000
RESET = 3000

death_bringer_sheet = pygame.image.load('wizard.png').convert_alpha() # loads the death bringer sprite sheet.
angel_sheet = pygame.image.load('warrior.png').convert_alpha() # loads the angel sprite sheet.

DEATH_BRINGER_ANIMATIONS = [8, 8, 1, 8, 8, 3, 7]  # defines the  number of steps for each animation (numbers equal animation frames).
ANGEL_ANIMATIONS = [10, 8, 1, 7, 7, 3, 7] # defines the number of steps for each animation (numbers equal animation frames).

'''define death bringer variables'''
DEATH_BRINGER_SIZE = 250  # png size divided by number of items in the row.
DEATH_BRINGER_SCALE = 3
DEATH_BRINGER_POSITION = [112, 107] #offsets to align with their rect.
DEATH_BRINGER_DATA = [DEATH_BRINGER_SIZE, DEATH_BRINGER_SCALE, DEATH_BRINGER_POSITION]
'''define angel variables'''
ANGEL_SIZE = 162
ANGEL_SCALE = 4
ANGEL_POSITION = [72, 56] # offsets to align with rect.
ANGEL_DATA = [ANGEL_SIZE, ANGEL_SCALE, ANGEL_POSITION]

'''load music and sound.'''
pygame.mixer.music.load('rick_roll.mp3')
pygame.mixer.music.set_volume(0.75)
pygame.mixer.music.play(-2, 0.0, 5000)

sword_fx = pygame.mixer.Sound('sword_effect.wav')
sword_fx.set_volume(0.17)

magic_fx = pygame.mixer.Sound('magic_effect.wav')
magic_fx.set_volume(1)

background_image = pygame.image.load('krusty_krab.jpg').convert_alpha() # sets the background image

def background_rendering():
    '''renders the background and sets the screen width and height.'''
    scaled_background = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_background,(0,0))

def healthbar_rendering(health, x, y):
    '''renders the health bars on screen and will reduce healthbar size to show health loss.'''
    ratio = health / 100 # divides healthbar by the ratio.
    pygame.draw.rect(screen, WHITE,(x - 2, y - 2, 304, 24 ))
    pygame.draw.rect(screen, RED, (x, y, 300, 20)) # sits behind healthbar and will display "health loss."
    pygame.draw.rect(screen, GREEN, (x, y, 300 * ratio, 20)) # assigns health bars to the screen, location and width/height.
    


'''creates instances of each character''' 
character_1 = character_models(1, 200, 150, False, ANGEL_DATA, angel_sheet, ANGEL_ANIMATIONS, sword_fx)
character_2 = character_models(2, 700, 150, True, DEATH_BRINGER_DATA, death_bringer_sheet, DEATH_BRINGER_ANIMATIONS, magic_fx)

game_running = True

'''main game loop'''
while game_running:

    clock.tick(FPS)

    background_rendering()

    healthbar_rendering(character_1.health, 20, 20) # displays the character status (health) and the exact x/y location.
    healthbar_rendering(character_2.health, 680, 20)

    character_1.character_movement(SCREEN_WIDTH, SCREEN_HEIGHT, screen, character_2, ) # character_2 argument allows charcter 1 to attack them.
    character_2.character_movement(SCREEN_WIDTH, SCREEN_HEIGHT, screen, character_1)

    '''updates character animations'''
    character_1.update_animation() 
    character_2.update_animation()


    '''renders the character on the screen.'''
    character_1.display_character(screen) 
    character_2.display_character(screen)

    if end_of_round == False:
        if character_1.alive == False:
            score[1] += 1
            end_of_round = True
            RESET = pygame.time.get_ticks()
            print(score)
        elif character_2.alive == False:
            score[0] += 1
            end_of_round = True
            RESET = pygame.time.get_ticks()
            print(score)
    else:
        if pygame.time.get_ticks() - RESET > ROUND_COOLDOWN:
            end_of_round = False
            character_1 = character_models(1, 200, 310, False, ANGEL_DATA, angel_sheet, ANGEL_ANIMATIONS, sword_fx)
            character_2 = character_models(2, 700, 310, True, DEATH_BRINGER_DATA, death_bringer_sheet, DEATH_BRINGER_ANIMATIONS, magic_fx)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    pygame.display.update()
pygame.quit()