import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit(0)

m, l, M, L, t_m, t_l = data
possible = False

# try both choices for which cow gets finished first
for first_start, first_end, first_deadline, second_start, second_end, second_deadline in (
    (m, M, t_m, l, L, t_l),
    (l, L, t_l, m, M, t_m),
):
    # this is the plain "just do one cow and then the other" order
    first_time = abs(first_start) + abs(first_end - first_start)
    total_time = first_time + abs(second_start - first_end) + abs(second_end - second_start)
    if first_time <= first_deadline and total_time <= second_deadline:
        possible = True
        break

    # this one lets us drag the other cow somewhere useful first
    base_time = abs(second_start) + abs(first_end - first_start)
    min_first_time = base_time + abs(first_start - second_start)
    slack = first_deadline - min_first_time

    # if even the fastest setup misses the first deadline, this order is dead
    if slack < 0:
        continue

    # the temporary drop point for the second cow must stay inside this window
    low2 = 2 * min(second_start, first_start) - slack
    high2 = 2 * max(second_start, first_start) + slack

    # the total route is minimized by a median, then clamped to what the deadline allows
    middle_points = sorted((second_start, first_start, first_end, second_end))
    x2 = 2 * middle_points[1]
    if x2 < low2:
        x2 = low2
    if x2 > high2:
        x2 = high2

    # everything is doubled here so we can avoid half positions
    total_time_twice = (
        2 * base_time
        + abs(x2 - 2 * second_start)
        + abs(x2 - 2 * first_start)
        + abs(x2 - 2 * first_end)
        + abs(x2 - 2 * second_end)
    )

    if total_time_twice <= 2 * second_deadline:
        possible = True
        break

sys.stdout.write("possible\n" if possible else "impossible\n")
