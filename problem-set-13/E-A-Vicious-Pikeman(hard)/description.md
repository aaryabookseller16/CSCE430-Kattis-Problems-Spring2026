# Problem E: A Vicious Pikeman (Hard)

## Problem

A contestant has `N` programming problems and a contest time limit of `T`
minutes.

Each problem has an estimated solving time. If a problem is solved, its penalty
is the minute when it is submitted. The total penalty is the sum of the
submission times of all solved problems.

The contestant wants to:

1. solve as many problems as possible within the time limit
2. among all ways to solve that many problems, get the smallest total penalty

The best strategy is to solve shorter problems first.

The first problem takes `t0` minutes. The rest of the problem times are generated
with:

```text
t_i = ((A * t_(i-1) + B) mod C) + 1
```

for `i = 1` through `N - 1`.

This is the hard version, so `N` may be too large to store every generated
problem time.

## Input

Input contains two lines.

The first line contains:

```text
N T
```

where:

- `N` is the number of problems
- `T` is the contest length in minutes

The second line contains:

```text
A B C t0
```

Constraints:

- `1 <= N <= 10^9`
- `1 <= T <= 10^18`
- `1 <= A, B, C <= 10^6`
- `1 <= t0 <= C`

## Output

Print two integers:

```text
solved penalty
```

where:

- `solved` is the maximum number of problems that can be solved
- `penalty` is the minimum total penalty for that many solved problems

Print the penalty modulo:

```text
1000000007
```

## Sample Input 1

```text
1 3
2 2 2 1
```

## Sample Output 1

```text
1 1
```

## Sample Input 2

```text
2 10
2 2 2 2
```

## Sample Output 2

```text
2 4
```

## Notes

The generated solving times are always between `1` and `C`.

Since `C <= 10^6`, the sequence must eventually repeat. Once a repeated value is
seen, the rest of the sequence is a cycle. This lets us count how many times each
solving time appears without generating all `N` values.

After that, process times from `1` to `C`. If there are many problems with the
same solving time, take as many as fit and add their penalty using an arithmetic
series.
