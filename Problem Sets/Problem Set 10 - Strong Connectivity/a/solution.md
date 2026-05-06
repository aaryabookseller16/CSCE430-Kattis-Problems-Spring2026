# Solution: Cantina of Babel

## Goal
Solve the problem with strongly connected components. The implementation's main job is: A directed edge means one character can be understood by another. The largest strongly connected component is the largest group that can all communicate, so everyone else leaves.

## Key idea
The solution is built around strongly connected components. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: A directed edge means one character can be understood by another. The largest strongly connected component is the largest group that can all communicate, so everyone else leaves.

## Step-by-step algorithm
1. Build both the directed graph and its reverse graph.
2. Run the first DFS pass to get vertices in finishing order.
3. Run the second pass on the reversed graph in reverse finishing order.
4. Assign each vertex to a strongly connected component.
5. Use component sizes or build the condensation graph, depending on the problem.
6. Compute the requested value from the SCC structure.
7. Print that value.

## Example walkthrough
If three people can translate in a cycle, they stay together even if communication is indirect.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N^2 + E) time because all pairs of people are checked; memory O(N^2) in the worst case.

## Important details
Kosaraju is implemented iteratively to avoid recursion limits.
