import itertools
import math

test_cases = int(input())
for case_number in range(test_cases):
    digits = input().strip()
    numbers_seen = set()
    for length in range(1, len(digits) + 1):
        for arrangement in itertools.permutations(digits, length):
            made_number = int("".join(arrangement))
            numbers_seen.add(made_number)
            # print("made", made_number)
    prime_count = 0
    for number in numbers_seen:
        if number < 2:
            continue
        is_prime = True
        for possible_factor in range(2, int(math.sqrt(number)) + 1):
            if number % possible_factor == 0:
                is_prime = False
                break
        if is_prime:
            prime_count = prime_count + 1
    print(prime_count)
