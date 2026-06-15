import pygame
import pathfinding
import rooms


class Enemy:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(x, y, 32, 32)

        self.max_speed = 3
        self.acceleration = 0.4
        self.friction = 0.85

    def handle_movement(self, player):
        enemy_tile = self.standing_tile()
        player_tile = player.standing_tile()

        current_matrix = rooms.get_grid_matrix()
        path = pathfinding.find_path(enemy_tile, player_tile, current_matrix)

        if len(path) > 1:
            next_tile = path[1]

            target_x = (next_tile[0] * rooms.TILE_SIZE) + 16
            target_y = (next_tile[1] * rooms.TILE_SIZE) + 16

            dx = target_x - self.rect.centerx
            dy = target_y - self.rect.centery
            dir_vector = pygame.Vector2(dx, dy)

            if dir_vector.length() > 4:
                dir_vector = dir_vector.normalize()
                self.vel += dir_vector * self.acceleration

        self.vel *= self.friction

        if self.vel.length() > self.max_speed:
            self.vel = self.vel.normalize() * self.max_speed

    def standing_tile(self):
        return (int(self.rect.centerx // rooms.TILE_SIZE), int(self.rect.centery // rooms.TILE_SIZE))
