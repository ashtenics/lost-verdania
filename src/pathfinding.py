from . import rooms


def find_path(start_coords, target_coords, matrix):
    queue = [start_coords]
    visited = [start_coords]
    parent_map = {}

    found_target = False

    while len(queue) > 0:
        current = queue.pop(0)

        if current == target_coords:
            found_target = True
            break

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            neighbor_x = current[0] + dx
            neighbor_y = current[1] + dy
            neighbor = (neighbor_x, neighbor_y)

            if dx != 0 and dy != 0:
                side_1 = matrix[current[1]][current[0] + dx]
                side_2 = matrix[current[1] + dy][current[0]]

                if side_1 == 1 or side_2 == 1:
                    continue

            if 0 <= neighbor_y < len(matrix) and 0 <= neighbor_x < len(matrix[0]):
                if matrix[neighbor_y][neighbor_x] == 0 and neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)

                    parent_map[neighbor] = current

    if not found_target:
        return []

    path = []
    current_tile = target_coords
    while current_tile != start_coords:
        path.append(current_tile)
        current_tile = parent_map[current_tile]

    path.append(start_coords)
    path.reverse()

    return path
