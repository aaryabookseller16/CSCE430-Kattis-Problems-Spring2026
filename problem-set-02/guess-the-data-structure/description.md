# I Can Guess the Data Structure!

## Problem
There is a bag-like data structure that supports two operations:

1. `1 x`: put the element `x` into the bag.
2. `2 x`: take out an element from the bag, and it must be `x`.

Given the sequence of operations and the values that were returned, you must decide which data structure(s) it could be:
- stack (LIFO)
- queue (FIFO)
- priority queue (always removes the largest element)

If exactly one fits, print its name. If more than one fits, print `not sure`. If none fit, print `impossible`.

## Input
There are several test cases. Each test case begins with a single integer `n` (`1 <= n <= 1000`), the number of operations. The next `n` lines each contain two integers:
- the operation code `1` or `2`
- the value `x` (`x` is positive and `x <= 100`)

Input ends at EOF. The input size does not exceed 1MB.

## Output
For each test case, output one of the following:
- `stack`
- `queue`
- `priority queue`
- `impossible`
- `not sure`

## Sample Input 1
```text
6
1 1
1 2
1 3
2 1
2 2
2 3
6
1 1
1 2
1 3
2 3
2 2
2 1
2
1 1
2 2
4
1 2
1 1
2 1
2 2
7
1 2
1 5
1 1
1 3
2 5
2 3
2 2
1
2 1
```

## Sample Output 1
```text
queue
not sure
impossible
stack
priority queue
impossible
```
