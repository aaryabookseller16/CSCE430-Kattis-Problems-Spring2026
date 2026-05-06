# Solution: Gopher II

## Goal
Solve the problem with bipartite matching. The implementation's main job is: A gopher connects to every hole it can reach before the deadline. Maximum matching gives the most saved gophers.

## Key idea
The solution is built around bipartite matching. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: A gopher connects to every hole it can reach before the deadline. Maximum matching gives the most saved gophers.

## Step-by-step algorithm
1. Build a bipartite graph from left-side choices to right-side resources.
2. Add an edge whenever that assignment is allowed.
3. Maintain the current matched left item for each right item.
4. For each left item, search for an augmenting path to a free right item.
5. When a path is found, flip the matches along that path.
6. Count the number of successful augmentations.
7. Convert that matched count into the requested answer.

## Example walkthrough
If gopher 1 can reach holes A and B, and gopher 2 can only reach B, augmenting paths can reassign gopher 1 to A.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n * E) with BFS augmenting paths in the checked-in implementation; memory O(E).

## Important details
The answer is total gophers minus matched gophers.
