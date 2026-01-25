import sys

tokens = sys.stdin.buffer.read().split()
index = 0
answers = []

if index < len(tokens):
    total_test_cases = int(tokens[index])
    index += 1

    # print("Loaded test cases:", total_test_cases)

    for case_number in range(1, total_test_cases + 1):
        vector_size = int(tokens[index])
        index += 1
        
        # load in the input
        first_vector = list(map(int, tokens[index:index + vector_size]))
        index += vector_size
        second_vector = list(map(int, tokens[index:index + vector_size]))
        index += vector_size

        # print("Case", case_number, "size:", vector_size)
        # print("Vector 1:", first_vector)
        # print("Vector 2:", second_vector)

        first_vector.sort()
        second_vector.sort(reverse=True)

        minimum_scalar_product = 0
        for i in range(vector_size):
            minimum_scalar_product += first_vector[i] * second_vector[i]

        answers.append(f"Case #{case_number}: {minimum_scalar_product}")

sys.stdout.write("\n".join(answers))
