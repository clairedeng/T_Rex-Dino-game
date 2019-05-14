import sys

import pygame

from time import sleep
from settings import Settings
import game_functions as gf
from ground import Ground
from cloud import Cloud
from pygame.sprite import Group
from dinosaur import Dinosaur
from cactus import Cactus
from bird import Bird
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    dino_settings = Settings()
    screen = pygame.display.set_mode((dino_settings.screen_width, dino_settings.screen_height))
    pygame.display.set_caption("dino")
    score = float(0)
    while True:
        ground = Ground(dino_settings, screen)
        dinosaur = Dinosaur(dino_settings, screen)
        clouds = Group()
        birds = Group()
        cactus = Group()
        gf.create_clouds(dino_settings, screen, clouds)
        gf.create_birds(dino_settings, screen, birds)
        gf.create_cactus(dino_settings, screen, cactus)
        sb = Scoreboard(dino_settings, screen)
        while not dinosaur.dead:
            gf.check_events(dinosaur)
            ground.update()
            dinosaur.update()
            score += 3
            dino_settings.score = int(score)
            sb.prep_score()
            gf.update_clouds(dino_settings, screen, clouds)
            gf.update_birds(dino_settings, screen, birds, dinosaur)
            gf.update_cactus(dino_settings, screen, cactus, dinosaur)
            gf.update_screen(dino_settings, screen, ground, clouds, dinosaur, cactus, birds, sb)
        while dinosaur.dead:
            exit_game = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if button.rect.collidepoint(mouse_x, mouse_y):
                        exit_game = True
            if exit_game:
                if dino_settings.score > dino_settings.high_score:
                    dino_settings.high_score = dino_settings.score
                    sb.prep_high_score()
                dino_settings.score = 0
                score = 0
                break
            
            button = Button(dino_settings, screen)
            button.blitme()
            pygame.display.flip()
            
run_game()
