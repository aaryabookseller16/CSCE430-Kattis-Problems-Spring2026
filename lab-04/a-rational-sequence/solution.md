# Solution: A Rational Sequence

## Goal
Solve the problem with Calkin-Wilf next-fraction formula. The implementation's main job is: The code computes the next fraction in the rational sequence directly from p/q.

## Key idea
The solution is built around Calkin-Wilf next-fraction formula. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code computes the next fraction in the rational sequence directly from p/q.

## Step-by-step algorithm
1. Read the dataset id and current fraction p/q.
2. Split the fraction into numerator p and denominator q.
3. The next numerator is q.
4. Compute the next denominator using the Calkin-Wilf next formula.
5. Print the dataset id followed by the new fraction.

## Example walkthrough
For a fraction p/q, the next numerator is q, and the denominator formula uses floor(p/q).

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(1) per test case; memory O(1).

## Important details
Dataset ids are echoed in the output.
