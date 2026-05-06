import sys

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit(0)

# read number of sides and number of rolls allowed
number_of_sides = int(data[0])
max_rolls = int(data[1])

# expected value if we only roll once
current_expected_value = (number_of_sides + 1) / 2.0

# for each extra roll, update using E[max(X, previous_expected)]
for rolls_left in range(2, max_rolls + 1):

    threshold = current_expected_value  # if roll is below this, we reroll

    # if threshold is <= 1, stopping always gives the die value
    if threshold <= 1.0:
        current_expected_value = (number_of_sides + 1) / 2.0
        continue

    # if threshold is >= max face value, always reroll value is worse
    if threshold >= number_of_sides:
        continue

    # floor of threshold to split the expectation
    floor_value = int(threshold)

    # how many outcomes are <= floor_value
    count_low = floor_value

    # how many outcomes are > floor_value
    count_high = number_of_sides - floor_value

    # sum of integers from floor_value+1 to number_of_sides
    sum_high_values = (floor_value + 1 + number_of_sides) * count_high / 2.0

    # compute E[max(X, threshold)]
    current_expected_value = (
        count_low * threshold + sum_high_values
    ) / number_of_sides

# print with enough precision
sys.stdout.write(f"{current_expected_value:.10f}\n")