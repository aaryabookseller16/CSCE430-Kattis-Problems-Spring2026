# Solution: Texas Summers

## Goal
Solve the problem with dense Dijkstra shortest path. The implementation's main job is: Shade spots, dorm, and class are graph nodes. Edge cost is squared distance, representing sweat for one sunny segment.

## Key idea
The solution is built around dense Dijkstra shortest path. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Shade spots, dorm, and class are graph nodes. Edge cost is squared distance, representing sweat for one sunny segment.

## Step-by-step algorithm
1. Treat each point or state as a graph node.
2. Initialize the start distance to 0 and all others to infinity.
3. Repeatedly choose the unused node with smallest known distance.
4. Relax every possible outgoing edge from that node.
5. Store parents when the actual path must be printed.
6. Stop when the target is finalized.
7. Reconstruct and print the path or answer.

## Example walkthrough
Stopping at shade can split one long squared distance into two smaller squared distances.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n^2) time and O(n) memory.

## Important details
The output is the sequence of shade indices on the shortest path, or - if none.
