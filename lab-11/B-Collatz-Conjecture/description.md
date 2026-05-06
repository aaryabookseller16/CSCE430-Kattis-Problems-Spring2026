# Problem B: Collatz Conjecture

## Problem

The Collatz sequence starts with a positive integer.

Repeatedly apply these rules:

- if the number is even, divide it by `2`
- if the number is odd, replace it with `3 * number + 1`

For this problem, the sequence stops once it reaches `1`.

You are given two starting values `A` and `B`. You need to find the first number
that appears in both Collatz sequences, and how many steps each starting value
needs to reach that number.

## Input

The input contains at most `1500` test cases.

Each test case contains two integers:

```text
A B
```

where:

- `1 <= A, B <= 1000000`

The input ends with:

```text
0 0
```

This last line should not be processed.

## Output

For each test case, print exactly:

```text
A needs SA steps, B needs SB steps, they meet at C
```

where:

- `SA` is the number of steps from `A` to the meeting value
- `SB` is the number of steps from `B` to the meeting value
- `C` is the first value from `B`'s sequence that also appears in `A`'s sequence

## Sample Input 1

```text
7 8
27 30
0 0
```

## Sample Output 1

```text
7 needs 13 steps, 8 needs 0 steps, they meet at 8
27 needs 95 steps, 30 needs 2 steps, they meet at 46
```

## Notes

One easy way to solve the problem is to remember the whole sequence starting
from `A`.

For every number reached from `A`, store how many steps it took to get there.
Then generate the sequence from `B` until a number is found in that stored list.
That number is the first meeting point from `B`'s side, and the stored value
gives the step count for `A`.
