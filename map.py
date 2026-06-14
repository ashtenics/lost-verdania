import pygame


TILE_SIZE = 32

MAP_LAYOUT = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W............................W",
    "W....W..................W....W",
    "W....WWWW............WWWW....W",
    "W............................W",
    "W............................W",
    "W............................W",
    "W............................W",
    "W............................W",
    "W............................W",
    "W............................W",
    "W............................W",
    "W....WWWWWWWWWWWWWWWWWWWW....W",
    "W............................W",
    "W............................W",
    "W............................W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

def load_map():
    walls = []

    for row_index, row in enumerate(MAP_LAYOUT):
        for col_index, character in enumerate(row):
            if character == "W":
                x_pixel = col_index * TILE_SIZE
                y_pixel = row_index * TILE_SIZE

                wall_rect = pygame.Rect(x_pixel, y_pixel, 32, 32)
                walls.append(wall_rect)

    return walls
