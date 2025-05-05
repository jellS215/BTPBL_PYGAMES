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

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(). __init__()
        self.image = pygame.surface((5,10))
        self.image.fill((255, 0, 0))
        self.rect = (self.image.git_rect())
        self.rect.center = (x,y)
        self.x = x
        self.y = y
        self.y_change = -3

    def update(self):
        self.y += self.y_change
        self.rect.y = self.y
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(). __init__()
        self.image = pygame.surface((50,50))
        self.image.fill((0, 255, 0))
        self.rect = (self.image.git_rect())
        self.rect = self.image.get_rect()
        self.rect.x = random.randint (0, 735)
        self.rect.y = random.randint (-200, -50)
        

    def update(self):
        self.rect.y +=3
        if self.rect.y > 600:
            self.rect.x = random.randint (0, 735)
            self.rect.y = random.randint (-200, -50)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

bullets = pygame.sprite.Group()

enemies = pygame.sprite.Group()
for i in range(5):
    enemy = Enemy(random.randint(0, 735), random.randint(-200, -50))
    all_sprites.add(enemy)
    enemies.add(enemy)



                


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

pygame.quit()

