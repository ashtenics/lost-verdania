import pygame


def update_player_physics(player, walls):
    player.pos.x += player.vel.x

    player.rect.x = int(player.pos.x)

    for wall in walls:
        if player.rect.colliderect(wall):
            if player.vel.x > 0:
                player.rect.right = wall.left
            elif player.vel.x < 0:
                player.rect.left = wall.right
            player.pos.x = player.rect.x
    
    player.pos.y += player.vel.y
    
    player.rect.y = int(player.pos.y)

    for wall in walls:
        if player.rect.colliderect(wall):
            if player.vel.y > 0:
                player.rect.bottom = wall.top
            if player.vel.y < 0:
                player.rect.top = wall.bottom
            player.pos.y = player.rect.y
