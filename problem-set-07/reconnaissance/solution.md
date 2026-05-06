# Solution: Reconnaissance

## Goal
Solve the problem with ternary search on a convex function. The implementation's main job is: At time t, the needed sensor range is max position minus min position. That spread is convex, so ternary search finds its minimum.

## Key idea
The solution is built around ternary search on a convex function. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: At time t, the needed sensor range is max position minus min position. That spread is convex, so ternary search finds its minimum.

## Step-by-step algorithm
1. Identify the continuous convex/unimodal function being minimized.
2. Start with a time interval that contains the optimum.
3. Evaluate the function at two interior points.
4. Discard the third of the interval that cannot contain the minimum.
5. Repeat enough times for the required precision.
6. Evaluate once more near the final midpoint.
7. Print the minimized value.

## Example walkthrough
Two vehicles moving toward each other have spread decreasing to 0, then increasing.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(n * iterations), with 200 fixed iterations; memory O(n).

## Important details
The output tolerance allows floating-point search.
