import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)
BLOCK_COLOR = (255, 0, 0)


clock = pygame.time.Clock()


player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 7

block_size = 50
block_speed = 5
blocks = []


font = pygame.font.SysFont("Arial", 30)

def draw_player(x, y):
    pygame.draw.rect(screen, PLAYER_COLOR, (x, y, player_size, player_size))

def drop_block():
    x_pos = random.randint(0, WIDTH - block_size)
    return [x_pos, 0]

def draw_blocks(blocks):
    for block in blocks:
        pygame.draw.rect(screen, BLOCK_COLOR, (block[0], block[1], block_size, block_size))

def collision(player_rect, block_rect):
    return player_rect.colliderect(block_rect)


def game_loop():
    global player_x
    score = 0
    blocks.clear()
    blocks.append(drop_block())

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        for block in blocks:
            block[1] += block_speed
            if block[1] > HEIGHT:
                blocks.remove(block)
                blocks.append(drop_block())
                score += 1

        
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        for block in blocks:
            block_rect = pygame.Rect(block[0], block[1], block_size, block_size)
            if collision(player_rect, block_rect):
                running = False

        draw_player(player_x, player_y)
        draw_blocks(blocks)

        
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)


    screen.fill(WHITE)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

if __name__ == "__main__":
    game_loop()
