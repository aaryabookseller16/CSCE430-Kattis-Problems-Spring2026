def find_key_by_value(d, target):
    for k, v in d.items():
        if v == target:
            return k
    return None

import sys
value_dict = {}

# accept input until we hit "clear"
while True:
    line = sys.stdin.readline()
    if not line:  # EOF
        break

    line = line.strip()

    # clear -> forget all definitions
    if line == "clear":
        value_dict.clear()
        continue

    parts = line.split()

    # def -> add/update element in a dictionary with given value
    if parts[0] == "def":
        key = parts[1]
        value = int(parts[2])

        # if key existed, overwrite its old value
        value_dict[key] = value

    # calc -> find operator, fetch variable value from dictionary and print result
    elif parts[0] == "calc":
        temp_result = 0
        temp_str = " ".join(parts[1:]) # use the input for output but without "def"
        unknown_flag = False

        # first operand is always parts[1]
        prefix = parts[1]
        if prefix not in value_dict:
            unknown_flag = True
        else:
            temp_result = value_dict[prefix]
            
            
        #iterate for as long as we hit the = sign and store elements along the way
        i = 2
        while i < len(parts) and parts[i] != "=":
            operator = parts[i]
            suffix = parts[i + 1]

            if suffix not in value_dict: #if our result is unknown
                unknown_flag = True
                break

            prefix_int = temp_result
            suffix_int = value_dict[suffix]

            if operator == "+":
                temp_result = prefix_int + suffix_int
            elif operator == "-":
                temp_result = prefix_int - suffix_int

            i += 2

        if unknown_flag:
            key_print = "unknown"
        else:
            key_print = find_key_by_value(value_dict, temp_result)
            if key_print is None:
                key_print = "unknown"

        print(temp_str + " " + key_print)