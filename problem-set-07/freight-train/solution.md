# Solution: Freight Train

## Goal
Solve the problem with binary search with greedy feasibility. The implementation's main job is: The answer is the smallest maximum Luxembourg-bound train length. For a guessed length, the code greedily counts how many chunks are needed.

## Key idea
The solution is built around binary search with greedy feasibility. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The answer is the smallest maximum Luxembourg-bound train length. For a guessed length, the code greedily counts how many chunks are needed.

## Step-by-step algorithm
1. Choose the answer value to binary search.
2. Set lower and upper bounds that definitely contain the answer.
3. Write a feasibility check for a guessed value.
4. Try the middle value.
5. If the guess works, keep the lower half; otherwise keep the upper half.
6. Repeat until the bounds meet.
7. Print the final bound as the smallest feasible answer.

## Example walkthrough
If the next freight wagon is too far from the current front, an empty chunk is sent away first.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(W log N) per test case; memory O(W).

## Important details
Binary search works because if length X is feasible, any larger length is also feasible.
