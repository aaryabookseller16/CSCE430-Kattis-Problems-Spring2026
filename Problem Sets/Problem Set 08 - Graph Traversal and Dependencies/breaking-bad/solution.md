# Solution: Breaking Bad

## Goal
Solve the problem with bipartite graph coloring. The implementation's main job is: Items are graph nodes and suspicious pairs are edges. A valid shopping split exists exactly when this graph is bipartite.

## Key idea
The solution is built around bipartite graph coloring. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Items are graph nodes and suspicious pairs are edges. A valid shopping split exists exactly when this graph is bipartite.

## Step-by-step algorithm
1. Map each item name to an integer node id.
2. Build an undirected graph where suspicious pairs are edges.
3. For each uncolored component, assign the first node group 0.
4. Use BFS to color every neighbor with the opposite group.
5. If an edge ever connects two nodes with the same group, the split is impossible.
6. Otherwise collect group 0 items for Walter and group 1 items for Jesse.
7. Print the two groups.

## Example walkthrough
If acid conflicts with medicine, they get opposite colors, one for each shopper.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N+M) time and memory.

## Important details
Disconnected components can be colored independently.
