import sys

all_tokens = sys.stdin.buffer.read().split()

test_case_count = int(all_tokens[0])
token_index = 1
output_lines = []

for _ in range(test_case_count):
    # input format per case: K p/q
    data_set_id = int(all_tokens[token_index])
    token_index += 1

    fraction_token = all_tokens[token_index]
    token_index += 1

    left_side, right_side = fraction_token.split(b"/") # split numerator and denominactor
    current_numerator = int(left_side) 
    current_denominator = int(right_side)

    next_numerator = current_denominator
    next_denominator = (2 * (current_numerator // current_denominator) + 1) * current_denominator - current_numerator

    output_lines.append(f"{data_set_id} {next_numerator}/{next_denominator}")

sys.stdout.write("\n".join(output_lines))
