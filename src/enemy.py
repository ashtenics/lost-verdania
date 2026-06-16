import pygame
from . import pathfinding
from . import rooms
from . import physics


class Enemy:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.knockback = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(x, y, 32, 32)

        self.max_speed = 3
        self.acceleration = 0.4
        self.friction = 0.85
        self.kb_friction = 0.7

        self.path_timer = 0
        self.path = []
        self.is_pushed = False

    def handle_movement(self, player):

        if self.is_pushed:
            return

        enemy_tile = self.standing_tile()
        player_tile = player.standing_tile()
        self.path_timer += 1

        touching_player = self.rect.inflate(2, 2).colliderect(player.rect)

        if touching_player:
            self.path = []
            self.path_timer = 11

        else:
            if self.path_timer % 12 == 0:
                current_matrix = rooms.get_grid_matrix()
                new_path = pathfinding.find_path(enemy_tile, player_tile, current_matrix)
                if new_path:
                    self.path = new_path
                else:
                    self.path = []

        if len(self.path) > 1:
            next_tile = self.path[1]
            HALF_TILE = int(rooms.TILE_SIZE / 2)

            target_x = (next_tile[0] * rooms.TILE_SIZE) + HALF_TILE
            target_y = (next_tile[1] * rooms.TILE_SIZE) + HALF_TILE

            dx = target_x - self.rect.centerx
            dy = target_y - self.rect.centery
            dir_vector = pygame.Vector2(dx, dy)

            if dir_vector.length() > 4:
                dir_vector = dir_vector.normalize()
                self.vel += dir_vector * self.acceleration

        self.vel *= self.friction
        if self.vel.length() > self.max_speed:
            self.vel = self.vel.normalize() * self.max_speed
        
        self.knockback *= self.kb_friction
        if self.knockback.length() < 0.1:
            self.knockback = pygame.Vector2(0, 0)

    def standing_tile(self):
        return (int(self.rect.centerx // rooms.TILE_SIZE), int(self.rect.centery // rooms.TILE_SIZE))


def spawn_in_enemies():
    enemies_active = []
    spawn_locations = rooms.get_enemy_spawns()
    for coords in spawn_locations:

        px = coords[0] * rooms.TILE_SIZE
        py = coords[1] * rooms.TILE_SIZE

        enemy = Enemy(px, py)
        enemies_active.append(enemy)

    return enemies_active


def track_enemy_pos(enemies):
    occupied_tiles = []
    for e in enemies:
        occupied_tiles.append(e.standing_tile())
    return occupied_tiles
