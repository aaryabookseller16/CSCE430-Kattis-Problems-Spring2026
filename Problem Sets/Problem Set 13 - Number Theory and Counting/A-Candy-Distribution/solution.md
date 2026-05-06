# Solution: Candy Distribution

## Goal
Solve the problem with number theory and extended Euclidean algorithm. The implementation's main job is: The equation C*Y = K*X + 1 becomes C*Y congruent to 1 modulo K. When gcd(C,K)=1, the extended Euclidean algorithm gives the modular inverse Y.

## Key idea
The solution is built around number theory and extended Euclidean algorithm. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The equation C*Y = K*X + 1 becomes C*Y congruent to 1 modulo K. When gcd(C,K)=1, the extended Euclidean algorithm gives the modular inverse Y.

## Step-by-step algorithm
1. Rewrite the candy equation as a modular equation.
2. Handle special cases where one side is 1.
3. Run the extended Euclidean algorithm to compute gcd(C, K) and Bezout coefficients.
4. If the gcd is not 1, no modular inverse exists, so print IMPOSSIBLE.
5. Otherwise turn the coefficient for C into a positive solution modulo K.
6. Check any output bound required by the problem statement.
7. Print the valid bag count.

## Example walkthrough
For K=10 and C=7, 7*3 = 21, which leaves 1 after giving 10 kids 2 candies each, so 3 bags works.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(log min(K,C)) per test case; memory O(1).

## Important details
The checked-in code handles gcd failures and special cases, but it uses an infinite bag limit instead of enforcing the statement limit of 10^9.
