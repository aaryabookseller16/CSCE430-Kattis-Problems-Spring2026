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
    smallest_gap = 10 ** 18

    for inner_wall_number in range(inner_count):
        inner_start = inner_polygon[inner_wall_number]
        inner_end = inner_polygon[(inner_wall_number + 1) % inner_count]
        for outer_wall_number in range(outer_count):
            outer_start = outer_polygon[outer_wall_number]
            outer_end = outer_polygon[(outer_wall_number + 1) % outer_count]
            # inner wall start to outer wall
            wall_dx = outer_end[0] - outer_start[0]
            wall_dy = outer_end[1] - outer_start[1]
            along_wall = ((inner_start[0] - outer_start[0]) * wall_dx + (inner_start[1] - outer_start[1]) * wall_dy) / (wall_dx * wall_dx + wall_dy * wall_dy)
            if along_wall < 0:
                along_wall = 0
            if along_wall > 1:
                along_wall = 1
            closest_x = outer_start[0] + along_wall * wall_dx
            closest_y = outer_start[1] + along_wall * wall_dy
            smallest_gap = min(smallest_gap, math.hypot(inner_start[0] - closest_x, inner_start[1] - closest_y))

            # inner wall end to outer wall
            along_wall = ((inner_end[0] - outer_start[0]) * wall_dx + (inner_end[1] - outer_start[1]) * wall_dy) / (wall_dx * wall_dx + wall_dy * wall_dy)
            if along_wall < 0:
                along_wall = 0
            if along_wall > 1:
                along_wall = 1
            closest_x = outer_start[0] + along_wall * wall_dx
            closest_y = outer_start[1] + along_wall * wall_dy
            smallest_gap = min(smallest_gap, math.hypot(inner_end[0] - closest_x, inner_end[1] - closest_y))

            # outer wall start to inner wall
            wall_dx = inner_end[0] - inner_start[0]
            wall_dy = inner_end[1] - inner_start[1]
            along_wall = ((outer_start[0] - inner_start[0]) * wall_dx + (outer_start[1] - inner_start[1]) * wall_dy) / (wall_dx * wall_dx + wall_dy * wall_dy)
            if along_wall < 0:
                along_wall = 0
            if along_wall > 1:
                along_wall = 1
            closest_x = inner_start[0] + along_wall * wall_dx
            closest_y = inner_start[1] + along_wall * wall_dy
            smallest_gap = min(smallest_gap, math.hypot(outer_start[0] - closest_x, outer_start[1] - closest_y))

            # outer wall end to inner wall
            along_wall = ((outer_end[0] - inner_start[0]) * wall_dx + (outer_end[1] - inner_start[1]) * wall_dy) / (wall_dx * wall_dx + wall_dy * wall_dy)
            if along_wall < 0:
                along_wall = 0
            if along_wall > 1:
                along_wall = 1
            closest_x = inner_start[0] + along_wall * wall_dx
            closest_y = inner_start[1] + along_wall * wall_dy
            smallest_gap = min(smallest_gap, math.hypot(outer_end[0] - closest_x, outer_end[1] - closest_y))
            # print("edge pair", inner_start, inner_end, outer_start, outer_end, smallest_gap)

    print(smallest_gap / 2)
