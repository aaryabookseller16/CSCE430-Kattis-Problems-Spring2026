# Solution: Watering Grass

## Goal
Solve the problem with interval conversion and greedy covering. The implementation's main job is: Each sprinkler becomes the interval of strip length it can water. The greedy algorithm repeatedly takes the interval starting before the current covered point that reaches farthest.

## Key idea
The solution is built around interval conversion and greedy covering. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Each sprinkler becomes the interval of strip length it can water. The greedy algorithm repeatedly takes the interval starting before the current covered point that reaches farthest.

## Step-by-step algorithm
1. Read each sprinkler and convert it to an interval on the strip.
2. Ignore sprinklers whose radius cannot reach across half the strip width.
3. Clamp useful intervals to the strip range from 0 to l.
4. Sort intervals by left endpoint.
5. Keep the farthest point currently covered.
6. Among intervals starting at or before that point, choose the one reaching farthest right.
7. Repeat until the strip is covered or no interval can extend coverage.

## Example walkthrough
A sprinkler centered at x with enough radius covers [x-dx, x+dx] along the road.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n log n) per case for sorting; memory O(n).

## Important details
Sprinklers with radius too small to cover half the strip width are ignored.
