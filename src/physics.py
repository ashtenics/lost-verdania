import pygame

def update_entity_physics(entity, walls):
    entity.pos.x += entity.vel.x
    entity.rect.x = round(entity.pos.x)

    for wall in walls:
        if entity.rect.colliderect(wall):
            if entity.vel.x > 0:
                entity.rect.right = wall.left
            elif entity.vel.x < 0:
                entity.rect.left = wall.right
            entity.pos.x = entity.rect.x
            entity.vel.x = 0

    entity.pos.y += entity.vel.y
    entity.rect.y = round(entity.pos.y)

    for wall in walls:
        if entity.rect.colliderect(wall):
            if entity.vel.y > 0:
                entity.rect.bottom = wall.top
            elif entity.vel.y < 0:
                entity.rect.top = wall.bottom

            entity.pos.y = entity.rect.y
            entity.vel.y = 0
