# Solution: Avoiding the Apocalypse

## Goal
Solve the problem with time-expanded network flow with Dinic. The implementation's main job is: Each location is copied once per time step. Waiting edges, road edges, and medical-facility edges turn the scheduling problem into max flow.

## Key idea
The solution is built around time-expanded network flow with Dinic. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Each location is copied once per time step. Waiting edges, road edges, and medical-facility edges turn the scheduling problem into max flow.

## Step-by-step algorithm
1. Create a source and sink for the flow model.
2. Add nodes for each category in the problem, such as time layers, people, parties, clubs, or locations.
3. Add directed edges with capacities that represent the original limits.
4. Run BFS levels and blocking-flow pushes using Dinic.
5. Repeat until no augmenting path remains or the needed flow has been sent.
6. Interpret the amount of flow, or the saturated edges, as the answer.
7. Print the resulting count or assignment.

## Example walkthrough
A road taking 3 minutes from A to B becomes an edge from A at time 2 to B at time 5.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Let V=n(s+1) and E include all time-expanded roads; Dinic runs over that graph, with flow capped by the group size.

## Important details
This handles splitting people across different routes.
