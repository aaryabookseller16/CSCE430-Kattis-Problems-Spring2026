# Solution: Bridges and Tunnels

## Goal
Solve the problem with union-find with name compression. The implementation's main job is: Building names are mapped to integer ids. Each new bridge unions two ids and prints the connected component size.

## Key idea
The solution is built around union-find with name compression. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Building names are mapped to integer ids. Each new bridge unions two ids and prints the connected component size.

## Step-by-step algorithm
1. Build the undirected graph with edge ids when needed.
2. Run DFS while recording discovery times.
3. Maintain low-link values that show how far back each subtree can reach.
4. Use low-link tests to mark bridges or articulation points.
5. Run the second problem-specific pass using only safe edges or accepted candidate graphs.
6. Use reachability or validity of that pass to decide the answer.
7. Print the count or minimum distance.

## Example walkthrough
After MC-DC and DC-Eng, the component containing that new bridge has size 3.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n alpha(n)) time and O(n) memory.

## Important details
The DSU is sized for up to two new names per bridge.
