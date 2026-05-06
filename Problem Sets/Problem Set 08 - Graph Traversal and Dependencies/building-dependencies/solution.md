# Solution: Building Dependencies

## Goal
Solve the problem with reverse graph search and topological sort. The implementation's main job is: The changed file reaches every file that depends on it through reverse edges. Then the affected subgraph is topologically sorted so dependencies print first.

## Key idea
The solution is built around reverse graph search and topological sort. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The changed file reaches every file that depends on it through reverse edges. Then the affected subgraph is topologically sorted so dependencies print first.

## Step-by-step algorithm
1. Read the factorial value as a string so huge numbers do not overflow.
2. Check the small factorials directly because several have short digit lengths.
3. For larger inputs, keep a running sum of log10(i).
4. After each i, the digit count of i! is floor(sum)+1.
5. Stop when that digit count equals the input length.
6. Print the corresponding i.

## Example walkthrough
If base changes, files set and map are marked, then solution waits until those dependencies print.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n+e) time and memory.

## Important details
Only dependencies among affected files contribute to indegrees.
