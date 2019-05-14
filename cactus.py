import pygame
import random
from pygame.sprite import Sprite

class Cactus(Sprite):
    def __init__(self, dino_settings, screen):
        super(Cactus, self).__init__()
        self.dino_settings = dino_settings
        self.screen = screen
        img_big = pygame.image.load('images/cacti-big.png')
        img_small = pygame.image.load('images/cacti-small.png')
        img_big = img_big.convert()
        img_small = img_small.convert()
        width_big, height_big = img_big.get_width()/3, img_big.get_height()
        width_small, height_small = img_small.get_width()/3, img_small.get_height()

        self.images = []
        for num in range(0, 3):
            rect = pygame.Rect(num * width_big, 0, width_big, height_big)
            surface = pygame.Surface(rect.size)
            surface.blit(img_big, (0,0), rect)
            
            colorkey = surface.get_at((0,0))
            surface.set_colorkey(colorkey)
            surface = pygame.transform.scale(surface, (40,40))
            self.images.append(surface)
        for num in range(0, 5):
            rect = pygame.Rect(num * width_small, 0, width_small, height_small)
            surface = pygame.Surface(rect.size)
            surface.blit(img_small, (0,0), rect)
            colorkey = surface.get_at((0,0))
            surface.set_colorkey(colorkey)
            surface = pygame.transform.scale(surface, (30, 40))
            self.images.append(surface)

        self.image = self.images[random.randrange(0, 6)]
        self.rect= self.images[0].get_rect()
        self.rect.bottom = 147
        self.rect.left = 700
        self.x = float(self.rect.x)


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.right <= 0:
            return True

    def update(self):
        self.x -= 0.2
        self.rect.x = self.x
