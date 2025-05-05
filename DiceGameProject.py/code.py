import random
import pygame as pg

# Dice position (center of screen or wherever you want)
x = 350
y = 250

# Dice size (assumes dice images are 200x200)
DICE_SIZE = 200

# Create clickable area (we update its position to follow dice image)
DICE_RECT = pg.Rect(x, y, DICE_SIZE, DICE_SIZE)

def load_images():
    images = {}
    for i in range(1, 7):
        images[i] = pg.image.load(f'dice{i}.png').convert_alpha()
    return images

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Dice Roller")

    dice_images = load_images()

    # Load and scale background
    background = pg.image.load("background.jpg").convert()
    background = pg.transform.scale(background, (800, 600))

    # Default dice face (start with 1)
    roll = 1

    clock = pg.time.Clock()
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if DICE_RECT.collidepoint(mouse_pos):
                    roll = random.randint(1, 6)
                    print(f"Dice rolled: {roll}")

        # Draw background
        screen.blit(background, (0, 0))

        # Draw the dice image
        screen.blit(dice_images[roll], (x, y))

        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    main()
