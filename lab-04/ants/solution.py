import sys

input_numbers = list(map(int, sys.stdin.buffer.read().split()))

if not input_numbers:
    sys.exit(0)

total_test_cases = input_numbers[0]
current_number_index = 1
answer_lines = []

for _ in range(total_test_cases):
    pole_length_cm = input_numbers[current_number_index] #get pole length
    current_number_index += 1

    ants_on_pole_count = input_numbers[current_number_index]
    current_number_index += 1

    earliest_time_when_all_fall = 0
    latest_time_when_all_fall = 0

    # read each ant position and update earliest/latest possibilities
    for _ in range(ants_on_pole_count):
        ant_position_from_left = input_numbers[current_number_index]
        current_number_index += 1

        distance_to_left_end = ant_position_from_left
        # becasuee we know dist from left, dist from right will be l - dist from left
        distance_to_right_end = pole_length_cm - ant_position_from_left

        # earliest case: this ant heads to its closer end
        nearest_end_distance = distance_to_left_end
        if distance_to_right_end < nearest_end_distance:
            nearest_end_distance = distance_to_right_end

        # latest case: this ant heads to its farther end
        farthest_end_distance = distance_to_left_end
        if distance_to_right_end > farthest_end_distance:
            farthest_end_distance = distance_to_right_end
            
            
        # update dist based on the nearer dist
        if nearest_end_distance > earliest_time_when_all_fall:
            earliest_time_when_all_fall = nearest_end_distance
        # update dist based on the farthest
        if farthest_end_distance > latest_time_when_all_fall:
            latest_time_when_all_fall = farthest_end_distance

    answer_lines.append(f"{earliest_time_when_all_fall} {latest_time_when_all_fall}")

sys.stdout.write("\n".join(answer_lines))
