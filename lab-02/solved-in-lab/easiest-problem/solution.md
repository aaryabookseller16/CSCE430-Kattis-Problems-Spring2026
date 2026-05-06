# Solution: The Easiest Problem Is This One

## Goal
Solve the problem with brute-force digit sums. The implementation's main job is: For each N, the code tries multipliers p starting at 11 until digit_sum(N*p) equals digit_sum(N).

## Key idea
The solution is built around brute-force digit sums. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: For each N, the code tries multipliers p starting at 11 until digit_sum(N*p) equals digit_sum(N).

## Step-by-step algorithm
1. For each input N, compute the digit sum of N.
2. Try multipliers p starting at 11.
3. Compute N*p.
4. Compute the digit sum of N*p.
5. If the digit sum matches the original digit sum, print p and stop this case.
6. Otherwise increase p and continue.

## Example walkthrough
For N=3029, p=37 works because both digit sums are 14.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(p * digits(N*p)) per query; memory O(1).

## Important details
The search bound in the code is 100000.
