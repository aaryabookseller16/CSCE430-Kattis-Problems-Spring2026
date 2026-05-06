# Solution: Ljutnja

## Goal
Solve the problem with water-filling greedy distribution. The implementation's main job is: The total missing candies are spread as evenly as possible because squared anger is minimized by balanced deprivation. Caps stop a child from missing more than they asked for.

## Key idea
The solution is built around water-filling greedy distribution. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The total missing candies are spread as evenly as possible because squared anger is minimized by balanced deprivation. Caps stop a child from missing more than they asked for.

## Step-by-step algorithm
1. Read total candies, child count, and each child request.
2. Compute total deprivation: total requested minus available candies.
3. Sort requests so small requests cap first.
4. Raise a common missing-candy level across all still-uncapped children.
5. When the next request value is reached, that child cannot miss more than requested and becomes capped.
6. If deprivation runs out between two levels, split the remaining missing candies as evenly as possible.
7. Sum squared missing candies and print the minimum anger.

## Example walkthrough
If three children miss 5 candies total, 2,2,1 is better than 5,0,0.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n log n) time for sorting; memory O(n).

## Important details
The code raises a common deprivation level across children.
