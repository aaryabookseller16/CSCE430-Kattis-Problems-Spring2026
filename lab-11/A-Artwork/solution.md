# Solution: Artwork

## Goal
Solve the problem with reverse processing with union-find. The implementation's main job is: The grid is painted forward to know the final black cells. Then strokes are undone backward, adding white cells and unioning neighboring white regions.

## Key idea
The solution is built around reverse processing with union-find. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The grid is painted forward to know the final black cells. Then strokes are undone backward, adding white cells and unioning neighboring white regions.

## Step-by-step algorithm
1. Give every object an integer id.
2. Initialize each id as its own parent with size or sum metadata.
3. Use find with path compression to locate component roots.
4. For union operations, attach the smaller component to the larger one.
5. Update component metadata at the new root.
6. For special move operations, create a fresh node when an element changes sets.
7. Answer queries from the metadata stored at the root.

## Example walkthrough
Adding back a white cell between two white areas merges two components into one.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(nm + total stroke length * alpha(nm)) time; memory O(nm).

## Important details
Reverse processing avoids having to delete cells from a DSU.
