# Solution: Where's My Internet

## Goal
Solve the problem with DFS connectivity. The implementation's main job is: The code finds all houses reachable from house 1. Any unseen house is printed as disconnected.

## Key idea
The solution is built around DFS connectivity. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code finds all houses reachable from house 1. Any unseen house is printed as disconnected.

## Step-by-step algorithm
1. Build the graph, grid, or neighbor relation from the input.
2. Put the starting node or starting cells into a stack or queue.
3. Mark nodes as seen when they are added.
4. Repeatedly remove one node and inspect its legal neighbors.
5. Skip walls, invalid moves, already-seen nodes, or unsafe states.
6. Update counts, distances, or component ids while visiting.
7. Use the visited set to produce the final answer.

## Example walkthrough
If cables connect 1-2-3, houses 2 and 3 are reachable from the internet source.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N+M) time and memory.

## Important details
If no houses are missing, it prints Connected.
