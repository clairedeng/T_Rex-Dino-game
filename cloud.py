import pygame
import random
from pygame.sprite import Sprite

class Cloud(Sprite):
    def __init__(self, dino_settings, screen):
        super(Cloud, self).__init__()
        im = pygame.image.load('images/cloud.png')
        self.image = pygame.transform.scale(im, (60, 30))
        self.dino_settings = dino_settings
        self.screen = screen
        self.rect = self.image.get_rect()
        heights = [30, 45, 50]
        self.rect.x = self.rect.width * 8
        self.rect.y = heights[random.randrange(0,3)]
        self.x = float(self.rect.x)

        self.speed_factor = dino_settings.cloud_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.right <= 0:
            return True

    def update(self):
        self.x -= self.speed_factor
        self.rect.x = self.x
