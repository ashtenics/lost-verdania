import sys
import pygame
from pyhsics import check_collision

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("An ass of a game :(")

clock = pygame.time.Clock()

enemy_rect = pygame.Rect(725, 25, 50, 50)
player_rect = pygame.Rect(375, 275, 50, 50)
walls = [
    pygame.Rect(100, 100, 600, 50),
    pygame.Rect(500, 200, 100, 200),
    pygame.Rect(200, 400, 200, 50)
]

player_x = float(player_rect.x)
player_y = float(player_rect.y)

vel_x = 0.0
vel_y = 0.0

ACCELERATION = 1.2
FRICTION = 0.75
MAX_SPEED = 8.0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    acc_x = 0
    acc_y = 0

    if keys[pygame.K_RIGHT]:
        acc_x = ACCELERATION
    if keys[pygame.K_LEFT]:
        acc_x = -ACCELERATION
    if keys[pygame.K_DOWN]:
        acc_y = ACCELERATION
    if keys[pygame.K_UP]:
        acc_y = -ACCELERATION
    
    vel_x += acc_x
    vel_y += acc_y

    vel_x *= FRICTION
    vel_y *= FRICTION

    if vel_x > MAX_SPEED:  vel_x = MAX_SPEED
    if vel_x < -MAX_SPEED:  vel_x = -MAX_SPEED
    if vel_y > MAX_SPEED:  vel_y = MAX_SPEED
    if vel_y < -MAX_SPEED: vel_y = -MAX_SPEED

    player_x, player_y, vel_x, vel_y = check_collision(player_rect, player_x, player_y, vel_x, vel_y, walls)

    screen.fill((40, 40, 40))

    pygame.draw.rect(screen, (255, 255, 255), enemy_rect)
    pygame.draw.rect(screen, (46, 204, 113), player_rect)
    pygame.draw.line(screen, (255, 0, 0), (enemy_rect.centerx, enemy_rect.centery), (player_rect.centerx, player_rect.centery), 10)

    for wall in walls:
        pygame.draw.rect(screen, (231, 76, 60), wall)

    pygame.display.flip()

    clock.tick(60)
