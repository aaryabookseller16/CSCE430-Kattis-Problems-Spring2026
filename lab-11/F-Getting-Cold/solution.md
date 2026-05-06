# Solution: Getting Gold

## Goal
Solve the problem with DFS with trap-adjacency stopping rule. The implementation's main job is: The player collects gold on reachable safe cells. If the current cell is next to a trap, the search does not continue from it.

## Key idea
The solution is built around DFS with trap-adjacency stopping rule. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The player collects gold on reachable safe cells. If the current cell is next to a trap, the search does not continue from it.

## Step-by-step algorithm
1. Build the graph, grid, or neighbor relation from the input.
2. Put the starting node or starting cells into a stack or queue.
3. Mark nodes as seen when they are added.
4. Repeatedly remove one node and inspect its legal neighbors.
5. Skip walls, invalid moves, already-seen nodes, or unsafe states.
6. Update counts, distances, or component ids while visiting.
7. Use the visited set to produce the final answer.

## Example walkthrough
A gold square is counted if reachable, but if it is beside a trap, movement stops there.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(WH) time and memory.

## Important details
Walls and traps are never entered.
