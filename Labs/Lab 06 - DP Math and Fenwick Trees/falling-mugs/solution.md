# Solution: Falling Mugs

## Goal
Solve the problem with difference of squares search. The implementation's main job is: The problem asks for integers a,b with b^2 - a^2 equal to the target. The code tries b and checks whether b^2-D is a square.

## Key idea
The solution is built around difference of squares search. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The problem asks for integers a,b with b^2 - a^2 equal to the target. The code tries b and checks whether b^2-D is a square.

## Step-by-step algorithm
1. Read the target distance D.
2. Try possible later frame numbers b.
3. Compute b squared.
4. Set a_squared = b_squared - D.
5. If a_squared is nonnegative and a perfect square, then a^2 and b^2 differ by D.
6. Print a and b for the first such pair.
7. If no pair is found in the searched range, print impossible.

## Example walkthrough
If D=7, then 4^2-3^2=7, so it prints 3 4.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(D) in the simple bound used; memory O(1).

## Important details
math.isqrt avoids floating-point square checks.
