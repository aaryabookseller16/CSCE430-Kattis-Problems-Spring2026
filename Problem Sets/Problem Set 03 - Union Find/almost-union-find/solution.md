# Solution: Almost Union-Find

## Goal
Solve the problem with DSU with virtual nodes for move operations. The implementation's main job is: Each element has a current node id. Moving an element creates a new node in the target set and subtracts it from the old set.

## Key idea
The solution is built around DSU with virtual nodes for move operations. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Each element has a current node id. Moving an element creates a new node in the target set and subtracts it from the old set.

## Step-by-step algorithm
1. Give every object an integer id.
2. Initialize each id as its own parent with size or sum metadata.
3. Use find with path compression to locate component roots.
4. For union operations, attach the smaller component to the larger one.
5. Update component metadata at the new root.
6. For special move operations, create a fresh node when an element changes sets.
7. Answer queries from the metadata stored at the root.

## Example walkthrough
If 3 moves from set A to set B, node old-3 stays behind but no longer represents element 3.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Almost O(alpha(n+m)) per operation; memory O(n+m).

## Important details
Set size and sum are stored at roots.
