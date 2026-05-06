# Solution: Semi-prime H-numbers

## Goal
Solve the problem with custom sieve and prefix counts. The implementation's main job is: The solution marks H-composites, collects H-primes, marks products of two H-primes, then builds prefix counts for fast queries.

## Key idea
The solution is built around custom sieve and prefix counts. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The solution marks H-composites, collects H-primes, marks products of two H-primes, then builds prefix counts for fast queries.

## Step-by-step algorithm
1. Read all queries first and find the largest value that must be answered.
2. Generate or mark only the numbers relevant to this special number system.
3. Use a sieve-style pass to decide which numbers are prime in that system.
4. Generate products of two such primes and mark them as semiprimes.
5. Build a prefix-count array where prefix[x] is the number of semiprimes up to x.
6. Answer each query by looking up the prefix value.

## Example walkthrough
25 is counted because 25 = 5*5, and 85 is counted because 85 = 5*17.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Precomputation is roughly O(H^2/16) in the worst case but stops products above the maximum query; queries are O(1).

## Important details
Only numbers congruent to 1 modulo 4 are meaningful in this problem.
