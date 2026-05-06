# Solution: Knights in Fen

## Goal
Solve the problem with precomputed BFS from the target board. The implementation's main job is: All boards within 10 moves of the target are generated once. Each test board is then a dictionary lookup.

## Key idea
The solution is built around precomputed BFS from the target board. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: All boards within 10 moves of the target are generated once. Each test board is then a dictionary lookup.

## Step-by-step algorithm
1. Build the graph, grid, or neighbor relation from the input.
2. Put the starting node or starting cells into a stack or queue.
3. Mark nodes as seen when they are added.
4. Repeatedly remove one node and inspect its legal neighbors.
5. Skip walls, invalid moves, already-seen nodes, or unsafe states.
6. Update counts, distances, or component ids while visiting.
7. Use the visited set to produce the final answer.

## Example walkthrough
If the blank can swap with a knight by a legal knight move, that neighbor board is one BFS edge.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Precomputation is bounded by all states within depth 10; each query is O(1) lookup after reading 25 cells.

## Important details
Starting from the target makes many test cases cheap.
