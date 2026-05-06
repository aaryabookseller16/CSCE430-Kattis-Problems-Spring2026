# Problem B: Counting Triangles

You are given a set of line segments. A triangle is formed by three segments if
you can start at the intersection of two of them, follow one segment to its
intersection with a third segment, then follow that third segment to its
intersection with the first segment.

So, for this problem, three segments define a triangle when every pair of the
three segments intersects, and the intersections are not all the same point.
The statement guarantees that no more than two segments intersect at a single
point.

## Input

The input contains up to 250 test cases.

Each test case starts with an integer `n`, the number of line segments, where
`1 <= n <= 50`.

The next `n` lines each contain four real numbers:

```text
x1 y1 x2 y2
```

These are the two endpoints of one segment.

Notes from the statement:

- segments may be parallel
- no two segments intersect at more than one point
- no more than two segments intersect at any single point
- all coordinates are in `[0, 100]`
- real values have at most 6 digits after the decimal point

The input ends with `0`.

## Output

For each test case, print the number of triangles defined by the given line
segments.

## Sample Input

```text
5
1.350 1.890 3.825 3.330
3.915 1.575 2.385 3.690
1.350 2.295 4.545 1.845
2.250 1.710 4.140 3.060
2.250 3.150 3.465 1.755
9
4.050 2.115 6.660 3.825
6.705 3.330 4.455 5.760
5.355 5.940 2.205 4.320
2.475 5.355 3.375 2.205
2.070 2.970 5.985 2.205
4.905 1.710 5.760 5.670
6.300 2.790 3.150 5.670
2.250 3.510 6.705 4.545
2.430 4.140 6.345 2.970
0
```

## Sample Output

```text
4
11
```

## Idea

Since `n` is only 50, it is fine to try every group of three segments.

For a triple, check the three pairwise segment intersections. If all three pairs
intersect, count one triangle.
