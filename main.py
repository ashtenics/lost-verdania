import sys
import pygame
from pyhsics import update_player_physics
from player import Player
import map

pygame.init()
clock = pygame.time.Clock()

TILE_SIZE = 32
GRID_WIDTH = 30
GRID_HEIGHT = 17
WINDOW_WIDTH = GRID_WIDTH * TILE_SIZE   # 960
WINDOW_HEIGHT = GRID_HEIGHT * TILE_SIZE # 544

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("An ass of a game :(")

walls = map.load_map()
player = Player(100, 100)
game_running = True

while game_running:
    # ---- INPUT PHASE ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    player.handle_input()

    # ---- UPDATE PHASE ----
    update_player_physics(player, walls)

    # ---- RENDERING PHASE ----
    screen.fill((40, 40, 40))

    for wall in walls:
        pygame.draw.rect(screen, (231, 76, 60), wall)

    pygame.draw.rect(screen, (0, 255, 0), player.rect)

    pygame.display.flip()
    clock.tick(60)

print("Exited loop.")
pygame.quit()
sys.exit()
