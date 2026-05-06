# Solution: Club Representative Assignment

## Goal
Solve the problem with max flow with party/person/club layers. The implementation's main job is: The graph sends flow from parties to people to clubs. Party capacities prevent one party from controlling too many club representatives.

## Key idea
The solution is built around max flow with party/person/club layers. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The graph sends flow from parties to people to clubs. Party capacities prevent one party from controlling too many club representatives.

## Step-by-step algorithm
1. Create a source and sink for the flow model.
2. Add nodes for each category in the problem, such as time layers, people, parties, clubs, or locations.
3. Add directed edges with capacities that represent the original limits.
4. Run BFS levels and blocking-flow pushes using Dinic.
5. Repeat until no augmenting path remains or the needed flow has been sent.
6. Interpret the amount of flow, or the saturated edges, as the answer.
7. Print the resulting count or assignment.

## Example walkthrough
If a person belongs to Chess and Drama, one unit of flow through that person chooses at most one of those clubs.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Dinic on O(parties + people + clubs) nodes and membership edges; memory O(E).

## Important details
The output is built from saturated person-to-club edges.
