# Solution: Eroding Pillars

## Goal
Solve the problem with binary search over distances plus articulation points. The implementation's main job is: The answer must be one of the pairwise distances. For each candidate jump distance, the code builds a graph and checks that every pillar is reachable and no non-start pillar is an articulation point.

## Key idea
The solution is built around binary search over distances plus articulation points. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The answer must be one of the pairwise distances. For each candidate jump distance, the code builds a graph and checks that every pillar is reachable and no non-start pillar is an articulation point.

## Step-by-step algorithm
1. Build the undirected graph with edge ids when needed.
2. Run DFS while recording discovery times.
3. Maintain low-link values that show how far back each subtree can reach.
4. Use low-link tests to mark bridges or articulation points.
5. Run the second problem-specific pass using only safe edges or accepted candidate graphs.
6. Use reachability or validity of that pass to decide the answer.
7. Print the count or minimum distance.

## Example walkthrough
If removing one middle pillar disconnects the graph, that jump distance is too small.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(D * (n^2+n+m)) where D is log of the number of unique distances; memory O(n^2) for candidate graphs.

## Important details
Distances are compared squared, then square-rooted for output.
