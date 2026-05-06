# Problem A

# Cow Crane

Farmer Laura has a barn in her farm, she has two cows, Monica and Lydia. Monica and Lydia love food, and they are quite lazy. For most of the day they chill out in the barn, waiting for Laura to come serve them a nice meal. Farmer Laura is always very precise about when to serve them food, Monica and Lydia know exactly when to expect food, the same time every day.

This might sound surprising to you but there's a problem. Farmer Laura needs your help. She will be replacing some planks in the floor of the barn, which means that the cows have to be moved temporarily from their favorite spots. Since the cows are infinitely lazy, they refuse to walk themselves. Farmer Laura has rented an excellent tool to resolve this issue - a cow crane, designed and crafted specifically for the cow's comfort.

We visualize the barn as a one-dimensional line. The cow crane starts at time `t = 0` at position `x = 0`, and it can move one distance unit per second. The crane can only carry one cow at a time, but it may pick up and drop off a cow as many times as necessary. Monica's current location is at `m`, and Lydia is located at `l`. Monica will have to be temporarily located at `M` and Lydia is to be located at `L`. Monica and Lydia always have their daily meal at `t_m` and `t_l`. Because they are lazy, so the cows had better be in their respective temporary locations exactly by these times. You may assume that it takes no time for the crane to pick up or drop off a cow and that the cows can't be at the same position at the same time.

## Task

Farmer Laura would like to know if she can move the cows so that both of them are in place at their temporary location no later than their daily meal occurs.

## Input

Input consists of three lines. The first line consists of two integers `m` and `l`, the current positions of the cows. The second line consists of two integers `M` and `L`, the new positions of the cows. The third line consists of two integers `t_m` and `t_l`, the time at which the two cows will be served their daily meal. It is guaranteed that `-10^5 <= m, l, M, L <= 10^5` and `1 <= t_m, t_l <= 10^5`. It is also guaranteed that both cows will actually move, i.e. `m != M` and `l != L`.

## Output

Output should consist of a single word. Print `"possible"` if it is possible to move both cows before they are served their daily meal. Otherwise, print `"impossible"`.

## Sample Input 1

```text
-1 1
-2 2
6 6
```

## Sample Output 1

```text
possible
```

## Sample Input 2

```text
-1 1
-2 3
5 5
```

## Sample Output 2

```text
impossible
```

## Sample Input 3

```text
-1 1
1 -1
3 5
```

## Sample Output 3

```text
possible
```

## Sample Input 4

```text
0 1
2 3
6 3
```

## Sample Output 4

```text
possible
```
