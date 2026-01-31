
import sys
from collections import deque

DEBUG = False


def debug(*args):
    if DEBUG:
        print("[debug]", *args, file=sys.stderr)


def can_finish(grid):
    n = len(grid)
    if n == 0:
        return False

    # visited[r][c] means we already reached row r, col c
    visited = [[False] * 3 for _ in range(n)]
    q = deque()

    # start on any rail in the first row
    for c in range(3):
        if grid[0][c] == '.':
            visited[0][c] = True
            q.append((0, c))
            debug("start at", 0, c)

    while q:
        r, c = q.popleft()
        cell = grid[r][c]
        debug("pop", r, c, cell)

        if r == n - 1:
            return True

        # move left/right on same type (rail or train)
        if cell in ('.', '*'):
            for dc in (-1, 1):
                nc = c + dc
                if 0 <= nc < 3 and not visited[r][nc] and grid[r][nc] == cell:
                    visited[r][nc] = True
                    q.append((r, nc))
                    debug("horiz to", r, nc)

        # move forward (down)
        if cell == '.':
            nr = r + 1
            if nr < n:
                below = grid[nr][c]
                if below == '.':
                    if not visited[nr][c]:
                        visited[nr][c] = True
                        q.append((nr, c))
                        debug("down on rail to", nr, c)
                elif below == '/':
                    # ladder: must go forward to the train roof
                    nr2 = r + 2
                    if nr2 < n and grid[nr2][c] == '*' and not visited[nr2][c]:
                        visited[nr2][c] = True
                        q.append((nr2, c))
                        debug("ladder up to train", nr2, c)
                # if below is '*', can't climb directly without a ladder
        elif cell == '*':
            nr = r + 1
            if nr < n:
                below = grid[nr][c]
                if below == '.' or below == '*':
                    if not visited[nr][c]:
                        visited[nr][c] = True
                        q.append((nr, c))
                        debug("down from train to", nr, c)
                # if below is '/', ignore (shouldn't happen with valid input)

    return False


def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    grid = tokens[1:1 + n]

    # if input is weird, just trim / pad safely
    if len(grid) != n:
        debug("warning: expected", n, "rows, got", len(grid))
        grid = grid[:n]

    ans = "YES" if can_finish(grid) else "NO"
    print(ans)


if __name__ == "__main__":
    main()
