import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display

screen_width = 1920
screen_height = 1080
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))




running = True
while running:
    fps = 60
    clock.tick(60)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()