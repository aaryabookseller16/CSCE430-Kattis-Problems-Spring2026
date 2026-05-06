# Solution: Adding Words

## Goal
Solve the problem with dictionary simulation. The implementation's main job is: Definitions map words to numbers. Calculations evaluate the expression, then search for a word with the resulting value.

## Key idea
The solution is built around dictionary simulation. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Definitions map words to numbers. Calculations evaluate the expression, then search for a word with the resulting value.

## Step-by-step algorithm
1. Read the starting state.
2. Process events or commands in input order.
3. Before each event, update any derived state such as time, position, counters, or current resources.
4. Apply the event rules exactly as stated.
5. Check for stopping conditions after each update.
6. Keep the output values that each command asks for.
7. Print the final result or all collected outputs.

## Example walkthrough
If foo=3 and bar=7, calc foo + bar = looks for a word whose value is 10.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(L + V) per calc, where L is expression length and V is number of defined words; memory O(V).

## Important details
The reverse lookup is done by scanning the dictionary.
