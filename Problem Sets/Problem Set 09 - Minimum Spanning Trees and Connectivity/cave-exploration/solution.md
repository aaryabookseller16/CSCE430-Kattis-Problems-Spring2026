# Solution: Cave Exploration

## Goal
Solve the problem with bridge-finding with low-link DFS. The implementation's main job is: First the code marks every bridge. Then it walks from room 0 while ignoring bridges; those rooms are safe because no single edge can cut them off.

## Key idea
The solution is built around bridge-finding with low-link DFS. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: First the code marks every bridge. Then it walks from room 0 while ignoring bridges; those rooms are safe because no single edge can cut them off.

## Step-by-step algorithm
1. Build the undirected graph with edge ids when needed.
2. Run DFS while recording discovery times.
3. Maintain low-link values that show how far back each subtree can reach.
4. Use low-link tests to mark bridges or articulation points.
5. Run the second problem-specific pass using only safe edges or accepted candidate graphs.
6. Use reachability or validity of that pass to decide the answer.
7. Print the count or minimum distance.

## Example walkthrough
In a triangle, no edge is a bridge, so all three rooms stay reachable.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n+m) time and memory.

## Important details
The DFS is iterative instead of recursive.
