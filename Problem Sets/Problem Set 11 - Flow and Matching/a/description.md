# Avoiding the Apocalypse

You and the rest of your team are stuck in a town during the zombie apocalypse of 2020. You may all have been infected, so you need to get to one of the medical facilities before it is too late. Because you are scientists, you quickly realize that it is safer to sneak past the zombies than to fight them directly.

Zombies are everywhere, so some streets might take more time to cross than others. It is also possible that some streets are much easier to cross in one direction than in the other, so roads should be treated as directed. Since it is easier to move unnoticed in smaller groups, your team may split up along different routes.

How many of you can get to a medical facility in time?

## Input

The first line contains the number of test cases, at most `100`.

For each test case:

- One line with a single integer `n` (`1 <= n <= 1000`), the number of locations in the town.
- One line with three space-separated integers `i`, `g`, and `s` (`1 <= i <= n`, `1 <= g <= 100`, `1 <= s <= 100`), where:
  - `i` is the starting location of your group,
  - `g` is the number of people in the group,
  - `s` is the number of time steps available to reach a medical facility.
- One line with a single integer `m` (`1 <= m <= n`), the number of medical facilities.
- `m` lines, each with a single integer `x` (`1 <= x <= n`), giving the location of a medical facility.
- One line with a single integer `r` (`0 <= r <= 1000`), the number of roads.
- `r` lines, each with four space-separated integers `a`, `b`, `p`, and `t` (`1 <= a, b <= n`, `a != b`, `1 <= p <= 100`, `1 <= t <= 100`), describing a road from `a` to `b` that:
  - takes `t` time steps to traverse,
  - allows at most `p` people to enter the road during each time step.

There are at most two roads between any pair of locations, one in each direction.

Locations are safe, so people may wait there for any amount of time, and there is no limit on how many people can stay at a location at once.

## Output

For each test case, print a single integer: the largest number of people who can reach some medical facility within `s` time steps.

## Sample Input

```text
2
4
3 8 5
2
2
4
5
1 2 1 3
3 2 1 4
3 1 2 1
1 4 1 3
3 4 1 3
4
3 10 5
2
2
4
5
1 2 1 3
3 2 1 4
3 1 2 1
1 4 1 3
3 4 1 3
```

## Sample Output

```text
8
9
```
