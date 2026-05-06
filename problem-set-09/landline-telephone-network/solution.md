# Solution: Landline Telephone Network

## Goal
Solve the problem with modified MST with special leaf nodes. The implementation's main job is: Insecure buildings must attach directly to a secure building. The code chooses each insecure building cheapest secure edge, then runs Kruskal among secure buildings.

## Key idea
The solution is built around modified MST with special leaf nodes. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Insecure buildings must attach directly to a secure building. The code chooses each insecure building cheapest secure edge, then runs Kruskal among secure buildings.

## Step-by-step algorithm
1. Create the weighted graph that represents possible connections.
2. Treat any already-free connection as an edge of cost 0.
3. Run Prim or Kruskal to choose the cheapest edges that connect all required nodes.
4. Skip edges that connect vertices already in the same component or tree.
5. Accumulate the cost of chosen paid edges.
6. Handle special problem rules, such as removing the largest satellite edges or attaching insecure nodes as leaves.
7. Print the selected edges or total cost.

## Example walkthrough
An insecure building with two possible secure links keeps only the cheaper one.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(m log m) time and O(n+m) memory.

## Important details
If a required insecure or secure connection is missing, it prints impossible.
