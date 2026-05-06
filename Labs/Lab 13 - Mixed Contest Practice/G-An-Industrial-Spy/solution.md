# Solution: An Industrial Spy

## Goal
Solve the problem with permutation generation and primality testing. The implementation's main job is: The code creates every distinct number that can be formed from one or more digits, then tests each for primality.

## Key idea
The solution is built around permutation generation and primality testing. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code creates every distinct number that can be formed from one or more digits, then tests each for primality.

## Step-by-step algorithm
1. Create the weighted graph that represents possible connections.
2. Treat any already-free connection as an edge of cost 0.
3. Run Prim or Kruskal to choose the cheapest edges that connect all required nodes.
4. Skip edges that connect vertices already in the same component or tree.
5. Accumulate the cost of chosen paid edges.
6. Handle special problem rules, such as removing the largest satellite edges or attaching insecure nodes as leaves.
7. Print the selected edges or total cost.

## Example walkthrough
Digits 011 can form 11, 101, and other numbers; duplicates are removed by a set.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Up to O(sum P(d,k) * sqrt(value)) per case; memory O(number of distinct values).

## Important details
Leading zeroes are naturally handled by int().

## Other implementations in this folder
- `solution_sieve.md` has its own markdown explanation.
