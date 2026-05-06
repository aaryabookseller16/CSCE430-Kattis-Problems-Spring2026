# Slow Solution: Bridge Automation

## What this version changes
This markdown explains `solution_slow.py`. The approach is dynamic programming with explicit group simulation. For every possible group of consecutive boats, this version simulates when the bridge would be raised and how long the group takes.

## Step-by-step algorithm
1. Read all boat arrival times.
2. Let best_time[i] be the minimum closed time for the first i boats.
3. For every last_boat, try every possible first_boat in its final group.
4. Assume the bridge is fully raised as late as allowed for the first boat.
5. Simulate each boat in the group, waiting if needed, and add 20 seconds per boat.
6. Compute the opening cost and update best_time[last_boat].
7. Print best_time[N].

## Example walkthrough
If boats 3 through 5 are grouped, the DP combines best_time[2] with the simulated cost of serving boats 3, 4, and 5 in one opening.

## Complexity
O(N^3) in the direct simulation form; memory O(N).

## Important details
The main solution replaces the inner simulation with a formula, reducing the transition cost.
