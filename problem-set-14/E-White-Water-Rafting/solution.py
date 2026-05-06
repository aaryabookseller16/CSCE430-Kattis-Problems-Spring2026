import math

test_cases = int(input())

for case_number in range(test_cases):
    inner_count = int(input())
    inner_polygon = []
    for point_number in range(inner_count):
        x, y = map(float, input().split())
        inner_polygon.append((x, y))

    outer_count = int(input())
    outer_polygon = []
    for point_number in range(outer_count):
        x, y = map(float, input().split())
        outer_polygon.append((x, y))

    smallest_gap = 999999999.0

    # every inner corner to every outer wall
    for inner_corner in inner_polygon:
        point_x = inner_corner[0]
        point_y = inner_corner[1]
        for wall_number in range(outer_count):
            wall_start = outer_polygon[wall_number]
            wall_end = outer_polygon[(wall_number + 1) % outer_count]

            wall_dx = wall_end[0] - wall_start[0]
            wall_dy = wall_end[1] - wall_start[1]

            along_wall = ((point_x - wall_start[0]) * wall_dx + (point_y - wall_start[1]) * wall_dy) / (wall_dx * wall_dx + wall_dy * wall_dy)
            if along_wall < 0:
                along_wall = 0
            if along_wall > 1:
                along_wall = 1

            closest_x = wall_start[0] + along_wall * wall_dx
            closest_y = wall_start[1] + along_wall * wall_dy

            distance = math.sqrt((point_x - closest_x) ** 2 + (point_y - closest_y) ** 2)
            if distance < smallest_gap:
                smallest_gap = distance

            # print("inner to outer", inner_corner, wall_start, wall_end, distance)

    # every outer corner to every inner wall, because the closest spot can be like this too
    for outer_corner in outer_polygon:
        point_x = outer_corner[0]
        point_y = outer_corner[1]
        for wall_number in range(inner_count):
            wall_start = inner_polygon[wall_number]
            wall_end = inner_polygon[(wall_number + 1) % inner_count]

            wall_dx = wall_end[0] - wall_start[0]
            wall_dy = wall_end[1] - wall_start[1]

            along_wall = ((point_x - wall_start[0]) * wall_dx + (point_y - wall_start[1]) * wall_dy) / (wall_dx * wall_dx + wall_dy * wall_dy)
            if along_wall < 0:
                along_wall = 0
            if along_wall > 1:
                along_wall = 1

            closest_x = wall_start[0] + along_wall * wall_dx
            closest_y = wall_start[1] + along_wall * wall_dy

            distance = math.sqrt((point_x - closest_x) ** 2 + (point_y - closest_y) ** 2)
            if distance < smallest_gap:
                smallest_gap = distance

            # print("outer to inner", outer_corner, wall_start, wall_end, distance)

    print(smallest_gap / 2.0)
