# Solution: Transit Woes

## Goal
Solve the problem with timeline simulation with bus waits. The implementation's main job is: The code walks to each stop, waits until the next bus departure multiple, rides the bus, and finally walks to class.

## Key idea
The solution is built around timeline simulation with bus waits. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code walks to each stop, waits until the next bus departure multiple, rides the bus, and finally walks to class.

## Step-by-step algorithm
1. Read the starting state.
2. Process events or commands in input order.
3. Before each event, update any derived state such as time, position, counters, or current resources.
4. Apply the event rules exactly as stated.
5. Check for stopping conditions after each update.
6. Keep the output values that each command asks for.
7. Print the final result or all collected outputs.

## Example walkthrough
Arriving at time 8 for a bus every 5 minutes means waiting until time 10.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(n) memory for input arrays.

## Important details
It prints yes only when final arrival time is at most t.
