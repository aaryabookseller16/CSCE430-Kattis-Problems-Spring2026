target = "111110111100 110000100000"

knight_steps = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

seen = {}
seen[target] = 0
line = [target]
front = 0
while front < len(line):
    board = line[front]
    how_far = seen[board]
    front = front + 1
    if how_far == 10:
        continue
    blank = board.index(" ")
    row = blank // 5
    col = blank % 5
    for move in knight_steps:
        nr = row + move[0]
        nc = col + move[1]
        if nr >= 0 and nr < 5 and nc >= 0 and nc < 5:
            other = nr*5 + nc
            letters = list(board)
            letters[blank] = letters[other]
            letters[other] = " "
            new_board = "".join(letters)

            if new_board not in seen:
                seen[new_board] = how_far + 1
                line.append(new_board)
                # if len(line) % 500 == 0:
                #     print("stored", len(line))

tests = int(input())
for case_number in range(tests):
    rows = []
    for r in range(5):
        rows.append(input())
    start = "".join(rows)
#pirnt result
    if start in seen:
        print("Solvable in " + str(seen[start]) + " move(s).")
    else:
        print("Unsolvable in less than 11 move(s).")
