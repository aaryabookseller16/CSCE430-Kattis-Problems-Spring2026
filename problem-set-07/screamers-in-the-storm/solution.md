# Solution: Screamers in the Storm

## Goal
Solve the problem with matrix exponentiation over allowed adjacent heights. The implementation's main job is: A K by K transition matrix marks pairs of heights with gcd 1. Raising it to N-1 counts all valid strings of length N.

## Key idea
The solution is built around matrix exponentiation over allowed adjacent heights. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: A K by K transition matrix marks pairs of heights with gcd 1. Raising it to N-1 counts all valid strings of length N.

## Step-by-step algorithm
1. Build a transition matrix where entry i,j is 1 when state i can move to state j.
2. Start with a vector representing strings or states of length 1.
3. Use binary exponentiation for N-1 transitions.
4. Whenever a power bit is set, multiply the current vector by the matrix.
5. Square the matrix after each bit.
6. Take all operations modulo the required modulus.
7. Sum or read the final vector to get the answer.

## Example walkthrough
For K=2, height 1 can be next to anything and height 2 can only be next to 1.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(K^3 log N) time and O(K^2) memory.

## Important details
The vector starts with one way to end at each height for a one-dune string.
