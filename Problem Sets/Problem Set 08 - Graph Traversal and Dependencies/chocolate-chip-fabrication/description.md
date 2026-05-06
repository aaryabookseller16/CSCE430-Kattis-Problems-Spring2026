# Problem C - Chocolate Chip Fabrication

You are making a chocolate chip cookie using a machine that has a rectangular pan composed of unit squares. You have determined the shape of your cookie, which occupies some squares in that area. Each square of your cookie must be chocolate chipified.

To make the cookie you repeatedly perform the following two steps:

1. You place cookie dough in some unit squares.
2. You expose the cookie dough to a shallow chocolate chip solution. Any cookie dough square that does not have all four adjacent squares (up, down, left, right) filled with cookie dough becomes chocolate chipified. Any cookie dough in a square on the boundary of the pan always gets chipified.

The following example shows how to make a cookie of the shape shown on the left:

```text
(s)    (a1)   (a2)   (b1)   (b2)
-X-X-  -D-D-  -C-C-  -C-C-  -C-C-
XXXXX  -D-D-  -C-C-  DCDCD  CCCCC
XXXXX  -DDD-  -CCC-  DCCCD  CCCCC
-XXX-  --D--  --C--  -DCD-  -CCC-
--X--  -----  -----  --D--  --C--
```

First you place cookie dough in 8 squares `(a1)`. All squares become chipified after the first solution exposure `(a2)`. You place cookie dough in 8 more squares `(b1)`. The second exposure makes every square chipified and completes the cookie `(b2)`.

Your chocolate chip solution is expensive, so you want to perform the exposure as few times as possible. Given a cookie shape, determine the minimum number of chocolate chip solution exposures required to make the cookie.

## Input

The first line contains two integers `n` and `m` (`1 <= n, m <= 1000`), indicating the pan has `n` rows and `m` columns of unit squares.

Each of the next `n` lines contains a string of exactly `m` characters. Each character is either:

- `X`, representing a square occupied by your cookie
- `-`, representing an empty square

The cookie occupies at least one square. The shape may consist of multiple disconnected pieces.

## Output

Output the minimum number of chocolate chip solution exposures required to make the cookie.

## Sample Input 1

```text
5 5
-X-X-
XXXXX
XXXXX
-XXX-
--X--
```

## Sample Output 1

```text
2
```

## Sample Input 2

```text
4 5
--XXX
--X-X
X-XXX
XX---
```

## Sample Output 2

```text
1
```

## Sample Input 3

```text
5 5
XXXXX
XXXXX
XXXXX
XXXXX
XXXXX
```

## Sample Output 3

```text
3
```
