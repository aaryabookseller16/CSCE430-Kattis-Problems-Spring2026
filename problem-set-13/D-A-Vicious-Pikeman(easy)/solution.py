numbers_to_answer = []

while True:
    h_number = int(input())
    if h_number == 0:
        break
    numbers_to_answer.append(h_number)

if len(numbers_to_answer) > 0:
    biggest_number = max(numbers_to_answer)

    is_h_prime = [False] * (biggest_number + 1)
    for possible_h_number in range(5, biggest_number + 1, 4):
        is_h_prime[possible_h_number] = True

    # cross off H-composites
    for first_factor in range(5, biggest_number + 1, 4):
        if is_h_prime[first_factor]:
            second_factor = first_factor
            while first_factor * second_factor <= biggest_number:
                is_h_prime[first_factor * second_factor] = False
                second_factor = second_factor + 4

    h_primes = []
    for possible_h_number in range(5, biggest_number + 1, 4):
        if is_h_prime[possible_h_number]:
            h_primes.append(possible_h_number)

    is_h_semiprime = [False] * (biggest_number + 1)

    for first_place in range(len(h_primes)):
        first_prime = h_primes[first_place]
        if first_prime * first_prime > biggest_number:
            break

        second_place = first_place
        while second_place < len(h_primes):
            second_prime = h_primes[second_place]
            product = first_prime * second_prime

            if product > biggest_number:
                break

            is_h_semiprime[product] = True
            second_place = second_place + 1

            # print("made semi", product)

    semiprime_count_up_to = [0] * (biggest_number + 1)
    running_count = 0
    for value in range(biggest_number + 1):
        if is_h_semiprime[value]:
            running_count = running_count + 1
        semiprime_count_up_to[value] = running_count

    for h_number in numbers_to_answer:
        print(h_number, semiprime_count_up_to[h_number])
