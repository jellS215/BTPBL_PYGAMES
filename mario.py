import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display

screen_width = 800
screen_height = 600
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Mario Game')

# Load images
player_image = pygame.image.load('mario.png')
player_image = pygame.transform.scale(player_image, (50, 50))

background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))



PLATFORM_COLOR = (0, 255, 0)
PLATFORM_SIZE = (100, 20)
ENEMY_COLOR = (255, 0, 0)
ENEMY_SIZE = (50, 50)

# Define colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define player class

class Player(pygame.sprite.Sprite):
    def __init__(self):
        size = (50, 50)
        self.rect = pygame.Rect
        self.image = player_image
        self. position = (screen_width // 100, screen_height // 125)
        self.vel =[0,0]
        self.accel = [0,0]
        self.speed = 5
        self.jumpPower =-15
        self.gravity = 1
        self.on_ground = False

scroll_x = 0

def draw(self, surface, scroll_x):
         pygame.draw.rect(surface, (0,0,220), (self.rect.x - scroll_x, self.rect.y, self.rect.width, self.rect.height))


platforms = [
    pygame.Rect(0, screen_height-100, 2000, 40), # Ground
    pygame.Rect(300, screen_height-200, 200, 40), # Platform 1
    pygame.Rect(600, screen_height-300, 200, 40), # Platform 2
    pygame.Rect(900, screen_height-400, 200, 40), # Platform 3
]
        
   



def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep player within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

def input(self, keys):
        if keys[pygame.K_LEFT]:
            self.x_change = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.x_change = self.speed
        else:
            self.x_change = 0

        if keys[pygame.K_UP] and self.on_ground:
            self.y_change = self.jumpPower
            self.on_ground = False

        if not self.on_ground:
            self.y_change += self.gravity

        if keys[pygame.K_DOWN]:
            self.y_change = 0


# Create player instance
player = Player()

all_sprites = pygame.sprite.Group()


running = True
while running:
    fps = 60
    clock.tick(60)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()


        






