# Problem Set 13 Topics

Number theory and counting: modular inverses, factorial digit estimates, custom sieves, cycle detection, and greedy scheduling.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Candy Distribution** (`A-Candy-Distribution`): number theory and extended Euclidean algorithm. Complexity: O(log min(K,C)) per test case; memory O(1).
- **Inverse Factorial** (`B-Inverse_Factorial`): factorial digit counting with logarithms. Complexity: O(n) where n is the recovered factorial argument; memory O(1) after reading the input string.
- **Semi-prime H-numbers** (`C-Semi-Prime-H-Numbers`): custom sieve and prefix counts. Complexity: Precomputation is roughly O(H^2/16) in the worst case but stops products above the maximum query; queries are O(1).
- **Checked-in H-number Sieve** (`D-A-Vicious-Pikeman(easy)`): custom sieve and prefix counts. Complexity: Precomputation depends on the largest query; each printed answer is O(1).
  - Alternate: `solution_slow.md` - Slow Solution: H-number Semiprimes. Complexity: Much slower than the sieve version; roughly quadratic over the H-number list before query answering. Memory O(max h).
- **A Vicious Pikeman Hard** (`E-A-Vicious-Pikeman(hard)`): cycle detection, counting sort idea, and greedy scheduling. Complexity: O(C + cycle_length) time and O(C) memory, where C is the modulus/range of generated times.

## Main concepts covered
- number theory and extended Euclidean algorithm
- factorial digit counting with logarithms
- custom sieve and prefix counts
- cycle detection, counting sort idea, and greedy scheduling

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
