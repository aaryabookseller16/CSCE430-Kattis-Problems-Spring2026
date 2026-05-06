# Solution: Mini Battleship

## Goal
Solve the problem with backtracking search. The implementation's main job is: The solution tries every horizontal or vertical placement for each ship, avoiding misses and already used cells, then checks all known hits.

## Key idea
The solution is built around backtracking search. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The solution tries every horizontal or vertical placement for each ship, avoiding misses and already used cells, then checks all known hits.

## Step-by-step algorithm
1. Read board size, ship count, board clues, and ship lengths.
2. Record known hit cells and known miss cells.
3. Use a grid_used array to mark cells occupied by ships in the current search branch.
4. For the current ship, try every horizontal placement and every vertical placement.
5. Reject placements that leave the board, overlap another ship, or cover a miss.
6. Recurse to place the next ship.
7. After all ships are placed, count the arrangement only if every known hit is covered.

## Example walkthrough
A size-3 ship can be placed at row 0 columns 1-3 only if none of those cells is a miss.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Exponential in the number of ships and possible placements; memory O(n^2).

## Important details
Length-1 ships are not double-counted as both horizontal and vertical.
