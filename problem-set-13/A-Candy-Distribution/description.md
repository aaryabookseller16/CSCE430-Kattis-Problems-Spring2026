# Problem A: Candy Distribution

## Problem

You are planning a party for `K` kids. A fair candy distribution means every kid
gets the same positive number `X` of candies, but you also want exactly one spare
candy left over.

So the total number of candies you buy must look like:

```text
K * X + 1
```

Candy is sold in bags, and every bag contains exactly `C` candies. You need to
choose how many bags to buy so that the total number of candies from those bags
matches the rule above.

In other words, find a positive number of bags `Y` such that:

```text
C * Y = K * X + 1
```

for some positive integer `X`.

You are not allowed to buy more than `10^9` bags.

## Input

The first line contains an integer `t`, the number of test cases.

Each test case contains two integers:

```text
K C
```

where:

- `K` is the number of kids
- `C` is the number of candies in one bag

Constraints:

- `0 < t < 100`
- `1 <= K, C <= 10^9`

## Output

For each test case, print one line.

If there is a valid number of bags, print that number. If there is more than one
answer, any valid answer is fine.

If there is no answer using at most `10^9` bags, print:

```text
IMPOSSIBLE
```

## Sample Input 1

```text
5
10 5
10 7
1337 23
123454321 42
999999937 142857133
```

## Sample Output 1

```text
IMPOSSIBLE
3
872
14696943
166666655
```

## Notes

The equation

```text
C * Y = K * X + 1
```

means:

```text
C * Y == 1 (mod K)
```

So `Y` is the modular inverse of `C` modulo `K`, if that inverse exists.

If `C` and `K` have a common divisor greater than `1`, then the inverse does not
exist and the answer is impossible.

There is one special case when `C = 1`. Then the equation becomes:

```text
Y = K * X + 1
```

Since `X` must be positive, the smallest possible number of bags is `K + 1`.
