# Solution: Climbing Stairs

## Goal
Solve the problem with small case analysis with parity adjustment. The implementation's main job is: The code compares two visit orders and adds the smallest even number of extra steps needed to reach the required step count.

## Key idea
The solution is built around small case analysis with parity adjustment. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code compares two visit orders and adds the smallest even number of extra steps needed to reach the required step count.

## Step-by-step algorithm
1. Compute the total route if registration happens before visiting the office.
2. Compute how many extra back-and-forth steps are needed to reach at least the required step count for that route.
3. Extra steps must be even, so round an odd gap up by one.
4. Compute the total route if registration happens after visiting the office.
5. Apply the same extra-even-step calculation.
6. Print the smaller of the two totals.

## Example walkthrough
If you need 10 steps but have only walked 7 before registering, you need 3 more, rounded to 4 because extra back-and-forth steps come in pairs.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(1) time and memory.

## Important details
The helper extra_even handles the parity constraint.
