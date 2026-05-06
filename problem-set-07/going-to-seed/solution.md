# Solution: Going to Seed

## Goal
Solve the problem with interactive interval splitting. The implementation's main job is: The possible tree interval expands by one each round because the target moves, then it is split into four parts encoded by two yes/no answers.

## Key idea
The solution is built around interactive interval splitting. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The possible tree interval expands by one each round because the target moves, then it is split into four parts encoded by two yes/no answers.

## Step-by-step algorithm
1. Keep the current possible interval of target trees.
2. Before each query, expand the interval by one on both sides because the target moves to an adjacent tree.
3. If only two or three trees remain possible, use a small direct query to distinguish them.
4. Otherwise split the expanded interval into four chunks.
5. Ask two range queries whose yes/no pair encodes the chunk containing the target.
6. Replace the possible interval with the selected chunk.
7. After at most 16 rounds, print the remaining tree as the answer.

## Example walkthrough
Answers 00, 10, 11, and 01 select one of four chunks.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
At most 16 queries; memory O(1).

## Important details
This is an interactive solution and depends on judge replies.
