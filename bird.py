import pygame
import random
from pygame.sprite import Sprite

class Bird(Sprite):
    def __init__(self, dino_settings, screen):
        super(Bird, self).__init__()
        self.dino_settings = dino_settings
        self.screen = screen
        img = pygame.image.load('images/ptera.png')
        img = img.convert()
        width, height = img.get_width()/2, img.get_height()

        self.images = []
        for num in range(0, 2):
            rect = pygame.Rect(num * width, 0, width, height)
            surface = pygame.Surface(rect.size)
            surface.blit(img, (0,0), rect)
            
            colorkey = surface.get_at((0,0))
            surface.set_colorkey(colorkey)
            surface = pygame.transform.scale(surface, (46,40))
            self.images.append(surface)

        self.index = 0
        self.image = self.images[0]
        self.rect= self.image.get_rect()
        heights = [20, 50, 100]
        self.rect.centery = heights[random.randint(0, 2)]
        self.rect.left = 800
        self.x = float(self.rect.x)
        self.count = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.right <= 0:
            return True

    def update(self):
        self.count += 1
        self.count %= 600
        if self.count%30 == 0:
            self.index = (self.index + 1) % 2
        self.image = self.images[self.index]
        self.x -= 0.2
        self.rect.x = self.x
