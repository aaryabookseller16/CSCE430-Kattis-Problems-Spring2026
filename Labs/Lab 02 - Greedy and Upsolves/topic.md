# Lab 2 Topics

Greedy balancing, paper-size math, brute force, average inequalities, heap medians, and grid reachability.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Ljutnja** (`solved-in-lab/Ljutnja`): water-filling greedy distribution. Complexity: O(n log n) time for sorting; memory O(n).
- **A1 Paper** (`solved-in-lab/a1-paper`): greedy paper assembly. Complexity: O(n) time and O(n) memory for counts.
- **The Easiest Problem Is This One** (`solved-in-lab/easiest-problem`): brute-force digit sums. Complexity: O(p * digits(N*p)) per query; memory O(1).
- **Paradox With Averages** (`solved-in-lab/paradox-with-averages`): average inequality test. Complexity: O(N_CS + N_E) per case; memory O(total students).
- **Ragged Right** (`solved-in-lab/ragged-right`): line length penalty sum. Complexity: O(number of lines) time and O(number of lines) memory.
- **Thanos the Hero** (`solved-in-lab/thanos-the-hero`): right-to-left greedy adjustment. Complexity: O(n) time and O(n) memory.
- **Cookie Selection** (`upsolve/cookie-selection`): two heaps for upper median. Complexity: O(log n) per insert or # request; memory O(n).
- **Railway Runner** (`upsolve/railway-runner`): BFS on a 3-column grid. Complexity: O(N) time and memory because there are only 3 columns.

## Main concepts covered
- water-filling greedy distribution
- greedy paper assembly
- brute-force digit sums
- average inequality test
- line length penalty sum
- right-to-left greedy adjustment
- two heaps for upper median
- BFS on a 3-column grid

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
