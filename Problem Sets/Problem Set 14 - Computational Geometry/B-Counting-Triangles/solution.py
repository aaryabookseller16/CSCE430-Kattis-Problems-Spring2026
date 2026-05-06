while True:
    segment_count = int(input())
    if segment_count == 0:
        break
    segments = []
    for segment_number in range(segment_count):
        x1, y1, x2, y2 = map(float, input().split())
        segments.append((x1, y1, x2, y2))
    triangle_count = 0
    tiny = 0.000000001

    for first_segment in range(segment_count):
        for second_segment in range(first_segment + 1, segment_count):
            for third_segment in range(second_segment + 1, segment_count):
                how_many_pairs_touch = 0
                pairs_to_check = [(first_segment, second_segment), (first_segment, third_segment), (second_segment, third_segment)]
                for pair in pairs_to_check:
                    line_one = segments[pair[0]]
                    line_two = segments[pair[1]]
                    x1 = line_one[0]
                    y1 = line_one[1]
                    x2 = line_one[2]
                    y2 = line_one[3]
                    x3 = line_two[0]
                    y3 = line_two[1]
                    x4 = line_two[2]
                    y4 = line_two[3]
                    cross_one = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
                    cross_two = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
                    cross_three = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
                    cross_four = (x4 - x3) * (y2 - y3) - (y4 - y3) * (x2 - x3)
                    they_touch = False
                    if abs(cross_one) < tiny and min(x1, x2) - tiny <= x3 <= max(x1, x2) + tiny and min(y1, y2) - tiny <= y3 <= max(y1, y2) + tiny:
                        they_touch = True
                    if abs(cross_two) < tiny and min(x1, x2) - tiny <= x4 <= max(x1, x2) + tiny and min(y1, y2) - tiny <= y4 <= max(y1, y2) + tiny:
                        they_touch = True
                    if abs(cross_three) < tiny and min(x3, x4) - tiny <= x1 <= max(x3, x4) + tiny and min(y3, y4) - tiny <= y1 <= max(y3, y4) + tiny:
                        they_touch = True
                    if abs(cross_four) < tiny and min(x3, x4) - tiny <= x2 <= max(x3, x4) + tiny and min(y3, y4) - tiny <= y2 <= max(y3, y4) + tiny:
                        they_touch = True
                    if cross_one * cross_two < -tiny and cross_three * cross_four < -tiny:
                        they_touch = True
                    if they_touch:
                        how_many_pairs_touch += 1

                    # print("checking", pair, they_touch)
                if how_many_pairs_touch == 3:
                    triangle_count += 1

    print(triangle_count)
