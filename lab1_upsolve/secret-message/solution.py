import sys
import math

# read everything, nothing fancy
lines = [line.rstrip("\n") for line in sys.stdin if line.strip() != ""]

if not lines:
    sys.exit(0)

total = int(lines[0])
pos = 1
out_lines = []

# print("total", total)

for _ in range(total):
    if pos >= len(lines):
        break
    message = lines[pos]
    pos += 1

    # print("msg", message)

    length = len(message)
    side = int(math.ceil(math.sqrt(length)))
    size = side * side
    padded = message + ("*" * (size - length))

    # print("len", length, "side", side, "size", size)
    # print("pad", padded)

    grid = []
    for r in range(side):
        row = list(padded[r * side:(r + 1) * side])
        grid.append(row)

    # print("grid", grid)

    rotated = []
    for r in range(side):
        rotated.append([""] * side)

    # spin it 90 deg
    for r in range(side):
        for c in range(side):
            rotated[c][side - 1 - r] = grid[r][c]

    # print("rot", rotated)

    secret = []
    for r in range(side):
        for c in range(side):
            ch = rotated[r][c]
            if ch != "*":
                secret.append(ch)

    # stick it together
    out_lines.append("".join(secret))

sys.stdout.write("\n".join(out_lines))
