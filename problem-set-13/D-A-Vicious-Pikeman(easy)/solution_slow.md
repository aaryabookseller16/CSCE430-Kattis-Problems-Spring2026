# Slow Solution: H-number Semiprimes

## What this version changes
This markdown explains `solution_slow.py`. The approach is direct H-prime testing and semiprime marking. This version builds H-numbers, tests each possible H-prime by trial factors, then marks products of two H-primes.

## Step-by-step algorithm
1. Read every query and find the largest requested H-number.
2. Generate numbers 5, 9, 13, ... up to that maximum.
3. For each H-number, try H-number factors to see whether it can be split into smaller H-numbers.
4. Collect the numbers that cannot be split as H-primes.
5. Mark every product of two H-primes that stays within the maximum.
6. Build a prefix count array and answer each query in O(1).

## Example walkthrough
25 is marked because 5 and 5 are both H-primes, so 25 is an H-semiprime.

## Complexity
Much slower than the sieve version; roughly quadratic over the H-number list before query answering. Memory O(max h).

## Important details
This folder name says Vicious Pikeman, but this file also solves the H-number semiprime problem.
