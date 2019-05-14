import pygame

class Dinosaur():
    def __init__(self, dino_settings, screen):
        self.screen = screen
        self.dino_settings = dino_settings
        
        img_1 = pygame.image.load('images/dino.png')
        img_1 = img_1.convert()
        width_1, height_1 = img_1.get_width()/5, img_1.get_height()

        self.images_1 = []
        for num in range(0, 5):
            rect_1 = pygame.Rect(num * width_1, 0, width_1, height_1)
            surface_1 = pygame.Surface(rect_1.size)
            surface_1.blit(img_1, (0,0), rect_1)
            
            colorkey_1 = surface_1.get_at((0,0))
            surface_1.set_colorkey(colorkey_1)
            surface_1 = pygame.transform.scale(surface_1, (44,47))
            self.images_1.append(surface_1)

        self.index = 0
        self.image = self.images_1[0]
        self.rect= self.images_1[0].get_rect()
        self.rect.bottom = 147
        self.rect.left = 40


        img_2 = pygame.image.load('images/dino_ducking.png')
        img_2 = img_2.convert()
        width_2, height_2 = img_2.get_width()/2, img_2.get_height()
        self.images_2 = []
        for num in range(0, 2):
            rect_2 = pygame.Rect(num * width_2, 0, width_2, height_2)
            surface_2 = pygame.Surface(rect_2.size)
            surface_2.blit(img_2, (0,0), rect_2)
            colorkey_2 = surface_2.get_at((0,0))
            surface_2.set_colorkey(colorkey_2)
            surface_2 = pygame.transform.scale(surface_2, (59,47))
            self.images_2.append(surface_2)

        self.y = self.rect.centery
        self.jumping = False
        self.dead = False
        self.ducking = False
        self.uping = False

        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.jumping:
            self.index = 0
            self.image = self.images_1[self.index]

            if self.uping:
                self.y -= 0.3
                self.rect.centery = int(self.y)
                if self.rect.top <= 10:
                    self.uping = False
            elif not self.uping:
                self.y += 0.3
                self.rect.centery = int(self.y)
                if self.rect.bottom >= 147:
                   self.jumping = False
        elif self.ducking:
            self.index = (self.index + 1) % 2
            self.image = self.images_2[self.index]
        elif self.dead:
            self.index = 4
            self.image = self.images_1[self.index]
        else:
            if self.rect.bottom < 147:
                self.rect.centery += 1
            else: 
                self.index = (self.index + 1) % 2 + 2
                self.image = self.images_1[self.index]
