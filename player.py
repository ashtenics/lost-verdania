import pygame


class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(x, y, 32, 32)

        self.max_speed = 5
        self.acceleration = 0.6
        self.friction = 0.9

    def handle_input(self):
        move_input = pygame.Vector2(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  move_input.x -= 1
        if keys[pygame.K_RIGHT]: move_input.x += 1
        if keys[pygame.K_UP]:    move_input.y -= 1
        if keys[pygame.K_DOWN]:  move_input.y += 1

        if move_input.magnitude() > 0:
            move_input = move_input.normalize()
            self.vel += move_input * self.acceleration

        self.vel *= self.friction

        if self.vel.magnitude() > self.max_speed:
            self.vel = self.vel.normalize() * self.max_speed

        if self.vel.magnitude() < 0.1:
            self.vel = pygame.Vector2(0, 0)
