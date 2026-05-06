# Problem A: Board Wrapping

A sawmill packages rectangular boards for drying by putting them in a very thin
frame. From above, each board is a rectangle that may be rotated. The frame
must follow the convex hull of all board corners.

For each mould, find what percentage of the frame's interior area is actually
covered by boards.

## Input

The first line contains an integer `N`, the number of test cases.

Each test case starts with an integer `n`, the number of boards in the mould.

The next `n` lines each contain five values:

```text
x y w h v
```

where:

- `(x, y)` is the center of the board
- `w` is the board width
- `h` is the board height
- `v` is the angle in degrees between the board's height axis and the y-axis,
  measured clockwise

If `v = 0`, the board has width `w` along the x-axis and height `h` along the
y-axis.

The boards do not intersect.

Constraints from the statement:

- `N <= 50`
- `1 <= n <= 600`
- `0 <= x, y, w, h <= 10000`
- `-90 < v <= 90`

## Output

For each test case, print one line containing the percentage of the mould area
covered by boards. The answer must have one digit after the decimal point and
then a space and percent sign.

## Sample Input

```text
1
4
4 7.5 6 3 0
8 11.5 6 3 0
9.5 6 6 3 90
4.5 3 4.4721 2.2361 26.565
```

## Sample Output

```text
64.3 %
```

## Idea

Add the area of all boards directly. Then compute all four rotated corners for
each board and find the convex hull of those points. The mould area is the area
of that hull.

The answer is:

```text
100 * board_area / hull_area
```
