import sys
import pygame
from src import physics
from src import enemy
from src import player
from src import rooms

pygame.init()
clock = pygame.time.Clock()

GRID_WIDTH = 30
GRID_HEIGHT = 17
WINDOW_WIDTH = GRID_WIDTH * rooms.TILE_SIZE   # 960
WINDOW_HEIGHT = GRID_HEIGHT * rooms.TILE_SIZE # 544

rooms.load_room_from_json()
rooms.current_room_id = "room_01"
walls = rooms.load_room()

enemies = enemy.spawn_in_enemies()
player = player.Player(50, 50)

pygame.display.set_caption("An ass of a game :(")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT)).convert()
for wall in walls:
    pygame.draw.rect(background_surface, (231, 76, 60), wall)

game_running = True
while game_running:
    # ---- INPUT PHASE ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    player.handle_input()

    # ---- UPDATE PHASE ----
    for e in enemies:
        e.handle_movement(player)
        physics.update_entity_physics(e, walls)
    physics.update_entity_physics(player, walls)

    # ---- RENDERING PHASE ----
    screen.fill((40, 40, 40))
    screen.blit(background_surface, (0, 0))

    for e in enemies:
        pygame.draw.rect(screen, (255, 0, 0), e.rect)
    pygame.draw.rect(screen, (0, 255, 0), player.rect)

    pygame.display.flip()
    clock.tick(60)

print("Exited loop.")
pygame.quit()
sys.exit()
