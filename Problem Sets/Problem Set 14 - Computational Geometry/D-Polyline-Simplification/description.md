# Problem D: Polyline Simplification

A polyline is made from `n` connected line segments, described by `n + 1`
points `p0, p1, ..., pn`.

To simplify the polyline, you repeatedly remove one interior point `pi`, where
`1 <= i <= n - 1`. Removing `pi` replaces the two segments `p(i-1)-pi` and
`pi-p(i+1)` with one segment `p(i-1)-p(i+1)`.

At each step, choose the point whose neighboring triangle has the smallest area:

```text
p(i-1), pi, p(i+1)
```

If there is a tie, remove the point with the lowest index. Continue until the
polyline has exactly `m` segments.

## Input

The first line contains two integers `n` and `m`.

- `n` is the original number of line segments
- `m` is the target number of line segments after simplification

Constraints:

- `2 <= n <= 200000`
- `1 <= m < n`

The next `n + 1` lines each contain two integers `x` and `y`, the coordinates of
the points of the polyline in order.

Coordinates are between `-5000` and `5000`, inclusive.

The statement guarantees that all `x` values are strictly increasing:

```text
x_i < x_(i+1)
```

for all valid `i`.

## Output

Print `n - m` lines. The `k`-th line should contain the original index of the
point removed in the `k`-th simplification step.

## Sample Input

```text
10 7
0 0
1 10
2 20
25 17
32 19
33 5
40 10
50 13
65 27
75 22
85 17
```

## Sample Output

```text
1
9
6
```

## Idea

The triangle area for an active point only changes when one of its current
neighbors is removed.

Keep arrays for the previous and next active point, and keep all current triangle
areas in a heap. When a point is removed, update only its two neighbors and push
their new areas into the heap.
