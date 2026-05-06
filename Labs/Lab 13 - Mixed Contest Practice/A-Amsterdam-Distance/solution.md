# Solution: Amsterdam Distance

## Goal
Solve the problem with geometry on polar street grid. The implementation's main job is: The code tries every possible ring as the shared curved path: walk radially from both points to that ring, then along the arc.

## Key idea
The solution is built around geometry on polar street grid. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code tries every possible ring as the shared curved path: walk radially from both points to that ring, then along the arc.

## Step-by-step algorithm
1. Create the weighted graph that represents possible connections.
2. Treat any already-free connection as an edge of cost 0.
3. Run Prim or Kruskal to choose the cheapest edges that connect all required nodes.
4. Skip edges that connect vertices already in the same component or tree.
5. Accumulate the cost of chosen paid edges.
6. Handle special problem rules, such as removing the largest satellite edges or attaching insecure nodes as leaves.
7. Print the selected edges or total cost.

## Example walkthrough
Sometimes walking inward to a smaller ring is shorter because the arc radius is smaller.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(N) time over possible meeting rings; memory O(1).

## Important details
Ring width is R/N and angular separation is |a-b|*pi/M.

## Other implementations in this folder
- `solution_formula.md` has its own markdown explanation.
