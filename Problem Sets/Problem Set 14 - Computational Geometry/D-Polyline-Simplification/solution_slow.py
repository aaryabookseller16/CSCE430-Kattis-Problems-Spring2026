n, wanted_segments = map(int, input().split())

points = []
for point_number in range(n + 1):
    x, y = map(int, input().split())
    points.append((x, y))

active_points = []
for point_number in range(n + 1):
    active_points.append(point_number)

points_to_remove = n - wanted_segments

for step in range(points_to_remove):
    best_area = 10 ** 30
    best_place_in_list = -1
    best_original_index = -1

    for place_in_list in range(1, len(active_points) - 1):
        left_point = active_points[place_in_list - 1]
        middle_point = active_points[place_in_list]
        right_point = active_points[place_in_list + 1]

        left_x, left_y = points[left_point]
        middle_x, middle_y = points[middle_point]
        right_x, right_y = points[right_point]

        triangle_area = abs((middle_x - left_x) * (right_y - left_y) - (middle_y - left_y) * (right_x - left_x))

        if triangle_area < best_area or (triangle_area == best_area and middle_point < best_original_index):
            best_area = triangle_area
            best_place_in_list = place_in_list
            best_original_index = middle_point

    print(best_original_index)
    # print("slow cut", best_original_index, best_area)

    active_points.pop(best_place_in_list)
