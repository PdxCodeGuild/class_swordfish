import pygame

class character_models():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 30, 30))

    def character_movement(self, screen_width):

        SPEED = 10
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        
        self.rect.x += dx
        self.rect.y += dy

    def display_character(self, surface):

        pygame.draw.rect(surface, (0,255,0), self.rect)