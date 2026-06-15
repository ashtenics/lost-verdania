import rooms


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

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[1] < len(matrix) and 0 <= neighbor[0] < len(matrix[0]):
                if matrix[neighbor[1]][neighbor[0]] == 0 and neighbor not in visited:
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
