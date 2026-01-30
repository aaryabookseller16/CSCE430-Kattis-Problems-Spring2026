import sys

# Read all input tokens (handles blank lines safely)
all_input_tokens = sys.stdin.read().split()

number_of_test_cases = int(all_input_tokens[0])
current_index = 1

results = []

for _ in range(number_of_test_cases):
    number_of_cs_students = int(all_input_tokens[current_index])
    number_of_econ_students = int(all_input_tokens[current_index + 1])
    current_index += 2

    total_students = number_of_cs_students + number_of_econ_students

    student_iqs = list(map(int, all_input_tokens[current_index:current_index + total_students]))
    current_index += total_students
    
    # fetch corresponding iqs
    cs_students_iqs = student_iqs[:number_of_cs_students]
    econ_students_iqs = student_iqs[number_of_cs_students:]

    total_cs_iq = sum(cs_students_iqs)
    total_econ_iq = sum(econ_students_iqs)

    valid_transfer_count = 0

    for cs_student_iq in cs_students_iqs:
        cs_average_increases = cs_student_iq * number_of_cs_students < total_cs_iq # check for cs iqs post transfer
        econ_average_increases = cs_student_iq * number_of_econ_students > total_econ_iq # cehck for econ iqs post transfer

        if cs_average_increases and econ_average_increases:
            valid_transfer_count += 1

    results.append(str(valid_transfer_count))

print("\n".join(results))
