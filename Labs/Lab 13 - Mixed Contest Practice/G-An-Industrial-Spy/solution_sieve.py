import itertools

test_cases = int(input())

all_digit_strings = []
biggest_number = 0

for case_number in range(test_cases):
    digits = input().strip()
    all_digit_strings.append(digits)

    sorted_digits = sorted(digits, reverse=True)
    if len(sorted_digits) > 0:
        biggest_number = max(biggest_number, int("".join(sorted_digits)))

is_prime = [True] * (biggest_number + 1)
if biggest_number >= 0:
    is_prime[0] = False
if biggest_number >= 1:
    is_prime[1] = False

factor = 2
while factor * factor <= biggest_number:
    if is_prime[factor]:
        multiple = factor * factor
        while multiple <= biggest_number:
            is_prime[multiple] = False
            multiple = multiple + factor
    factor = factor + 1

for digits in all_digit_strings:
    numbers_seen = set()

    for length in range(1, len(digits) + 1):
        for arrangement in itertools.permutations(digits, length):
            numbers_seen.add(int("".join(arrangement)))

    answer = 0
    for number in numbers_seen:
        if is_prime[number]:
            answer = answer + 1

    # print("numbers", numbers_seen)
    print(answer)
