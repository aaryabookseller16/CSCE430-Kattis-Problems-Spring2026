while True:
    segment_count = int(input())
    if segment_count == 0:
        break

    segments = []
    for segment_number in range(segment_count):
        x1, y1, x2, y2 = map(float, input().split())
        segments.append((x1, y1, x2, y2))

    tiny = 0.000000001
    intersects = []
    for row in range(segment_count):
        intersects.append([False] * segment_count)

    for first_segment in range(segment_count):
        for second_segment in range(first_segment + 1, segment_count):
            first_line = segments[first_segment]
            second_line = segments[second_segment]

            x1 = first_line[0]
            y1 = first_line[1]
            x2 = first_line[2]
            y2 = first_line[3]

            x3 = second_line[0]
            y3 = second_line[1]
            x4 = second_line[2]
            y4 = second_line[3]

            first_cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            second_cross = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
            third_cross = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
            fourth_cross = (x4 - x3) * (y2 - y3) - (y4 - y3) * (x2 - x3)

            pair_touches = False

            if abs(first_cross) < tiny and min(x1, x2) - tiny <= x3 <= max(x1, x2) + tiny and min(y1, y2) - tiny <= y3 <= max(y1, y2) + tiny:
                pair_touches = True
            if abs(second_cross) < tiny and min(x1, x2) - tiny <= x4 <= max(x1, x2) + tiny and min(y1, y2) - tiny <= y4 <= max(y1, y2) + tiny:
                pair_touches = True
            if abs(third_cross) < tiny and min(x3, x4) - tiny <= x1 <= max(x3, x4) + tiny and min(y3, y4) - tiny <= y1 <= max(y3, y4) + tiny:
                pair_touches = True
            if abs(fourth_cross) < tiny and min(x3, x4) - tiny <= x2 <= max(x3, x4) + tiny and min(y3, y4) - tiny <= y2 <= max(y3, y4) + tiny:
                pair_touches = True

            if first_cross * second_cross < -tiny and third_cross * fourth_cross < -tiny:
                pair_touches = True

            intersects[first_segment][second_segment] = pair_touches
            intersects[second_segment][first_segment] = pair_touches

            # print("pair", first_segment, second_segment, pair_touches)

    answer = 0
    for first_segment in range(segment_count):
        for second_segment in range(first_segment + 1, segment_count):
            for third_segment in range(second_segment + 1, segment_count):
                if intersects[first_segment][second_segment] and intersects[first_segment][third_segment] and intersects[second_segment][third_segment]:
                    answer += 1

    print(answer)
