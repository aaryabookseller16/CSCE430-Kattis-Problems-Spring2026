# Solution: Secret Message

## Goal
Solve the problem with grid padding and rotation. The implementation's main job is: The message is padded to a square, written row by row, rotated 90 degrees clockwise, and read while skipping stars.

## Key idea
The solution is built around grid padding and rotation. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: The message is padded to a square, written row by row, rotated 90 degrees clockwise, and read while skipping stars.

## Step-by-step algorithm
1. Read each message.
2. Find the smallest square side length that can contain the message.
3. Pad the message with stars until it fills that square.
4. Write the padded message row by row into a grid.
5. Rotate the grid 90 degrees clockwise by mapping old cell (r,c) to new cell (c, side-1-r).
6. Read the rotated grid row by row, skipping stars.
7. Print the resulting encrypted message.

## Example walkthrough
A length 12 message pads to a 4x4 grid before rotation.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
O(L) time and memory per message.

## Important details
The side length is ceil(sqrt(L)).
