# Classrooms

We have `n` activities with start time `s` and end time `f`, and `k` classrooms. A classroom can hold only one activity at a time and activities that just touch (end equals start) can reuse the same room. The goal is to place as many activities as possible.

## Input
- First line: two integers `n` and `k` (`1 ≤ k ≤ n ≤ 200000`).
- Next `n` lines: two integers `s_i` and `f_i` (`1 ≤ s_i ≤ f_i ≤ 10^9`).

## Output
One integer, the maximum number of activities that can be scheduled.

## Sample
```
4 2
1 4
2 9
4 7
5 8
```
Output:
```
3
```
