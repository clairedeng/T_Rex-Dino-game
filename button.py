import pygame

class Button():
    def __init__(self, dino_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.dino_settings = dino_settings
        img = pygame.image.load('images/game_over.png')
        img = img.convert()
        self.rect = img.get_rect()
        surface = pygame.Surface(self.rect.size)
        surface.blit(img, (0,0), self.rect)
        colorkey = surface.get_at((0,0))
        surface.set_colorkey(colorkey)
        self.image = surface
        self.rect.center = self.screen_rect.center
    def blitme(self):
        self.screen.blit(self.image, self.rect)
