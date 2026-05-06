# Solution: Path Tracing

## Goal
Solve the problem with grid simulation and bounding box output. The implementation's main job is: The path starts in the middle of a large array. Moves mark visited cells, track min/max row/column, then print the smallest rectangle with a border.

## Key idea
The solution is built around grid simulation and bounding box output. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The path starts in the middle of a large array. Moves mark visited cells, track min/max row/column, then print the smallest rectangle with a border.

## Step-by-step algorithm
1. Read the starting state.
2. Process events or commands in input order.
3. Before each event, update any derived state such as time, position, counters, or current resources.
4. Apply the event rules exactly as stated.
5. Check for stopping conditions after each update.
6. Keep the output values that each command asks for.
7. Print the final result or all collected outputs.

## Example walkthrough
Moves down, down, left mark three path cells and then crop to just those rows and columns.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(M + A), where M is number of moves and A is printed area; memory uses a fixed 1000x1000 array.

## Important details
The code uses NumPy for the grid.
