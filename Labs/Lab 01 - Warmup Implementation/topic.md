# Lab 1 Topics

Basic contest implementation: sorting, simulation, grid rotation, greedy pairing, and timeline arithmetic.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Army Strength Hard** (`army-strength-hard`): maximum comparison. Complexity: O(NG+NM) per test case; memory O(1).
- **Bus Numbers** (`bus_numbers`): sorting and run compression. Complexity: O(n log n) time and O(n) memory.
- **Dice Cup** (`dice_cup`): enumerating most likely sums. Complexity: O(n*m) time in the loops, though the ways formula is constant for each sum; memory O(n+m).
- **Exam** (`exam`): count matching and differing answers. Complexity: O(n) time and O(1) memory.
- **Minimum Scalar Product** (`minimum-scalar-product`): greedy sorting by rearrangement inequality. Complexity: O(n log n) per case; memory O(n).
- **Secret Message** (`secret-message`): grid padding and rotation. Complexity: O(L) time and memory per message.
- **Transit Woes** (`transit-woes`): timeline simulation with bus waits. Complexity: O(n) time and O(n) memory for input arrays.
- **Working at the Restaurant** (`working-at-the-restaurant`): two-stack simulation strategy. Complexity: O(number of commands plus emitted operations) time; memory O(output).

## Main concepts covered
- maximum comparison
- sorting and run compression
- enumerating most likely sums
- count matching and differing answers
- greedy sorting by rearrangement inequality
- grid padding and rotation
- timeline simulation with bus waits
- two-stack simulation strategy

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
