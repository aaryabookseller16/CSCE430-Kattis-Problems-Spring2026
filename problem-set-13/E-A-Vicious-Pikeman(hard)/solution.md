# Solution: A Vicious Pikeman Hard

## Goal
Solve the problem with cycle detection, counting sort idea, and greedy scheduling. The implementation's main job is: The generated problem times eventually cycle. The code counts how many problems have each solving time, then solves shortest times first to maximize solved count and minimize penalty.

## Key idea
The solution is built around cycle detection, counting sort idea, and greedy scheduling. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The generated problem times eventually cycle. The code counts how many problems have each solving time, then solves shortest times first to maximize solved count and minimize penalty.

## Step-by-step algorithm
1. Generate values in order while recording the first index where each value appeared.
2. If N values are generated before a repeat, count the values directly.
3. If a repeat appears, split the generated list into a prefix and a cycle.
4. Count the prefix once.
5. Add full-cycle repetitions using integer division.
6. Add the leftover cycle prefix using the remainder.
7. Process the counted values in sorted order for the final greedy calculation.

## Example walkthrough
If there are two 3-minute tasks and one 10-minute task, the 3-minute tasks are always attempted first.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(C + cycle_length) time and O(C) memory, where C is the modulus/range of generated times.

## Important details
The penalty is updated with an arithmetic-series formula so repeated equal-duration tasks are handled in one batch.
