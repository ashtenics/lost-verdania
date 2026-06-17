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
rooms.current_room_id = "room_02"
walls = rooms.load_room()

enemies = enemy.spawn_in_enemies()
hero = player.Player(50, 50)
all_entities = [hero]
all_entities.extend(enemies)

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
    hero.handle_input()

    # ---- UPDATE PHASE ----

    occupied_tiles = enemy.track_enemy_pos(enemies)

    for e in enemies:
        if not e.rect.colliderect(hero.rect):
            e.handle_movement(hero, "active")
        else:
            e.handle_movement(hero, "ragdoll")

    for entity in all_entities:
        physics.update_position_x(entity)
        physics.handle_entity_collisions_x(entity, all_entities, hero)
        physics.check_wall_collisions_x(entity, walls)

        physics.update_position_y(entity)
        physics.handle_entity_collisions_y(entity, all_entities, hero)
        physics.check_wall_collisions_y(entity, walls)

    # ---- RENDERING PHASE ----
    screen.fill((40, 40, 40))
    screen.blit(background_surface, (0, 0))

    for e in enemies:
        pygame.draw.rect(screen, (255, 0, 0), e.rect)
    pygame.draw.rect(screen, (0, 255, 0), hero.rect)

    pygame.display.flip()
    clock.tick(60)

print("Exited loop.")
pygame.quit()
sys.exit()
