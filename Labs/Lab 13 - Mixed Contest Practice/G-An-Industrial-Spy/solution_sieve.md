# Sieve Solution: An Industrial Spy

## What this version changes
This markdown explains `solution_sieve.py`. The approach is prime sieve plus permutation generation. This version precomputes primality up to the largest number any test case can form, then checks generated numbers by table lookup.

## Step-by-step algorithm
1. Read all digit strings first.
2. For each string, sort digits descending to estimate the largest possible formed number.
3. Run a sieve of Eratosthenes up to the largest such number.
4. For each test case, generate every distinct number from all nonempty digit permutations.
5. Count how many generated numbers are prime according to the sieve.
6. Print the count.

## Example walkthrough
For digits 17, generated values include 7, 17, and 71, and all three are prime.

## Complexity
O(M log log M) sieve time plus permutation generation per test, where M is the maximum formed number; memory O(M).

## Important details
This is faster than trial division when many generated numbers must be tested.
