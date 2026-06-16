import pygame

pushing_active = False

def update_entity_physics(entity, walls, entities, player):
    global pushing_active

# ==================== X-AXIS ====================

    kb_x = getattr(entity, 'knockback', pygame.Vector2(0,0)).x
    entity.pos.x += (entity.vel.x + kb_x)
    entity.rect.x = round(entity.pos.x)

    for wall in walls:
        if entity.rect.colliderect(wall):
            if (entity.vel.x + kb_x) > 0: entity.rect.right = wall.left
            elif (entity.vel.x + kb_x) < 0: entity.rect.left = wall.right
            entity.pos.x = entity.rect.x
            entity.vel.x = 0
            if hasattr(entity, 'knockback'): entity.knockback.x = 0

    for e in entities:
        if e != entity and entity.rect.colliderect(e.rect):
            if entity == player:
                if entity.vel.x > 0:
                    entity.rect.right = e.rect.left
                    e.knockback.x = player.max_speed * 1.8
                elif entity.vel.x < 0:
                    entity.rect.left = e.rect.right
                    e.knockback.x = -player.max_speed * 1.8
                entity.pos.x = entity.rect.x
            else:
                if e != player:
                    if (entity.vel.x + kb_x) > 0:
                        entity.rect.right = e.rect.left
                    elif (entity.vel.x + kb_x) < 0:
                        entity.rect.left = e.rect.right
                    entity.pos.x = entity.rect.x
                else:
                    if (entity.vel.x + kb_x) > 0:
                        entity.rect.right = player.rect.left
                        entity.knockback.x = -2
                    elif (entity.vel.x + kb_x) < 0:
                        entity.rect.left = player.rect.right
                        entity.knockback.x = 2
                    entity.pos.x = entity.rect.x
                    entity.vel.x = 0

# ==================== Y-AXIS ====================

    kb_y = getattr(entity, 'knockback', pygame.Vector2(0,0)).y
    entity.pos.y += (entity.vel.y + kb_y)
    entity.rect.y = round(entity.pos.y)

    for wall in walls:
        if entity.rect.colliderect(wall):
            if (entity.vel.y + kb_y) > 0: entity.rect.bottom = wall.top
            elif (entity.vel.y + kb_y) < 0: entity.rect.top = wall.bottom
            entity.pos.y = entity.rect.y
            entity.vel.y = 0
            if hasattr(entity, 'knockback'): entity.knockback.y = 0

    for e in entities:
        if e != entity and entity.rect.colliderect(e.rect):
            if entity == player:
                if entity.vel.y > 0:
                    entity.rect.bottom = e.rect.top
                    e.knockback.y = player.max_speed * 1.8
                elif entity.vel.y < 0:
                    entity.rect.top = e.rect.bottom
                    e.knockback.y = -player.max_speed * 1.8
                entity.pos.y = entity.rect.y
            else:
                if e != player:
                    if (entity.vel.y + kb_y) > 0:
                        entity.rect.bottom = e.rect.top
                    elif (entity.vel.y + kb_y) < 0:
                        entity.rect.top = e.rect.bottom
                    entity.pos.y = entity.rect.y
                else:
                    if (entity.vel.y + kb_y) > 0:
                        entity.rect.bottom = player.rect.top
                        entity.knockback.y = -2
                    elif (entity.vel.y + kb_y) < 0:
                        entity.rect.top = player.rect.bottom
                        entity.knockback.y = 2
                    entity.pos.y = entity.rect.y
                    entity.vel.y = 0
