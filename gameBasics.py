import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SHOOTER')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        self.image = pygame.surface((50,30))
        self.image.fill((0, 0, 255))
        self.rect = (self.image.git_rect())
        self.rect.center = (400, 550)
        self.image = pygame.image.load('player.png')
        self.x = 370
        self.y = 480
        self.x_change = 0
        self.y_change = 0

def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            if keys[pygame.K_UP]:
                self.rect.y -= 5
                if keys[pygame.K_DOWN]:
                    self.rect.y += 5

def update(self):
        self.y += self.y_change
        self.rect.y = self.y
        if self.rect.bottom < 0:
            self.kill()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

pygame.quit()

