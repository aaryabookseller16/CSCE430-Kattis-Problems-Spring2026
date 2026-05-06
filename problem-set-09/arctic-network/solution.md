# Solution: Arctic Network

## Goal
Solve the problem with minimum spanning tree. The implementation's main job is: The code builds the complete graph of outpost distances, finds an MST, and removes the largest S-1 MST edges because satellite channels connect those clusters.

## Key idea
The solution is built around minimum spanning tree. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code builds the complete graph of outpost distances, finds an MST, and removes the largest S-1 MST edges because satellite channels connect those clusters.

## Step-by-step algorithm
1. Create the weighted graph that represents possible connections.
2. Treat any already-free connection as an edge of cost 0.
3. Run Prim or Kruskal to choose the cheapest edges that connect all required nodes.
4. Skip edges that connect vertices already in the same component or tree.
5. Accumulate the cost of chosen paid edges.
6. Handle special problem rules, such as removing the largest satellite edges or attaching insecure nodes as leaves.
7. Print the selected edges or total cost.

## Example walkthrough
With 2 satellites, the longest radio edge in the MST can be skipped.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(P^2 log P) time and O(P^2) memory due to the complete graph.

## Important details
The printed answer is the largest remaining edge length.
