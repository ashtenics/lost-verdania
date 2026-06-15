import sys
import pygame
import pyhsics
from player import Player
from enemy import Enemy
import rooms

pygame.init()
clock = pygame.time.Clock()

GRID_WIDTH = 30
GRID_HEIGHT = 17
WINDOW_WIDTH = GRID_WIDTH * rooms.TILE_SIZE   # 960
WINDOW_HEIGHT = GRID_HEIGHT * rooms.TILE_SIZE # 544

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("An ass of a game :(")

rooms.load_room_from_json()
rooms.current_room_id = "room_03"
walls = rooms.load_room()

enemy = Enemy(384, 352)
player = Player(50, 50)
game_running = True

while game_running:
    # ---- INPUT PHASE ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    player.handle_input()

    # ---- UPDATE PHASE ----
    enemy.handle_movement(player)
    pyhsics.update_entity_physics(player, walls)
    pyhsics.update_entity_physics(enemy, walls)

    # ---- RENDERING PHASE ----
    screen.fill((40, 40, 40))

    for wall in walls:
        pygame.draw.rect(screen, (231, 76, 60), wall)

    pygame.draw.rect(screen, (255, 0, 0), enemy.rect)
    pygame.draw.rect(screen, (0, 255, 0), player.rect)

    pygame.display.flip()
    clock.tick(60)

print("Exited loop.")
pygame.quit()
sys.exit()
