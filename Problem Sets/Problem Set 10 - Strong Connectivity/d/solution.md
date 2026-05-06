# Solution: Strong Connectivity Augmentation

## Goal
Solve the problem with SCC condensation graph. The implementation's main job is: The code finds SCCs, then counts source and sink components in the DAG. To make the graph strongly connected, the answer is max(sources, sinks).

## Key idea
The solution is built around SCC condensation graph. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The code finds SCCs, then counts source and sink components in the DAG. To make the graph strongly connected, the answer is max(sources, sinks).

## Step-by-step algorithm
1. Build both the directed graph and its reverse graph.
2. Run the first DFS pass to get vertices in finishing order.
3. Run the second pass on the reversed graph in reverse finishing order.
4. Assign each vertex to a strongly connected component.
5. Use component sizes or build the condensation graph, depending on the problem.
6. Compute the requested value from the SCC structure.
7. Print that value.

## Example walkthrough
If the condensed graph has two source components and one sink component, at least two new edges are needed.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n+m) time and memory per test case.

## Important details
If the original graph is already one SCC, the answer is 0.
