import sys
from collections import deque

tokens = sys.stdin.read().strip().split()
if not tokens:
    sys.exit()

it = iter(tokens)
rows = int(next(it))
cols = int(next(it))
board = [[int(next(it)) for _ in range(cols)] for _ in range(rows)]

BIG = 10 ** 18

# simple case: no diagonals => just strictly increasing rows/cols
if rows == 1 or cols == 1:
    max_allowed = [[BIG] * cols for _ in range(rows)]
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            cell_val = board[r][c]
            if cell_val > 0:
                max_allowed[r][c] = cell_val
            if r + 1 < rows and max_allowed[r + 1][c] - 1 < max_allowed[r][c]:
                max_allowed[r][c] = max_allowed[r + 1][c] - 1
            if c + 1 < cols and max_allowed[r][c + 1] - 1 < max_allowed[r][c]:
                max_allowed[r][c] = max_allowed[r][c + 1] - 1
            if max_allowed[r][c] <= 0:
                print(-1)
                sys.exit()
    filled = [[0] * cols for _ in range(rows)]
    total_sum = 0
    for r in range(rows):
        for c in range(cols):
            need_min = 1
            if r > 0 and filled[r - 1][c] + 1 > need_min:
                need_min = filled[r - 1][c] + 1
            if c > 0 and filled[r][c - 1] + 1 > need_min:
                need_min = filled[r][c - 1] + 1
            cell_val = board[r][c]
            if cell_val > 0:
                if cell_val < need_min or cell_val > max_allowed[r][c]:
                    print(-1)
                    sys.exit()
                filled[r][c] = cell_val
            else:
                if need_min > max_allowed[r][c]:
                    print(-1)
                    sys.exit()
                filled[r][c] = need_min
            total_sum += filled[r][c]
    print(total_sum)
    sys.exit()

# build components with diagonal edges
component_id = [[-1] * cols for _ in range(rows)]
parity_color = [[0] * cols for _ in range(rows)]
component_cells = []
component_count = 0
for r in range(rows):
    for c in range(cols):
        if component_id[r][c] != -1:
            continue
        component_id[r][c] = component_count
        parity_color[r][c] = 0
        queue = deque()
        queue.append((r, c))
        cells = []
        while queue:
            cr, cc = queue.popleft()
            cells.append((cr, cc))
            for dr, dc in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if component_id[nr][nc] == -1:
                        component_id[nr][nc] = component_count
                        parity_color[nr][nc] = parity_color[cr][cc] ^ 1
                        queue.append((nr, nc))
                    else:
                        if parity_color[nr][nc] == parity_color[cr][cc]:
                            print(-1)
                            sys.exit()
        component_cells.append(cells)
        component_count += 1

fixed_parity = [None] * component_count  # parity of color 0 (0 even, 1 odd)
for r in range(rows):
    for c in range(cols):
        cell_val = board[r][c]
        if cell_val == 0:
            continue
        value_parity = cell_val % 2
        cell_color = parity_color[r][c]
        base_parity = value_parity ^ cell_color
        comp_idx = component_id[r][c]
        if fixed_parity[comp_idx] is None:
            fixed_parity[comp_idx] = base_parity
        elif fixed_parity[comp_idx] != base_parity:
            print(-1)
            sys.exit()

free_components = [k for k in range(component_count) if fixed_parity[k] is None]

best_sum = [None]

def solve_with_parity(chosen_parity):
    max_allowed = [[BIG] * cols for _ in range(rows)]
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            cell_val = board[r][c]
            if cell_val > 0:
                max_allowed[r][c] = cell_val
            if r + 1 < rows and max_allowed[r + 1][c] - 1 < max_allowed[r][c]:
                max_allowed[r][c] = max_allowed[r + 1][c] - 1
            if c + 1 < cols and max_allowed[r][c + 1] - 1 < max_allowed[r][c]:
                max_allowed[r][c] = max_allowed[r][c + 1] - 1
            if max_allowed[r][c] <= 0:
                return None
    filled = [[0] * cols for _ in range(rows)]
    total_sum = 0
    for r in range(rows):
        for c in range(cols):
            need_min = 1
            if r > 0 and filled[r - 1][c] + 1 > need_min:
                need_min = filled[r - 1][c] + 1
            if c > 0 and filled[r][c - 1] + 1 > need_min:
                need_min = filled[r][c - 1] + 1
            desired_parity = parity_color[r][c] ^ chosen_parity[component_id[r][c]]
            cell_val = board[r][c]
            if cell_val > 0:
                if cell_val % 2 != desired_parity or cell_val < need_min or cell_val > max_allowed[r][c]:
                    return None
                filled[r][c] = cell_val
            else:
                if need_min % 2 != desired_parity:
                    need_min += 1
                if need_min > max_allowed[r][c]:
                    return None
                filled[r][c] = need_min
            total_sum += filled[r][c]
    return total_sum

def search(free_idx, parity_choice):
    if free_idx == len(free_components):
        val = solve_with_parity(parity_choice)
        if val is not None:
            if best_sum[0] is None or val < best_sum[0]:
                best_sum[0] = val
        return
    comp = free_components[free_idx]
    for pick in (0, 1):
        parity_choice[comp] = pick
        search(free_idx + 1, parity_choice)
    parity_choice[comp] = None

start_parity = fixed_parity[:]
search(0, start_parity)

if best_sum[0] is None:
    print(-1)
else:
    print(best_sum[0])
