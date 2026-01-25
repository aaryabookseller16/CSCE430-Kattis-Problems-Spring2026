import sys

# read the number of test cases
data = sys.stdin.buffer.read().split()
idx = 0
outputs = []

# loop as long as we have tets cases
if idx < len(data):
    total_cases = int(data[idx])
    idx += 1
    # processing one test case
    for case_num in range(1, total_cases + 1):
        test_case_size = int(data[idx]) # read array size
        
        # read the 2 arrays
        idx += 1
        temp_vector_1 = list(map(int, data[idx:idx + test_case_size]))
        idx += test_case_size
        temp_vector_2 = list(map(int, data[idx:idx + test_case_size]))
        idx += test_case_size

        temp_vector_1.sort()
        temp_vector_2.sort(reverse=True)
        
        # compute scalar product
        scalar_product = 0 
        for i in range(test_case_size):
            scalar_product += temp_vector_1[i] * temp_vector_2[i]

        outputs.append(f"Case #{case_num}: {scalar_product}")

sys.stdout.write("\n".join(outputs))
