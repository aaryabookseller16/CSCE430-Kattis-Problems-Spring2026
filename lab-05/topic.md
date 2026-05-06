# Lab 5 Topics

Greedy scans, sorting, component sums, union-find constraints, and topological propagation.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Bungee Builder** (`bungee-builder`): prefix/suffix maxima. Complexity: O(n) time and O(n) memory.
- **H-Index** (`h-index`): sorting and scan. Complexity: O(n log n) time and O(n) memory.
- **Island in the Data Stream** (`island-in-the-data-stream`): brute-force subarray counting. Complexity: O(12^3) per dataset as written, which is constant for the fixed 12 values; memory O(1).
- **Judging Troubles** (`judging-troubles`): multiset intersection with Counters. Complexity: O(n) time and memory.
- **Martens Theorem** (`martens-theorem`): union-find over rhyme/equality constraints. Complexity: Near O(W alpha(W) + suffix grouping) time; memory O(W).
- **Money Matters** (`money-matters`): connected-component sum check. Complexity: O(n+m) time and memory.
- **Planetaris** (`planetaris`): greedy sorting. Complexity: O(n log n) time and O(n) memory.
- **Succession** (`succession`): topological propagation of blood fractions. Complexity: O(n+m) time and memory over family records and claimants.

## Main concepts covered
- prefix/suffix maxima
- sorting and scan
- brute-force subarray counting
- multiset intersection with Counters
- union-find over rhyme/equality constraints
- connected-component sum check
- greedy sorting
- topological propagation of blood fractions

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
