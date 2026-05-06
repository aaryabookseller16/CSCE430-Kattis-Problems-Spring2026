# Solution: Chasing Subs

## Goal
Solve the problem with isomorphic string matching with per-letter hash signatures. The implementation's main job is: A window matches the fragment when the pattern of repeated letters is the same, even if the actual letters differ. The code compares sorted per-letter occurrence hashes.

## Key idea
The solution is built around isomorphic string matching with per-letter hash signatures. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: A window matches the fragment when the pattern of repeated letters is the same, even if the actual letters differ. The code compares sorted per-letter occurrence hashes.

## Step-by-step algorithm
1. Compute an occurrence-position signature for each letter in the fragment.
2. Build the same kind of signature for the first message window.
3. For each window, normalize its signatures so absolute position does not matter.
4. Sort the 26 letter signatures and compare with the fragment signature.
5. If they match, record that starting position.
6. Slide the window by removing the outgoing letter contribution and adding the incoming one.
7. Print the matching substring if unique, otherwise print the number of matches.

## Example walkthrough
Pattern wood matches a window like essa because the first and second letters form the same repeat structure.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(26*n log 26) time, effectively linear with a small constant; memory O(26).

## Important details
Double hashing is used to make the occurrence signatures robust.
