import pygame

pushing_on_the_x = False
pushing_on_the_y = False

# ==================== X-AXIS ====================

def update_position_x(entity):
    entity.pos.x += entity.vel.x
    entity.rect.x = round(entity.pos.x)


def check_wall_collisions_x(entity, walls):
    for wall in walls:
        if entity.rect.colliderect(wall):
            if entity.vel.x > 0:
                entity.rect.right = wall.left
            elif entity.vel.x < 0:
                entity.rect.left = wall.right
            entity.pos.x = entity.rect.x
            entity.vel.x = 0


def handle_entity_collisions_x(entity, entities, player):
    global pushing_on_the_x

    # CASE 1: The current entity is the PLAYER
    if entity == player:
        pushing_on_the_x = False
        for e in entities:
            if e != player and entity.rect.colliderect(e.rect):
                pushing_on_the_x = True
                if entity.vel.x > 0:
                    entity.rect.right = e.rect.left
                    e.vel.x = entity.vel.x
                    e.rect.left = entity.rect.right
                    e.pos.x = e.rect.x
                elif entity.vel.x < 0:
                    entity.rect.left = e.rect.right
                    e.vel.x = entity.vel.x
                    e.rect.right = entity.rect.left
                    e.pos.x = e.rect.x
                entity.pos.x = entity.rect.x

    # CASE 2: The current entity is an ENEMY
    else:
        for e in entities:
            # If this enemy runs into another enemy
            if e != player and e != entity and entity.rect.colliderect(e.rect):
                if entity.vel.x > 0:
                    entity.rect.right = e.rect.left
                elif entity.vel.x < 0:
                    entity.rect.left = e.rect.right
                entity.pos.x = entity.rect.x
            
            # If this enemy runs into the PLAYER
            elif e == player and entity.rect.colliderect(player.rect):
                # Only stop the enemy if the player isn't actively pushing them
                if not pushing_on_the_x:
                    if entity.vel.x > 0:
                        entity.rect.right = player.rect.left
                    elif entity.vel.x < 0:
                        entity.rect.left = player.rect.right
                    entity.pos.x = entity.rect.x
                    entity.vel.x = 0

# ==================== Y-AXIS ====================

def update_position_y(entity):
    entity.pos.y += entity.vel.y
    entity.rect.y = round(entity.pos.y)


def check_wall_collisions_y(entity, walls):
    for wall in walls:
        if entity.rect.colliderect(wall):
            if entity.vel.y > 0:
                entity.rect.bottom = wall.top
            elif entity.vel.y < 0:
                entity.rect.top = wall.bottom
            entity.pos.y = entity.rect.y
            entity.vel.y = 0


def handle_entity_collisions_y(entity, entities, player):
    global pushing_on_the_y
    
    # CASE 1: The current entity is the PLAYER
    if entity == player:
        pushing_on_the_y = False
        for e in entities:
            if e != player and entity.rect.colliderect(e.rect):
                pushing_on_the_y = True
                if entity.vel.y > 0:
                    entity.rect.bottom = e.rect.top
                    e.vel.y = entity.vel.y
                    e.rect.top = entity.rect.bottom
                    e.pos.y = e.rect.y
                elif entity.vel.y < 0:
                    entity.rect.top = e.rect.bottom
                    e.vel.y = entity.vel.y
                    e.rect.bottom = entity.rect.top
                    e.pos.y = e.rect.y
                entity.pos.y = entity.rect.y

    # CASE 2: The current entity is an ENEMY
    else:
        for e in entities:
            # If this enemy runs into another enemy
            if e != player and e != entity and entity.rect.colliderect(e.rect):
                if entity.vel.y > 0:
                    entity.rect.bottom = e.rect.top
                elif entity.vel.y < 0:
                    entity.rect.top = e.rect.bottom
                entity.pos.y = entity.rect.y
            
            # If this enemy runs into the PLAYER
            elif e == player and entity.rect.colliderect(player.rect):
                if not pushing_on_the_y:
                    if entity.vel.y > 0:
                        entity.rect.bottom = player.rect.top
                    elif entity.vel.y < 0:
                        entity.rect.top = player.rect.bottom
                    entity.pos.y = entity.rect.y
                    entity.vel.y = 0
