# Solution: Planetaris

## Goal
Solve the problem with greedy sorting. The implementation's main job is: To maximize wins, beat the cheapest enemy systems first, spending c_i+1 ships for each win.

## Key idea
The solution is built around greedy sorting. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: To maximize wins, beat the cheapest enemy systems first, spending c_i+1 ships for each win.

## Step-by-step algorithm
1. Read Ali ship count and Finn ship counts.
2. Sort Finn ship counts from smallest to largest.
3. For each system in that order, compute the ships needed to win: Finn ships plus 1.
4. If Ali has enough ships, spend them and add one win.
5. If Ali cannot beat the current cheapest system, stop because all later systems are at least as expensive.
6. Print the number of wins.

## Example walkthrough
With 5 ships and enemy systems 1,2,10, win the first two by spending 2 and 3.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n log n) time and O(n) memory.

## Important details
Once the next cheapest system cannot be beaten, no later system can be beaten either.
