# Problem E - Lost Map

Somewhere in a mountainous region of the world is a collection of `n` villages. Connecting these villages to one another is a series of roads, always running directly between two villages and allowing travel in both directions. Due to the treacherous landscape, building these roads is expensive, so a minimum number of roads have been constructed such that each village can reach every other village via a sequence of roads.

Trade between these villages is very important, since not every village has access to the same supply of natural resources. Many villages produce the same resource, however, so it is useful for villages to know their relative distance to other villages so that they can choose trading partners to minimize overall trading costs. Note that the distance between two villages `a` and `b` is the sum of the lengths of the individual roads on the shortest path that connects `a` and `b`.

A project has been underway to compute the distance between every pair of villages. This information has been incorporated in a table, along with a map that shows the layout of villages and roads that run between them. You have been assigned the task of distributing the table and map to all the villages for the benefit of the regional economy.

Unfortunately, not long after you were given this task, a gust of wind blew the map right out of your hand and into the countryside. Despite your best efforts of searching for it, you have been unable to locate it. You know that you could visit all the villages to reconstruct the map and then start distributing the map and table, but this will take twice as long as the original task and the villages will be very displeased with you. You wonder, maybe it's possible to reconstruct the map given only the table?

## Input

The first line of input contains the integer `n` (`2 <= n <= 2500`), the number of villages in this region.

The next `n` lines each contain `n` integers, where the `j`th integer on the `i`th line is the distance from village `i` to village `j`. These distances are nonnegative, are less than `10^7`, and satisfy `d(i, j) = d(j, i)`.

## Output

Output `n - 1` lines, each with two integers `u` and `v`, indicating that there is a road connecting villages `u` and `v` in this region. Assume the villages are numbered from `1` to `n`. Any solution that outputs the original set of roads will be accepted.

## Sample Input 1

```text
4
0 1 1 2
1 0 2 3
1 2 0 3
2 3 3 0
```

## Sample Output 1

```text
1 2
1 3
1 4
```

## Sample Input 2

```text
7
0 2 9 1 4 3 3
2 0 11 1 6 3 3
9 11 0 10 5 12 12
1 1 10 0 5 2 2
4 6 5 5 0 7 7
3 3 12 2 7 0 4
3 3 12 2 7 4 0
```

## Sample Output 2

```text
1 4
1 5
2 4
3 5
4 6
4 7
```
