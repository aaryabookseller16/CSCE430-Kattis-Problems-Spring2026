numbers_to_answer = []

while True:
    h_number = int(input())
    if h_number == 0:
        break
    numbers_to_answer.append(h_number)
if len(numbers_to_answer) > 0:
    biggest_number = max(numbers_to_answer)
    h_numbers = []
    for value in range(5, biggest_number + 1, 4):
        h_numbers.append(value)
    h_primes = []
    for possible_prime in h_numbers:
        can_be_broken = False
        for first_factor in h_numbers:
            if first_factor * first_factor > possible_prime:
                break
            if possible_prime % first_factor == 0:
                second_factor = possible_prime // first_factor
                if second_factor % 4 == 1:
                    can_be_broken = True
                    break
        if can_be_broken == False:
            h_primes.append(possible_prime)
        # print("checked", possible_prime, can_be_broken)
    is_h_semiprime = [False] * (biggest_number + 1)

    for first_place in range(len(h_primes)):
        first_prime = h_primes[first_place]
        if first_prime * first_prime > biggest_number:
            break
        for second_place in range(first_place, len(h_primes)):
            second_prime = h_primes[second_place]
            product = first_prime * second_prime
            if product > biggest_number:
                break
            is_h_semiprime[product] = True
    running_count = 0
    semiprime_count_up_to = [0] * (biggest_number + 1)
    for value in range(biggest_number + 1):
        if is_h_semiprime[value]:
            running_count = running_count + 1
        semiprime_count_up_to[value] = running_count

    for h_number in numbers_to_answer:
        print(h_number, semiprime_count_up_to[h_number])
