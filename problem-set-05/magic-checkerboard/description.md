# Magic Checkerboard

We have an `n x m` grid. Each row must be strictly increasing left to right, and each column strictly increasing top to bottom. Additionally, diagonally adjacent cells (sharing only a corner) must have opposite parity.

Input:
- One test case per run.
- First line: `n m` with `1 <= n, m <= 2000`.
- Next `n` lines: `m` integers `0..2000`, where 0 means empty.

Goal: fill zeros with positive integers so all rules hold and the sum of all cells is minimum. If impossible, print `-1`.

Output: the minimum total sum, or `-1`.

Sample (from problem statement):
```
4 4
1 2 3 0
0 0 5 6
0 7 8 0
7 0 0 10
```
Output
```
88
```
