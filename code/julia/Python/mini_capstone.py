import os
import pygame


pygame.init

WIDTH = 900
HEIGHT = 500
color_blue = (0, 0, 255)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Game!")


background = pygame.image.load(os.path.join( 'images', 'background.png'))

def window():
    screen.fill(color_blue)
    screen.blit(background, (900,500) )
    pygame.display.update


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
    main().quit