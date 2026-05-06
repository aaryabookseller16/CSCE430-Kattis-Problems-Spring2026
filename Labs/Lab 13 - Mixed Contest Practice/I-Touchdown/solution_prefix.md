# Prefix Solution: Touchdown

## What this version changes
This markdown explains `solution_prefix.py`. The approach is prefix position computation followed by drive simulation. This version first computes the field position after every play, then applies the same drive-ending rules to that position list.

## Step-by-step algorithm
1. Read all plays.
2. Starting from the 20 yard line, build a list of positions after each play.
3. Initialize the first-down line to 30 and play count to 0.
4. Scan positions in order.
5. Stop with Touchdown if position is at least 100, or Safety if it is at most 0.
6. Otherwise update plays since first down and reset on a first down.
7. If four plays pass without a first down, stop with Nothing.

## Example walkthrough
Positions 25, 31 reset the first-down target from 30 to 41 on the second play.

## Complexity
O(N) time and O(N) memory for the position list.

## Important details
The main solution updates the position and rules in a single pass; this version separates those two ideas.
