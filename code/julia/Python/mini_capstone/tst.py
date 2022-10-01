import pygame
 
pygame.init()

WIDTH = 600
HEIGHT = 600
FPS = 60
WHITE = (255,255,255)
 
# create the display surface object
# of specific dimension..e(WIDTH,HEIGHT).
scrn = pygame.display.set_mode((WIDTH, HEIGHT))

# set the pygame window name
pygame.display.set_caption('Mini Spaceship Game!')
 
# create a surface object, image is drawn on it.
# imp = pygame.image.load("C:\\Users\\DELL\\Downloads\\gfg.png").convert()
space = pygame.image.load("/Users/juliachobu/Desktop/class_swordfish/code/julia/Python/mini_capstone/images/space.png").convert()
spaceship = pygame.image.load("/Users/juliachobu/Desktop/class_swordfish/code/julia/Python/mini_capstone/images/spaceship.png").convert()
spaceship = pygame.transform.scale(spaceship,(100,200))
rock = pygame.image.load("/Users/juliachobu/Desktop/class_swordfish/code/julia/Python/mini_capstone/images/rock.png").convert()
rock = pygame.transform.scale(rock, (50,50))
# Using blit to copy content from one surface to other
scrn.blit(space, (0, 0))
scrn.blit(spaceship, (0, 0))
scrn.blit(rock,(0,0))
 
# paint screen one time
pygame.display.flip()
status = True
while (status):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            status = False

playing = True       
while (playing):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: #LEFT
        WIDTH-=1
    if keys[pygame.K_d]: #RIGHT
        WIDTH+=1
    if keys[pygame.K_s]: #DOWN
        HEIGHT+=1 
    if keys[pygame.K_w]: #UP
        HEIGHT-=1         
    scrn.blit(spaceship,(WIDTH, HEIGHT))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True






# deactivates the pygame library
pygame.quit()