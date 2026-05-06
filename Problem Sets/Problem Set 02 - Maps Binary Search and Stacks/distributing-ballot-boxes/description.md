# Distributing Ballot Boxes

## Problem
During an election, each city must be assigned at least one ballot box. The election office has a total of `B` boxes to distribute among `N` cities. City `i` has population `a_i`, and everyone in a city must use one of that city's assigned boxes. If a city receives `k` boxes, then at least one box in that city will have `ceil(a_i / k)` people assigned to it.

Your goal is to distribute the boxes to minimize the **maximum** number of people assigned to any single box across all cities.

## Input
The input contains at most 3 test cases. For each case:
- The first line has two integers `N` and `B`:
  - `1 <= N <= 500000`
  - `N <= B <= 2000000`
- The next `N` lines each contain an integer `a_i`:
  - `1 <= a_i <= 5000000`
- A single blank line follows each test case.

The last line of the input is `-1 -1` and should not be processed.

## Output
For each test case, output a single integer: the smallest possible value of the maximum number of people assigned to one box in an optimal distribution.

## Sample Input 1
```text
2 7
200000
500000

4 6
120
2680
3400
200

-1 -1
```

## Sample Output 1
```text
100000
1700
```

## Explanation (Informal)
In the first case, giving 2 boxes to the first city and 5 to the second yields a maximum of 100000 people per box, which is optimal. In the second case, an optimal distribution achieves a maximum of 1700 people per box.
