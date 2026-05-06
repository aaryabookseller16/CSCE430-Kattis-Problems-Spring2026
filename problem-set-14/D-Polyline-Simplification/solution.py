import heapq

n, wanted_segments = map(int, input().split())
points = []
for point_number in range(n + 1):
    x, y = map(int, input().split())
    points.append((x, y))

previous_point = []
next_point = []
for point_number in range(n + 1):
    previous_point.append(point_number - 1)
    next_point.append(point_number + 1)

next_point[n] = -1
removed = [False] * (n + 1)
area_version = [0] * (n + 1)
heap = []
for point_number in range(1, n):
    left_point = previous_point[point_number]
    right_point = next_point[point_number]

    left_x, left_y = points[left_point]
    middle_x, middle_y = points[point_number]
    right_x, right_y = points[right_point]

    triangle_area = abs((middle_x - left_x) * (right_y - left_y) - (middle_y - left_y) * (right_x - left_x))
    heapq.heappush(heap, (triangle_area, point_number, area_version[point_number]))
points_to_remove = n - wanted_segments
for step in range(points_to_remove):
    while True:
        triangle_area, point_to_cut, old_version = heapq.heappop(heap)
        if removed[point_to_cut] == False and old_version == area_version[point_to_cut]:
            break
    print(point_to_cut)
    # print("cutting", point_to_cut, "area", triangle_area)

    removed[point_to_cut] = True
    left_neighbor = previous_point[point_to_cut]
    right_neighbor = next_point[point_to_cut]
    next_point[left_neighbor] = right_neighbor
    previous_point[right_neighbor] = left_neighbor
    if left_neighbor != 0:
        area_version[left_neighbor] += 1
        left_left = previous_point[left_neighbor]
        left_right = next_point[left_neighbor]
        left_x, left_y = points[left_left]
        middle_x, middle_y = points[left_neighbor]
        right_x, right_y = points[left_right]
        triangle_area = abs((middle_x - left_x) * (right_y - left_y) - (middle_y - left_y) * (right_x - left_x))
        heapq.heappush(heap, (triangle_area, left_neighbor, area_version[left_neighbor]))
    if right_neighbor != n:
        area_version[right_neighbor] += 1
        right_left = previous_point[right_neighbor]
        right_right = next_point[right_neighbor]
        left_x, left_y = points[right_left]
        middle_x, middle_y = points[right_neighbor]
        right_x, right_y = points[right_right]
        triangle_area = abs((middle_x - left_x) * (right_y - left_y) - (middle_y - left_y) * (right_x - left_x))
        heapq.heappush(heap, (triangle_area, right_neighbor, area_version[right_neighbor]))
