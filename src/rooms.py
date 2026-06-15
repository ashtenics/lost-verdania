import pygame
import json


TILE_SIZE = 32

_MAP_DATA = {}
current_room_id = "room_01"


def load_room_from_json(filepath="data/rooms.json"):
    global _MAP_DATA
    with open(filepath, "r") as file:
        data = json.load(file)
        _MAP_DATA = data["rooms"]


def get_current_layout():
    return _MAP_DATA.get(current_room_id, {}).get("layout", [])


def load_room():
    walls = []
    layout = get_current_layout()

    for row_index, row in enumerate(layout):
        for col_index, character in enumerate(row):
            if character == "W":
                wall_rect = pygame.Rect(col_index * TILE_SIZE, row_index * TILE_SIZE, 32, 32)
                walls.append(wall_rect)

    return walls


def get_grid_matrix():
    matrix = []
    layout = get_current_layout()

    for row in layout:
        matrix_row = []
        for character in row:
            if character == "W":
                matrix_row.append(1)
            else:
                matrix_row.append(0)
        matrix.append(matrix_row)
    
    return matrix


def get_enemy_spawns():
    return _MAP_DATA.get(current_room_id, {}).get("enemy_spawns", [])
