import pygame
 
pygame.init()

WIDTH = 600
HEIGHT = 600
FPS = 60
SHIP_MOVEMENT_MULTIPLIER = 2
ROCK_MOVEMENT_MULTIPLIER = 2

# create the display surface object
# of specific dimension..(WIDTH,HEIGHT).
scrn = pygame.display.set_mode((WIDTH, HEIGHT))

# set the pygame window name
pygame.display.set_caption('Mini Spaceship Game!')
 
# create a surface object, image is drawn on it.
space = pygame.image.load("/Users/juliachobu/Desktop/class_swordfish/code/julia/Python/mini_capstone/images/space.png").convert()

spaceship = pygame.image.load("/Users/juliachobu/Desktop/class_swordfish/code/julia/Python/mini_capstone/images/spaceship.png").convert_alpha()
spaceship = pygame.transform.scale(spaceship,(100, 150))

rock = pygame.image.load("/Users/juliachobu/Desktop/class_swordfish/code/julia/Python/mini_capstone/images/rock.png").convert_alpha()
rock = pygame.transform.scale(rock, (50,50))

# Using blit to copy content from one surface to other
scrn.blit(space, (0, 0))
scrn.blit(spaceship, (300, 300))
scrn.blit(rock,(0,0))
 
# paint screen one time
pygame.display.flip()

# deactivates the pygame library

def main():
    #print("Main function")
    spaceship_x = 300
    spaceship_y = 300
    rock_x = 300
    rock_y = 0

    SHIP_RECT = spaceship.get_rect(center=( spaceship_x, spaceship_y))
    ROCK_RECT = rock.get_rect(center=(rock_x, rock_y))

    clock = pygame.time.Clock()

    playing = True       

    while (playing):
      #print("Executing the while loop")
      clock.tick(FPS)
      keys = pygame.key.get_pressed()
      if keys[pygame.K_a]: #LEFT
        SHIP_RECT.x -=1 * SHIP_MOVEMENT_MULTIPLIER
      if keys[pygame.K_d]: #RIGHT
        SHIP_RECT.x +=1 * SHIP_MOVEMENT_MULTIPLIER
      if keys[pygame.K_s]: #DOWN
        SHIP_RECT.y +=1 * SHIP_MOVEMENT_MULTIPLIER
      if keys[pygame.K_w]: #UP
        SHIP_RECT.y -=1 * SHIP_MOVEMENT_MULTIPLIER
      ROCK_RECT.y += 1* ROCK_MOVEMENT_MULTIPLIER
      #print("Drawing on screen")

      scrn.blit(space, (0, 0))
      scrn.blit(rock,ROCK_RECT)
      scrn.blit(spaceship,SHIP_RECT)
      pygame.display.flip()
      pygame.display.update()

      if (SHIP_RECT.colliderect(ROCK_RECT)):{pygame.quit()}
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit() 

if __name__ == "__main__"  :
    main()