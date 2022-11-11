import os
import pygame


pygame.init

WIDTH = 900
HEIGHT = 500
color_blue = (0, 0, 255)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game!")

print(os.path.join( 'images', 'space.png'))

path_to_image = pygame.image.load('/Users/juliachobu/Desktop/class_swordfish/code/julia/Python/mini_capstone/images/space.png').convert()
# background = pygame.image.load(path_to_image).convert()

print(os.path.join( 'images', 'spaceship.png'))
#ship = pygame.image.load(path_to_image).convert()

def window():
    screen.fill(color_blue)
    screen.blit(path_to_image, (900,500) )

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    run = True 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window()

    pygame.quit()


if __name__ == "__main__"  :
    main()