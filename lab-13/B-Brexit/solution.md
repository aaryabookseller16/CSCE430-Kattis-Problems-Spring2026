# Solution: Brexit

## Goal
Solve the problem with queue simulation on graph thresholds. The implementation's main job is: When a country leaves, each neighbor loses one partner. A neighbor leaves once lost partners reach at least half of its original degree.

## Key idea
The solution is built around queue simulation on graph thresholds. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: When a country leaves, each neighbor loses one partner. A neighbor leaves once lost partners reach at least half of its original degree.

## Step-by-step algorithm
1. Read the starting state.
2. Process events or commands in input order.
3. Before each event, update any derived state such as time, position, counters, or current resources.
4. Apply the event rules exactly as stated.
5. Check for stopping conditions after each update.
6. Keep the output values that each command asks for.
7. Print the final result or all collected outputs.

## Example walkthrough
If a country originally had 4 partners, losing 2 of them makes it leave.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(C+P) time and memory.

## Important details
The queue is a BFS-style cascade of departures.

## Other implementations in this folder
- `solution_slow.md` has its own markdown explanation.
