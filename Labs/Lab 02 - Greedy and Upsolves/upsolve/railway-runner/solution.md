# Solution: Railway Runner

## Goal
Solve the problem with BFS on a 3-column grid. The implementation's main job is: Reachable rail/train cells are explored with movement rules for horizontal travel, forward movement, ladders, and jumping down.

## Key idea
The solution is built around BFS on a 3-column grid. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Reachable rail/train cells are explored with movement rules for horizontal travel, forward movement, ladders, and jumping down.

## Step-by-step algorithm
1. Build the graph, grid, or neighbor relation from the input.
2. Put the starting node or starting cells into a stack or queue.
3. Mark nodes as seen when they are added.
4. Repeatedly remove one node and inspect its legal neighbors.
5. Skip walls, invalid moves, already-seen nodes, or unsafe states.
6. Update counts, distances, or component ids while visiting.
7. Use the visited set to produce the final answer.

## Example walkthrough
From a rail cell with a ladder below, the move skips to the train roof after the ladder.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N) time and memory because there are only 3 columns.

## Important details
The answer is YES if any reachable state reaches the final row.
