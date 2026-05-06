# Solution: Natrij

## Goal
Solve the problem with time arithmetic in seconds. The implementation's main job is: The code converts current and detonation times to seconds and prints the positive wait time as HH:MM:SS.

## Key idea
The solution is built around time arithmetic in seconds. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code converts current and detonation times to seconds and prints the positive wait time as HH:MM:SS.

## Step-by-step algorithm
1. Read the starting state.
2. Process events or commands in input order.
3. Before each event, update any derived state such as time, position, counters, or current resources.
4. Apply the event rules exactly as stated.
5. Check for stopping conditions after each update.
6. Keep the output values that each command asks for.
7. Print the final result or all collected outputs.

## Example walkthrough
23:59:50 to 00:00:10 is a 20-second wait.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(1) time and memory.

## Important details
The checked-in condition only compares hours, so same-hour future times are treated as next day.
