import pygame
import sys
from cloud import Cloud
from bird import Bird
from cactus import Cactus
from time import sleep
from scoreboard import Scoreboard

def reset(dino_settings, screen, dinosaur, bird, cactus):
    return


def check_events(dinosaur):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dinosaur.jumping = True
                dinosaur.uping = True
            if event.key == pygame.K_DOWN:
                dinosaur.ducking = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                dinosaur.ducking = False


def create_cc(dino_settings, screen, cactus, cactus_num):
    cc = Cactus(dino_settings, screen)
    cc_width = cc.rect.width
    cc.x = 700 * (cactus_num+1)
    cc.rect.x = cc.x
    cactus.add(cc)


def create_cactus(dino_settings, screen, cactus):
    number_cactus_x = 3
    for cactus_num in range(number_cactus_x):
        create_cc(dino_settings, screen, cactus, cactus_num)


def create_bird(dino_settings, screen, birds, bird_num):
    bird = Bird(dino_settings, screen)
    bird_width = bird.rect.width
    bird.x = 1000 * (bird_num + 1)
    bird.rect.x = bird.x
    birds.add(bird)


def create_birds(dino_settings, screen, birds):
    number_birds_x = 3
    for bird_num in range(number_birds_x):
        create_bird(dino_settings, screen, birds, bird_num)


def create_cloud(dino_settings, screen, clouds, cloud_num):
    cloud = Cloud(dino_settings, screen)
    cloud_width = cloud.rect.width
    cloud.x = cloud_width + 10 * cloud_width * cloud_num
    cloud.rect.x = cloud.x
    clouds.add(cloud)
    

def create_clouds(dino_settings, screen, clouds):
    number_clouds_x = 3
    
    for cloud_num in range(number_clouds_x):
        create_cloud(dino_settings, screen, clouds, cloud_num)


def update_clouds(dino_settings, screen, clouds):
    clouds.update()
    for cloud in clouds:
        if cloud.check_edges():
            clouds.remove(cloud)
            create_cloud(dino_settings, screen, clouds, 2)

def update_birds(dino_settings, screen, birds, dinosaur):
    birds.update()
    for bird in birds:
        if bird.check_edges():
            birds.remove(bird)
            create_bird(dino_settings, screen, birds, 2)
        elif pygame.sprite.collide_mask(bird, dinosaur):
            dinosaur.dead = True
            

def update_cactus(dino_settings, screen, cactus, dinosaur):
    cactus.update()
    for cc in cactus:
        if cc.check_edges():
            cactus.remove(cc)
            create_cc(dino_settings, screen, cactus, 2)
        elif pygame.sprite.collide_mask(cc, dinosaur):
            dinosaur.dead = True
     

def update_screen(dino_settings, screen, ground, clouds, dinosaur, cactus, birds, sb):
    screen.fill(dino_settings.bg_color)
    ground.blitme()
    clouds.draw(screen)
    birds.draw(screen)
    cactus.draw(screen)
    dinosaur.blitme()
    sb.show_score()
    pygame.display.flip()
