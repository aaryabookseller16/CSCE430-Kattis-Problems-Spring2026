# Solution: Chocolate Chip Fabrication

## Goal
Solve the problem with multi-source BFS by layers. The implementation's main job is: Initially exposed cookie cells are layer 1. BFS inward gives the exposure number for every cell, and the maximum layer is the answer.

## Key idea
The solution is built around multi-source BFS by layers. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Initially exposed cookie cells are layer 1. BFS inward gives the exposure number for every cell, and the maximum layer is the answer.

## Step-by-step algorithm
1. Build the graph, grid, or neighbor relation from the input.
2. Put the starting node or starting cells into a stack or queue.
3. Mark nodes as seen when they are added.
4. Repeatedly remove one node and inspect its legal neighbors.
5. Skip walls, invalid moves, already-seen nodes, or unsafe states.
6. Update counts, distances, or component ids while visiting.
7. Use the visited set to produce the final answer.

## Example walkthrough
A solid 3x3 block has outside cells at layer 1 and the center at layer 2.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(nm) time and memory.

## Important details
Boundary cells and cells touching empty space start the BFS.
