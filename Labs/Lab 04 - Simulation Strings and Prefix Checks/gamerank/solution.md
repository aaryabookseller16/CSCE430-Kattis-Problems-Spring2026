# Solution: Game Rank

## Goal
Solve the problem with state simulation. The implementation's main job is: The solution tracks current rank, stars, and win streak, applying bonus stars and loss penalties after each game.

## Key idea
The solution is built around state simulation. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The solution tracks current rank, stars, and win streak, applying bonus stars and loss penalties after each game.

## Step-by-step algorithm
1. Read the starting state.
2. Process events or commands in input order.
3. Before each event, update any derived state such as time, position, counters, or current resources.
4. Apply the event rules exactly as stated.
5. Check for stopping conditions after each update.
6. Keep the output values that each command asks for.
7. Print the final result or all collected outputs.

## Example walkthrough
Three wins in a row at rank 10 give a bonus star on the third win.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(number of games) time and O(1) memory.

## Important details
The code prints Legend when rank 1 is passed.
