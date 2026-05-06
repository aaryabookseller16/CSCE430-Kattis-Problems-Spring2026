# Solution: Money Matters

## Goal
Solve the problem with connected-component sum check. The implementation's main job is: Friendships form components where money can be balanced internally. Each component must have total balance zero.

## Key idea
The solution is built around connected-component sum check. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Friendships form components where money can be balanced internally. Each component must have total balance zero.

## Step-by-step algorithm
1. Read balances and friendships.
2. Build an undirected graph of friendships.
3. Visit every connected component with DFS or a stack.
4. While visiting a component, sum all balances in it.
5. If any component sum is not zero, balancing debts inside that component is impossible.
6. Print POSSIBLE only if every component has sum zero.

## Example walkthrough
Balances +5 and -5 in the same component cancel; +5 alone cannot.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n+m) time and memory.

## Important details
The DFS is iterative.
