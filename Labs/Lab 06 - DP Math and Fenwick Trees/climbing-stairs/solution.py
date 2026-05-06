import sys

# read the three numbers: needed steps, desk height, office height
parts = sys.stdin.read().split()
if parts:
    need = int(parts[0])
    desk = int(parts[1])
    office = int(parts[2])

    # helper: minimal extra even steps to reach at least target from current
    def extra_even(current, target):
        if current >= target:
            return 0
        gap = target - current
        # smallest even number >= gap
        if gap % 2 == 0:
            return gap
        return gap + 1

    # Plan A: register before going to office
    pre_a = desk  # ground to desk
    extra_a = extra_even(pre_a, need)
    total_a = pre_a + extra_a + abs(desk - office) + office  # then to office and later exit to ground

    # Plan B: register after visiting office
    pre_b = office + abs(desk - office)  # ground->office->desk
    extra_b = extra_even(pre_b, need)
    total_b = pre_b + extra_b + desk  # then down to ground

    answer = total_a
    if total_b < answer:
        answer = total_b

    print(answer)
