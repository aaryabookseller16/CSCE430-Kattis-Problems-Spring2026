# Problem B - Cave Exploration

Alice is a soccer coach who occasionally brings her soccer team to explore Caveland, which can be modeled as an undirected, unweighted, connected graph, for special events such as initiation ceremonies, birthdays, and more. Caveland has `N` junctions and `M` tunnels.

Caveland is quite prone to flooding, but that does not stop Alice and her soccer team from doing what they enjoy. You are Bob, Alice's good friend. You want to keep Alice and her soccer team as safe as possible by identifying which junctions are safer than the rest.

A junction `u` is considered safe if, when any one tunnel is flooded, Alice and her soccer team can still get from junction `u` to the entrance of Caveland, which is always junction `0`, using a non-flooded path.

For the sample graph, junctions `{0, 1, 2, 3}` are considered safe. If tunnel `0-2` is flooded, for example, Alice and her soccer team can detour along the path `2 -> 3 -> 1 -> 0` to reach the entrance. However, junctions `{4, 5, 6, 7, 8}` are dangerous. If tunnel `2-8` or tunnel `3-4` is flooded, Alice and her soccer team will be trapped and unable to reach junction `0`.

## Input

The first line of input contains two integers `N` and `M` (`2 <= N <= 10000`, `1 <= M <= min(N(N - 1) / 2, 100000)`).

The next `M` lines each contain two integers `u` and `v`, the 0-based indices of two junctions connected by a tunnel (`0 <= u, v < N`, `u != v`).

No two junctions are directly connected by more than one tunnel. You are guaranteed that junction `0` can reach all other `N - 1` junctions if there is no flood.

## Output

Print one integer: the total number of junctions in Caveland that are safe for Alice and her soccer team to explore. The actual junction numbers are not needed.

## Sample Input 1

```text
9 10
0 1
0 2
1 3
2 3
2 8
3 4
4 5
4 6
5 7
6 7
```

## Sample Output 1

```text
4
```
