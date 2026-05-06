# Solution: Collatz Conjecture

## Goal
Solve the problem with hash map of one sequence. The implementation's main job is: The first sequence is stored with step counts. The second sequence is generated until it reaches a seen value.

## Key idea
The solution is built around hash map of one sequence. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The first sequence is stored with step counts. The second sequence is generated until it reaches a seen value.

## Step-by-step algorithm
1. Generate the Collatz sequence from A.
2. Store each value with the number of steps needed to reach it.
3. Generate the Collatz sequence from B.
4. Stop when B reaches a value that was already seen from A.
5. Look up A steps from the dictionary and keep B steps from the second generation.
6. Print both step counts and the meeting value.

## Example walkthrough
If A reaches 40 in 3 steps and B reaches 40 in 5 steps, that is the meeting report.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(length of both sequences until meeting); memory O(length of A sequence).

## Important details
The input ends at 0 0.
