import pygame


def check_collision(player_rect, player_x, player_y, vel_x, vel_y, walls):
    player_x += vel_x
    player_rect.x = int(player_x)

    for wall in walls:
        if player_rect.colliderect(wall):
            if vel_x > 0:
                player_rect.right = wall.left
            if vel_x < 0:
                player_rect.left = wall.right
            player_x = float(player_rect.x)
            vel_x = 0

    player_y += vel_y
    player_rect.y = int(player_y)

    for wall in walls:
        if player_rect.colliderect(wall):
            if vel_y > 0:
                player_rect.bottom = wall.top
            if vel_y < 0:
                player_rect.top = wall.bottom
            player_y = float(player_rect.y)
            vel_y = 0
    
    return player_x, player_y, vel_x, vel_y