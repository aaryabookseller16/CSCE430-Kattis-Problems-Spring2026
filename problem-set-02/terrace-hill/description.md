# Terrace Hill

## Problem
All explored mountain terraces in the Girotti hills in Charitum Montes (southern Martian hemisphere) have a peculiar feature: their sizes are approximately equal, and they all lie on a hypothetical straight line.

The flat surface of the terraces is ideal for future housing development. Their unusual configuration allows for a daring engineering project that will connect some terraces by bridges.

Due to relative geological instability in the surrounding region, the surface of any two terraces connected by a bridge must be at the same height. Obviously, a bridge between two terraces can be built only when the height of all terraces between them is less than the height of the two terraces to be connected.

The engineers want to know the maximum total length of all bridges that can be built. To simplify the introductory calculations, the following assumptions are made:
- The distance between two neighboring terraces is negligibly small (considered to be 0).
- The width of a terrace is 1 length unit.

## Input
- The first line contains an integer `N` (`1 <= N <= 3 * 10^5`), the number of terraces.
- The second line contains `N` integers `a1, a2, ..., aN` (`1 <= ai <= 10^6`), where `ai` is the height of the `i`th terrace. The heights are given in the order of terraces on the (hypothetical) line.

## Output
Print one integer: the maximum possible total length of all bridges.

## Sample Input 1
```text
5
1 2 3 3 1
```

## Sample Output 1
```text
0
```

## Sample Input 2
```text
6
5 5 5 3 2 3
```

## Sample Output 2
```text
1
```

## Sample Input 3
```text
6
2 3 2 1 2 3
```

## Sample Output 3
```text
4
```
