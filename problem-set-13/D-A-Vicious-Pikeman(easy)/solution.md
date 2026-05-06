# Solution: Checked-in H-number Sieve

## Goal
Solve the problem with custom sieve and prefix counts. The implementation's main job is: Despite the folder name, the checked-in description and solution implement the H-semi-prime counting problem.

## Key idea
The solution is built around custom sieve and prefix counts. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Despite the folder name, the checked-in description and solution implement the H-semi-prime counting problem.

## Step-by-step algorithm
1. Read all queries first and find the largest value that must be answered.
2. Generate or mark only the numbers relevant to this special number system.
3. Use a sieve-style pass to decide which numbers are prime in that system.
4. Generate products of two such primes and mark them as semiprimes.
5. Build a prefix-count array where prefix[x] is the number of semiprimes up to x.
6. Answer each query by looking up the prefix value.

## Example walkthrough
For a query 85, the prefix array returns 5 because there are five H-semi-primes up to 85.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Precomputation depends on the largest query; each printed answer is O(1).

## Important details
This documentation follows solution.py, not the folder title.

## Other implementations in this folder
- `solution_slow.md` has its own markdown explanation.
