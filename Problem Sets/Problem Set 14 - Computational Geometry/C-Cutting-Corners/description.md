# Problem C: Cutting Corners

You have a convex polygon shape. To make it less pointy, you may cut off a
corner by drawing a straight line between that corner's two neighboring corners.
The cut corner is removed, and the rest of the polygon stays.

Repeat this process with the sharpest remaining corner, meaning the corner with
the smallest interior angle. Stop when the polygon has only three corners, or when
cutting off the sharpest corner would not improve the shape. In this problem,
"improve" means the smallest angle in the new polygon must be larger than the
angle of the corner that was just cut.

There will never be more than one sharpest corner that is cuttable.

## Input

The input contains up to 100 polygon descriptions.

Each polygon description starts with an integer `n`, the number of corners, where
`1 <= n <= 20`. It is followed by `n` pairs of integers giving the corner
coordinates in order around the polygon.

All coordinates are in the range `[0, 1500]`. Corners are given clockwise or
counterclockwise around the polygon. Every polygon has at least three corners,
and no two corners are coincident.

The input ends with a line containing `0`.

## Output

For each polygon, print one line describing the polygon after all possible cuts.

Use the same format as the input: first the number of remaining corners, followed
by the coordinates of those corners in the same order as the input.

## Sample Input

```text
5 0 3 4 7 7 6 10 1 4 0
5 0 0 3 5 6 7 9 8 6 0
0
```

## Sample Output

```text
4 0 3 4 7 7 6 4 0
3 0 0 3 5 6 0
```

## Idea

For each current corner, compute its interior angle using the previous and next
points. The sharpest corner is the one with the smallest angle.

Try removing that corner. If the new polygon's smallest angle is larger than the
old sharpest angle, keep the cut. Otherwise stop.
