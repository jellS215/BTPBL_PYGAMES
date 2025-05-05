import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Liar's Dice Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Font setup
font = pygame.font.Font(None, 36)

# Dice class
class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = random.randint(1, 6)
        self.rect = pygame.Rect(x, y, 50, 50)

    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 5)  # Border
        text = font.render(str(self.value), True, BLACK)
        screen.blit(text, (self.x + 15, self.y + 10))

# Function to draw the board
def draw_board(player1_dice, player2_dice, message, current_bid, is_player1_turn):
    screen.fill(GREEN)
    
    # Draw Player 1 dice (only visible if it's Player 1's turn)
    if is_player1_turn:
        for i, die in enumerate(player1_dice):
            die.draw()
    
    # Draw Player 2 dice (only visible if it's Player 2's turn)
    if not is_player1_turn:
        for i, die in enumerate(player2_dice):
            die.draw()

    # Display the message (like current bid or bluff call)
    message_text = font.render(message, True, BLUE)
    screen.blit(message_text, (300, 500))

    # Display the current bid
    bid_text = font.render(f"Current Bid: {current_bid[0]} dice of {current_bid[1]}", True, RED)
    screen.blit(bid_text, (300, 550))

    pygame.display.flip()

# Function to check if the bid is valid
def check_bid(current_bid, player1_dice, player2_dice):
    total_dice = len(player1_dice) + len(player2_dice)
    # Count how many dice match the current bid face
    all_dice = [die.value for die in player1_dice + player2_dice]
    matched_dice = all_dice.count(current_bid[1])
    return matched_dice >= current_bid[0]

# AI logic to make a random bid
def ai_make_bid(current_bid, player_dice):
    # AI will raise the bid by 1 dice or change the face value randomly
    dice_count = current_bid[0] + random.randint(1, 2)  # Increase the count
    face_value = random.randint(1, 6)  # Random face value
    return [dice_count, face_value]

# Game loop
def main():
    player1_dice = [Dice(100 + i*60, 150) for i in range(5)]
    player2_dice = [Dice(100 + i*60, 250) for i in range(5)]
    current_bid = [1, 1]  # Start with the first player bidding 1 die of any face
    message = "Player 1's turn to bid!"
    
    bid_count = 1  # Initial dice count
    bid_face = 1   # Initial dice face value (1)
    
    is_player1_turn = True  # Track whose turn it is
    game_running = True
    clock = pygame.time.Clock()

    while game_running:
        screen.fill(GREEN)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and is_player1_turn:
                    bid_count += 1  # Increase dice count
                elif event.key == pygame.K_DOWN and bid_count > 1 and is_player1_turn:
                    bid_count -= 1  # Decrease dice count
                elif event.key == pygame.K_1 and is_player1_turn:
                    bid_face = 1  # Set bid to face value 1
                elif event.key == pygame.K_2 and is_player1_turn:
                    bid_face = 2  # Set bid to face value 2
                elif event.key == pygame.K_3 and is_player1_turn:
                    bid_face = 3  # Set bid to face value 3
                elif event.key == pygame.K_4 and is_player1_turn:
                    bid_face = 4  # Set bid to face value 4
                elif event.key == pygame.K_5 and is_player1_turn:
                    bid_face = 5  # Set bid to face value 5
                elif event.key == pygame.K_6 and is_player1_turn:
                    bid_face = 6  # Set bid to face value 6
                elif event.key == pygame.K_RETURN:
                    current_bid = [bid_count, bid_face]
                    if is_player1_turn:
                        message = f"Player 1 bid: {current_bid[0]} dice of {current_bid[1]}"
                    else:
                        message = f"Player 2 bid: {current_bid[0]} dice of {current_bid[1]}"
                    
                    # Switch turn after player makes a bid
                    if is_player1_turn:
                        is_player1_turn = False
                    else:
                        # AI makes its bid after Player 1
                        ai_bid = ai_make_bid(current_bid, player2_dice)
                        message = f"Player 2 (AI) bid: {ai_bid[0]} dice of {ai_bid[1]}"
                        current_bid = ai_bid
                        is_player1_turn = True

        draw_board(player1_dice, player2_dice, message, current_bid, is_player1_turn)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
