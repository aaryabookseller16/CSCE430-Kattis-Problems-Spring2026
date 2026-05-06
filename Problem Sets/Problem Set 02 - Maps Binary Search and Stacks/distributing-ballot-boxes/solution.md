# Solution: Distributing Ballot Boxes

## Goal
Solve the problem with binary search on maximum load. The implementation's main job is: For a proposed maximum people per box, the helper counts how many boxes are needed. Binary search finds the smallest feasible maximum.

## Key idea
The solution is built around binary search on maximum load. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: For a proposed maximum people per box, the helper counts how many boxes are needed. Binary search finds the smallest feasible maximum.

## Step-by-step algorithm
1. Choose the answer value to binary search.
2. Set lower and upper bounds that definitely contain the answer.
3. Write a feasibility check for a guessed value.
4. Try the middle value.
5. If the guess works, keep the lower half; otherwise keep the upper half.
6. Repeat until the bounds meet.
7. Print the final bound as the smallest feasible answer.

## Example walkthrough
A city with 10 people and max 4 needs ceil(10/4)=3 boxes.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N log max_population) per case; memory O(N).

## Important details
Feasibility is monotonic: larger allowed max never needs more boxes.
