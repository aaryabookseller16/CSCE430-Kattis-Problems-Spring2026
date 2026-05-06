# Solution: Exam

## Goal
Solve the problem with count matching and differing answers. The implementation's main job is: Where your answer matches your friend, you can be correct only when the friend is correct. Where they differ, you can be correct only when the friend is wrong.

## Key idea
The solution is built around count matching and differing answers. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Where your answer matches your friend, you can be correct only when the friend is correct. Where they differ, you can be correct only when the friend is wrong.

## Step-by-step algorithm
1. Build a bipartite graph from left-side choices to right-side resources.
2. Add an edge whenever that assignment is allowed.
3. Maintain the current matched left item for each right item.
4. For each left item, search for an augmenting path to a free right item.
5. When a path is found, flip the matches along that path.
6. Count the number of successful augmentations.
7. Convert that matched count into the requested answer.

## Example walkthrough
If you match in 6 spots and the friend got 4 correct, at most 4 of those matching spots can help you.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n) time and O(1) memory.

## Important details
The formula is min(same,k) + min(diff,n-k).
