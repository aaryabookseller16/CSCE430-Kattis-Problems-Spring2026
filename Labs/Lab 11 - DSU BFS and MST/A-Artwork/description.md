# Problem A: Artwork

## Problem

You start with a white grid of `n` rows and `m` columns.

An artwork is made by painting `q` black strokes on the grid. Each stroke is
either horizontal or vertical. A stroke starts at `(x1, y1)` and ends at
`(x2, y2)`, and every square in that straight segment becomes black.

The beauty of the artwork is the number of connected white regions. White
squares are connected only through horizontal and vertical movement, not
diagonal movement.

At the beginning, before any strokes, the whole grid is one white region.

Your task is to print the beauty after every stroke.

## Input

The first line contains three integers:

```text
n m q
```

where:

- `n` is the number of rows
- `m` is the number of columns
- `q` is the number of strokes

Constraints:

- `1 <= n, m <= 1000`
- `1 <= q <= 10000`

The next `q` lines each contain four integers:

```text
x1 y1 x2 y2
```

where:

- `1 <= x1 <= x2 <= n`
- `1 <= y1 <= y2 <= m`
- either `x1 = x2` or `y1 = y2`

So every stroke is a single row segment, a single column segment, or one square.

## Output

Print `q` lines.

The `i`th line should contain the beauty of the artwork after the `i`th stroke.

## Sample Input 1

```text
4 6 5
2 2 2 6
1 3 4 3
2 5 3 5
4 6 4 6
1 6 4 6
```

## Sample Output 1

```text
1
3
3
4
3
```

## Notes

Painting strokes forward can split a white region, which is awkward to update.

Instead, process the artwork backward:

1. First apply all strokes and count how many times each cell was painted.
2. Build connected components of the cells that are still white.
3. Remove strokes in reverse order.
4. When a cell's paint count becomes zero, it becomes white again and can be
   joined with neighboring white cells.

This turns the hard operation, splitting regions, into the easier operation,
merging regions.
