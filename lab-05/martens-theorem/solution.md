# Solution: Martens Theorem

## Goal
Solve the problem with union-find over rhyme/equality constraints. The implementation's main job is: Words are unioned when rules imply they rhyme, including suffix buckets and explicit is statements. Then not statements are checked for contradictions.

## Key idea
The solution is built around union-find over rhyme/equality constraints. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Words are unioned when rules imply they rhyme, including suffix buckets and explicit is statements. Then not statements are checked for contradictions.

## Step-by-step algorithm
1. Give every object an integer id.
2. Initialize each id as its own parent with size or sum metadata.
3. Use find with path compression to locate component roots.
4. For union operations, attach the smaller component to the larger one.
5. Update component metadata at the new root.
6. For special move operations, create a fresh node when an element changes sets.
7. Answer queries from the metadata stored at the root.

## Example walkthrough
If cat is bat, and cat not bat appears later, the final check fails.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Near O(W alpha(W) + suffix grouping) time; memory O(W).

## Important details
The suffix rules create extra implied unions before checking contradictions.
