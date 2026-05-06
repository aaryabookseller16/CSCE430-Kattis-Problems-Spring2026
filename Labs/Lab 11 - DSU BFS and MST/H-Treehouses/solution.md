# Solution: Treehouses

## Goal
Solve the problem with Prim MST with zero-cost existing edges. The implementation's main job is: Existing cables and land-connected first houses are treated as zero-cost edges. Prim then chooses the cheapest new cables to connect everything.

## Key idea
The solution is built around Prim MST with zero-cost existing edges. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Existing cables and land-connected first houses are treated as zero-cost edges. Prim then chooses the cheapest new cables to connect everything.

## Step-by-step algorithm
1. Create the weighted graph that represents possible connections.
2. Treat any already-free connection as an edge of cost 0.
3. Run Prim or Kruskal to choose the cheapest edges that connect all required nodes.
4. Skip edges that connect vertices already in the same component or tree.
5. Accumulate the cost of chosen paid edges.
6. Handle special problem rules, such as removing the largest satellite edges or attaching insecure nodes as leaves.
7. Print the selected edges or total cost.

## Example walkthrough
If treehouse 1 and 2 are already connected, the algorithm can move between them at cost 0.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n^2) time and O(n+p) memory.

## Important details
Euclidean distance is used for new cable costs.
