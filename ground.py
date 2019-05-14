import pygame

class Ground():
    def __init__(self, dino_settings, screen):
        self.screen = screen
        self.image_1 = pygame.image.load('images/ground.png')
        self.image_2 = pygame.image.load('images/ground.png')
        self.rect_1 = self.image_1.get_rect()
        self.rect_2 = self.image_2.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect_1.bottom = self.screen_rect.bottom
        self.rect_2.bottom = self.screen_rect.bottom
        self.rect_1.left = self.screen_rect.left
        self.rect_2.left = self.rect_1.right

        self.speed_factor = dino_settings.ground_speed

    def blitme(self):
        self.screen.blit(self.image_1, self.rect_1)
        self.screen.blit(self.image_2, self.rect_2)

    def update(self):
        self.rect_1.left -= self.speed_factor
        self.rect_2.left -= self.speed_factor
        if self.rect_1.right < 0:
            self.rect_1.left = self.rect_2.right
        if self.rect_2.right < 0:
            self.rect_2.left = self.rect_1.right
