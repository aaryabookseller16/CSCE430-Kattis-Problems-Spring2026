import math

while True:
    numbers = []
    while len(numbers) == 0:
        numbers = list(map(int, input().split()))
    corner_count = numbers[0]
    if corner_count == 0:
        break
    while len(numbers) < 1 + corner_count * 2:
        numbers += list(map(int, input().split()))
    polygon = []
    place = 1
    for corner_number in range(corner_count):
        x = numbers[place]
        y = numbers[place + 1]
        polygon.append((x, y))
        place += 2
    while len(polygon) > 3:
        corner_angles = []

        for corner_number in range(len(polygon)):
            previous_corner = polygon[(corner_number - 1) % len(polygon)]
            current_corner = polygon[corner_number]
            next_corner = polygon[(corner_number + 1) % len(polygon)]

            first_x = previous_corner[0] - current_corner[0]
            first_y = previous_corner[1] - current_corner[1]
            second_x = next_corner[0] - current_corner[0]
            second_y = next_corner[1] - current_corner[1]

            dot_product = first_x * second_x + first_y * second_y
            first_length = math.sqrt(first_x * first_x + first_y * first_y)
            second_length = math.sqrt(second_x * second_x + second_y * second_y)
            angle_cos = dot_product / (first_length * second_length)
            if angle_cos < -1:
                angle_cos = -1
            if angle_cos > 1:
                angle_cos = 1
            corner_angles.append(math.acos(angle_cos))
        sharpest_corner = 0
        for corner_number in range(1, len(corner_angles)):
            if corner_angles[corner_number] < corner_angles[sharpest_corner]:
                sharpest_corner = corner_number
        old_sharpest_angle = corner_angles[sharpest_corner]
        maybe_polygon = polygon[:sharpest_corner] + polygon[sharpest_corner + 1:]
        new_corner_angles = []
        for corner_number in range(len(maybe_polygon)):
            previous_corner = maybe_polygon[(corner_number - 1) % len(maybe_polygon)]
            current_corner = maybe_polygon[corner_number]
            next_corner = maybe_polygon[(corner_number + 1) % len(maybe_polygon)]

            first_x = previous_corner[0] - current_corner[0]
            first_y = previous_corner[1] - current_corner[1]
            second_x = next_corner[0] - current_corner[0]
            second_y = next_corner[1] - current_corner[1]

            dot_product = first_x * second_x + first_y * second_y
            first_length = math.sqrt(first_x * first_x + first_y * first_y)
            second_length = math.sqrt(second_x * second_x + second_y * second_y)

            angle_cos = dot_product / (first_length * second_length)
            if angle_cos < -1:
                angle_cos = -1
            if angle_cos > 1:
                angle_cos = 1

            new_corner_angles.append(math.acos(angle_cos))
        new_sharpest_angle = min(new_corner_angles)

        # print("trying to cut", polygon[sharpest_corner], old_sharpest_angle, new_sharpest_angle)
        if new_sharpest_angle > old_sharpest_angle + 0.000000000001:
            polygon = maybe_polygon
        else:
            break

    answer = [str(len(polygon))]
    for corner in polygon:
        answer.append(str(corner[0]))
        answer.append(str(corner[1]))

    print(" ".join(answer))
