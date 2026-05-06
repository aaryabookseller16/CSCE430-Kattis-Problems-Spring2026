# Solution: Touchdown

## Goal
Solve the problem with state simulation. The implementation's main job is: The code tracks field position, first-down line, and plays since first down while replaying the yard gains.

## Key idea
The solution is built around state simulation. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code tracks field position, first-down line, and plays since first down while replaying the yard gains.

## Step-by-step algorithm
1. Read the starting state.
2. Process events or commands in input order.
3. Before each event, update any derived state such as time, position, counters, or current resources.
4. Apply the event rules exactly as stated.
5. Check for stopping conditions after each update.
6. Keep the output values that each command asks for.
7. Print the final result or all collected outputs.

## Example walkthrough
Starting at 20, a +12 play moves to 32 and resets the first-down target to 42.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N) time and O(1) memory.

## Important details
It stops immediately on touchdown, safety, or turnover on downs.

## Other implementations in this folder
- `solution_prefix.md` has its own markdown explanation.
