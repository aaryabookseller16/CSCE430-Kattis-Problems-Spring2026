# Solution: Judging Troubles

## Goal
Solve the problem with multiset intersection with Counters. The implementation's main job is: Both judges outputs are counted by verdict string. The answer sums the overlap count for each verdict.

## Key idea
The solution is built around multiset intersection with Counters. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Both judges outputs are counted by verdict string. The answer sums the overlap count for each verdict.

## Step-by-step algorithm
1. Read the number of submissions.
2. Count how many times each verdict appears in DOMjudge output.
3. Count how many times each verdict appears in Kattis output.
4. For each verdict, add the smaller of the two counts to the answer.
5. Print the total overlap count.

## Example walkthrough
If one list has WA twice and the other has WA once, they match once.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and memory.

## Important details
Counter handles duplicate verdicts directly.
