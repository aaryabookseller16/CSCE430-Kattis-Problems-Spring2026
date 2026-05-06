# Problem F: Getting Gold

## Problem

You are in a small text adventure map.

The map contains:

- `P` the player's starting position
- `G` gold
- `T` a trap
- `#` a wall
- `.` normal floor

The player can walk up, down, left, and right, but not diagonally.

If the player is standing next to a trap, she can sense a draft. From such a
square, she should not move any farther, because continuing could risk walking
into a trap.

Find how much gold the player can safely collect.

## Input

The first line contains two integers:

```text
W H
```

where `W` is the width of the map and `H` is the height.

The next `H` lines each contain `W` characters describing the map.

The border of the map is always walls, and there is exactly one `P`.

## Output

Print one integer: the number of pieces of gold the player can safely get.

## Sample Input 1

```text
7 4
#######
#P.GTG#
#..TGG#
#######
```

## Sample Output 1

```text
1
```

## Sample Input 2

```text
8 6
########
#...GTG#
#..PG.G#
#...G#G#
#..TG.G#
########
```

## Sample Output 2

```text
4
```

## Notes

Use a normal flood fill from `P`.

When a reachable square is next to a trap, count gold on that square if it has
gold, but do not move from it into neighboring squares.
