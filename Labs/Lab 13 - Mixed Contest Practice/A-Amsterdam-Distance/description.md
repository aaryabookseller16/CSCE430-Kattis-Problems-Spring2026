# Problem A: Amsterdam Distance

Amsterdam is modeled as half of a circular city. The city has straight streets
running from the center outward, and curved streets running along half-circles
around the center.

The model is split into:

- `M` equal angular slices
- `N` equal radial rings
- total city radius `R`

A street corner is written as `(x, y)`, where `x` is the radial street number and
`y` is the ring number. The center is any point with `y = 0`.

Given two corners `a` and `b`, find the shortest distance between them while
walking only along the modeled streets.

## Input

The input consists of:

- one line with two integers `M`, `N`, and a real number `R`
- one line with four integers `ax ay bx by`

Meaning:

- `1 <= M <= 100`
- `1 <= N <= 100`
- `1 <= R <= 1000`
- `0 <= ax, bx <= M`
- `0 <= ay, by <= N`

`M` is the number of angular pieces, `N` is the number of half-rings, and `R` is
the radius of the city.

## Output

Print one real number: the shortest distance needed to travel from point `a` to
point `b` using only the streets.

The result should have absolute or relative error at most `10^-6`.

## Sample Input 1

```text
6 5 2.0
1 3 4 2
```

## Sample Output 1

```text
1.65663706143592
```

## Sample Input 2

```text
9 7 3.0
1 5 9 5
```

## Sample Output 2

```text
4.28571428571429
```

## Sample Input 3

```text
10 10 1.0
2 0 6 0
```

## Sample Output 3

```text
0
```

## Idea

You can walk inward or outward along radial streets, and you can move around the
city along a circular street at some ring.

Try every possible ring where you might switch from one radial street to the
other. The cost is:

```text
radial distance to that ring + arc distance around that ring
```
