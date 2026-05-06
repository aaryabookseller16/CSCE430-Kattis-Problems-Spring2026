# Solution: Lost Map

## Goal
Solve the problem with Prim MST on a complete distance table. The implementation's main job is: The original road network is the MST of the all-pairs shortest-path distance table. The code runs Prim directly on that complete graph.

## Key idea
The solution is built around Prim MST on a complete distance table. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The original road network is the MST of the all-pairs shortest-path distance table. The code runs Prim directly on that complete graph.

## Step-by-step algorithm
1. Create the weighted graph that represents possible connections.
2. Treat any already-free connection as an edge of cost 0.
3. Run Prim or Kruskal to choose the cheapest edges that connect all required nodes.
4. Skip edges that connect vertices already in the same component or tree.
5. Accumulate the cost of chosen paid edges.
6. Handle special problem rules, such as removing the largest satellite edges or attaching insecure nodes as leaves.
7. Print the selected edges or total cost.

## Example walkthrough
If village 1 is distance 1 from villages 2 and 3, those edges are likely chosen before longer alternatives.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n^2) time and O(n^2) memory for the distance table.

## Important details
The output can be any valid set of original roads.
