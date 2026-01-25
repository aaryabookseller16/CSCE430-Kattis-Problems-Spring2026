import sys

# grab all non-empty lines
lines = [line.strip() for line in sys.stdin if line.strip() != ""]
index = 0
all_outputs = []
case_number = 1

while index < len(lines):
    command_count = int(lines[index])
    index += 1
    if command_count == 0:
        break

    # print("Loaded case", case_number, "commands:", command_count)

    # just counts, no actual stacks
    pile_one_count = 0
    pile_two_count = 0
    case_output = []

    for _ in range(command_count):
        parts = lines[index].split()
        index += 1
        command = parts[0]
        amount = int(parts[1])

        # print("Command:", command, amount)

        if command == "DROP":
            # always drop on pile 2 in this simple plan
            pile_two_count += amount
            case_output.append(f"DROP 2 {amount}")
        else:  # TAKE
            # need to send plates out in order
            plates_needed = amount
            while plates_needed > 0:
                if pile_one_count == 0 and pile_two_count > 0:
                    # move everything over so we can take from pile 1
                    case_output.append(f"MOVE 2->1 {pile_two_count}")
                    pile_one_count = pile_two_count
                    pile_two_count = 0

                take_now = min(plates_needed, pile_one_count)
                if take_now == 0:
                    break
                # take what we can right now
                case_output.append(f"TAKE 1 {take_now}")
                pile_one_count -= take_now
                plates_needed -= take_now

    all_outputs.append("\n".join(case_output))
    case_number += 1

# blank line between cases
sys.stdout.write("\n\n".join(all_outputs))
