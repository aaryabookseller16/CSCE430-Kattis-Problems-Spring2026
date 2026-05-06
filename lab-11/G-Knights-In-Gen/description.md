# Problem G: Knights in Fen

## Problem

There is a `5 x 5` chessboard with black knights, white knights, and one empty
square.

Each turn, one knight may move into the empty square using a normal chess knight
move. The square that knight came from becomes the new empty square.

Given a starting board, find the minimum number of moves needed to reach the
final board:

```text
11111
01111
00 11
00001
00000
```

If it takes more than `10` moves, print that it is unsolvable in less than
`11` moves.

## Input

The first line contains an integer `N`, the number of boards.

Each board has exactly `5` lines.

Characters mean:

- `1` is a black knight
- `0` is a white knight
- space is the empty square

There is no blank line between boards.

## Output

For each board, print one of these lines:

```text
Solvable in n move(s).
```

or:

```text
Unsolvable in less than 11 move(s).
```

where `n <= 10`.

## Sample Input 1

```text
2
01011
110 1
01110
01010
00100
10110
01 11
10111
01001
00000
```

## Sample Output 1

```text
Unsolvable in less than 11 move(s).
Solvable in 7 move(s).
```

## Notes

Instead of searching from every input board separately, we can search once from
the final board.

There are only a limited number of boards reachable within `10` moves. Store the
minimum distance to each of those boards, then answer each input board with a
dictionary lookup.
