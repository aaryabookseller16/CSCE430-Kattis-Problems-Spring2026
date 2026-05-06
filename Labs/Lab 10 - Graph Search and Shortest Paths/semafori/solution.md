# Solution: Semafori

## Goal
Solve the problem with timeline simulation. The implementation's main job is: The truck drives to each light, waits if arrival time falls in the red part of the cycle, then continues.

## Key idea
The solution is built around timeline simulation. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The truck drives to each light, waits if arrival time falls in the red part of the cycle, then continues.

## Step-by-step algorithm
1. Read the starting state.
2. Process events or commands in input order.
3. Before each event, update any derived state such as time, position, counters, or current resources.
4. Apply the event rules exactly as stated.
5. Check for stopping conditions after each update.
6. Keep the output values that each command asks for.
7. Print the final result or all collected outputs.

## Example walkthrough
Arriving at time 7 for a 5-red/5-green light means it is green and no wait is needed.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N) time and O(1) memory.

## Important details
Traffic lights are already ordered by distance.
