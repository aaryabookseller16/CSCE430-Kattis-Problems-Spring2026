# Solution: Assembly Line

## Goal
Solve the problem with interval dynamic programming. The implementation's main job is: For every substring, the DP stores the cheapest way to produce each possible component type. Splits combine left and right subassemblies.

## Key idea
The solution is built around interval dynamic programming. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: For every substring, the DP stores the cheapest way to produce each possible component type. Splits combine left and right subassemblies.

## Step-by-step algorithm
1. Create DP states for every substring or interval.
2. Set base cases for intervals of length 1.
3. Process intervals in increasing length so smaller pieces are already solved.
4. Try every split point inside the interval.
5. Combine every reachable left result with every reachable right result.
6. Update the best cost for the resulting type or state.
7. Read the answer from the state covering the whole interval.

## Example walkthrough
For aba, the algorithm compares (ab)a with a(ba).

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(L^3*K^2) per query string; memory O(L^2*K).

## Important details
This is similar to matrix-chain multiplication with multiple result types.

## Other implementations in this folder
- `efficient.md` has its own markdown explanation.
