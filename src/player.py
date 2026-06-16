import pygame
from . import rooms


class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(x, y, 32, 32)

        self.max_speed = 5
        self.acceleration = 0.6
        self.friction = 0.9
        self.push_strength = 0.5

    def handle_input(self):
        move_input = pygame.Vector2(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  move_input.x -= 1
        if keys[pygame.K_d]: move_input.x += 1
        if keys[pygame.K_w]:    move_input.y -= 1
        if keys[pygame.K_s]:  move_input.y += 1

        if move_input.magnitude() > 0:
            move_input = move_input.normalize()
            self.vel += move_input * self.acceleration

        self.vel *= self.friction

        if self.vel.magnitude() > self.max_speed:
            self.vel = self.vel.normalize() * self.max_speed

        if self.vel.magnitude() < 0.1:
            self.vel = pygame.Vector2(0, 0)

    def standing_tile(self):
        return (self.rect.centerx // rooms.TILE_SIZE, self.rect.centery // rooms.TILE_SIZE)
