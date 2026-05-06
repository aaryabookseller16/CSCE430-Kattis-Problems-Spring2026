# Problem H: Treehouses

## Problem

There are `n` treehouses, numbered from `1` to `n`.

Treehouse `i` is located at coordinate `(xi, yi)`.

The first `e` treehouses are close enough to the open land that people can move
between them without building any new cable. Some other treehouses may already
be connected by existing straight cables.

You may add new straight cables between treehouses. The cost of a new cable is
its Euclidean length.

Your goal is to make every treehouse reachable from the open land while adding
the smallest possible total length of new cable.

Existing land access and existing cables cost `0`.

## Input

The first line contains three integers:

```text
n e p
```

where:

- `n` is the number of treehouses
- `e` is the number of treehouses already reachable from open land
- `p` is the number of existing cables

Constraints:

- `1 <= n <= 1000`
- `1 <= e <= n`
- `0 <= p <= 1000`

The next `n` lines each contain two real numbers:

```text
x y
```

These are the coordinates of one treehouse.

The next `p` lines each contain two integers:

```text
a b
```

meaning treehouse `a` and treehouse `b` already have a cable between them.

## Output

Print the minimum total length of new cable needed.

The answer should be accepted if it has absolute or relative error at most
`0.001`.

## Sample Input 1

```text
3 1 0
0.0 0.0
2.0 0.0
1.0 2.0
```

## Sample Output 1

```text
4.236067
```

## Sample Input 2

```text
3 1 1
0.0 0.0
0.5 2.0
2.5 2.0
1 2
```

## Sample Output 2

```text
2.000000
```

## Sample Input 3

```text
3 2 0
0.0 0.0
2.0 0.0
1.0 2.0
```

## Sample Output 3

```text
2.236067
```

## Notes

This is a minimum spanning tree problem.

The first `e` treehouses can be treated as already connected with free edges.
The existing `p` cables are also free edges.

After that, choose the cheapest new cable that expands the connected group until
all treehouses are included.
