# Solution: Working at the Restaurant

## Goal
Solve the problem with two-stack simulation strategy. The implementation's main job is: All dropped plates go to pile 2. Before taking plates, pile 2 is moved to pile 1 so the oldest plates become accessible in order.

## Key idea
The solution is built around two-stack simulation strategy. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: All dropped plates go to pile 2. Before taking plates, pile 2 is moved to pile 1 so the oldest plates become accessible in order.

## Step-by-step algorithm
1. Read the starting state.
2. Process events or commands in input order.
3. Before each event, update any derived state such as time, position, counters, or current resources.
4. Apply the event rules exactly as stated.
5. Check for stopping conditions after each update.
6. Keep the output values that each command asks for.
7. Print the final result or all collected outputs.

## Example walkthrough
DROP 2 3 followed by TAKE 2 causes MOVE 2->1 3, then TAKE 1 2.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(number of commands plus emitted operations) time; memory O(output).

## Important details
A blank line separates test cases.
