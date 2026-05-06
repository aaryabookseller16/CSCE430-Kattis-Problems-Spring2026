# Solution: Character Development

## Goal
Solve the problem with combinatorics with powers of two. The implementation's main job is: Every subset of at least two characters is a relationship, so the answer is 2^N minus singleton groups and the empty group.

## Key idea
The solution is built around combinatorics with powers of two. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Every subset of at least two characters is a relationship, so the answer is 2^N minus singleton groups and the empty group.

## Step-by-step algorithm
1. Identify the set of all possible groups or choices.
2. Count all subsets with a power of two.
3. Subtract invalid subsets such as the empty set or singleton sets.
4. Keep the result as an integer.
5. Print the final count.

## Example walkthrough
For N=3, subsets of size at least 2 are AB, AC, BC, ABC, so answer 4.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N) big-integer multiplications in the checked-in loop; memory O(1) besides the big integer.

## Important details
Python handles the large integer directly.

## Other implementations in this folder
- `solution_formula.md` has its own markdown explanation.
