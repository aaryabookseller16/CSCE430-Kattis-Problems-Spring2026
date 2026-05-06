# Solution: Buzzwords

## Goal
Solve the problem with double rolling hash for substring counting. The implementation's main job is: For each substring length, the code hashes every substring and records the maximum frequency. It stops once no substring of that length repeats.

## Key idea
The solution is built around double rolling hash for substring counting. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: For each substring length, the code hashes every substring and records the maximum frequency. It stops once no substring of that length repeats.

## Step-by-step algorithm
1. Remove spaces or normalize the input string as required.
2. Build prefix hashes and powers for two moduli.
3. For each candidate length, compute every substring hash in O(1).
4. Count equal hashes in a dictionary.
5. Record the largest count for that length.
6. Stop once the largest count is 1, because no repeated word exists at that length.
7. Print the counts collected before that stopping point.

## Example walkthrough
In ABABA, length 1 has A repeated 3 times and length 2 has AB repeated 2 times.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n^2) time per input line and O(n) memory per length.

## Important details
Two moduli reduce hash collision risk.
