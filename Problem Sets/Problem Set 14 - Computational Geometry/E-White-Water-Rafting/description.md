# Problem E: White Water Rafting

A theme park ride is shaped like a closed track between two polygons. One
polygon is the inner boundary and the other polygon is the outer boundary. The
outer polygon fully contains the inner polygon, and the two polygons do not
touch or intersect.

The rafts must be circular. To fit through the whole ride, the diameter of a
raft cannot be larger than the narrowest gap between the two polygon borders.

Find the maximum possible radius of a raft.

## Input

The first line contains an integer `T`, the number of test cases.

For each test case:

- One line contains `ni`, the number of points of the inner polygon.
- The next `ni` lines contain integer coordinates for the inner polygon points,
  in order.
- One line contains `no`, the number of points of the outer polygon.
- The next `no` lines contain integer coordinates for the outer polygon points,
  in order.

The points may be clockwise or counterclockwise.

Constraints:

- `T <= 100`
- `3 <= ni <= 100`
- `3 <= no <= 100`
- Coordinates have absolute value at most `1000`
- Polygon edges do not touch or intersect
- The outer polygon encloses the inner polygon

## Output

For each test case, print the maximum radius of the raft. Answers are accepted
with absolute or relative error at most `10^-6`.

## Sample Input

```text
2
4
-5 -5
5 -5
5 5
-5 5
4
-10 -10
-10 10
10 10
10 -10
3
0 0
1 0
1 1
5
3 -3
3 3
-4 2
-1 -1
-2 -2
```

## Sample Output

```text
2.5
0.70710678
```

## Idea

The largest raft radius is half of the smallest distance between the inner
polygon boundary and the outer polygon boundary.

That smallest distance can be found by checking distances from every vertex of
one polygon to every edge of the other polygon, in both directions.
