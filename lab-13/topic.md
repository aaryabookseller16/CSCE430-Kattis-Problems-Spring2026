# Lab 13 Topics

Mixed contest practice: geometry, graph cascades, DP grouping, probability enumeration, combinatorics, primality, and simulation.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Amsterdam Distance** (`A-Amsterdam-Distance`): geometry on polar street grid. Complexity: O(N) time over possible meeting rings; memory O(1).
  - Alternate: `solution_formula.md` - Formula Solution: Amsterdam Distance. Complexity: O(1) time and memory.
- **Brexit** (`B-Brexit`): queue simulation on graph thresholds. Complexity: O(C+P) time and memory.
  - Alternate: `solution_slow.md` - Slow Solution: Brexit. Complexity: O(C*P) in the worst case because many full scans can be needed; memory O(C+P).
- **Bridge Automation** (`C-Bridge-Automation`): dynamic programming over grouped arrivals. Complexity: O(N^2) time and O(N) memory.
  - Alternate: `solution_slow.md` - Slow Solution: Bridge Automation. Complexity: O(N^3) in the direct simulation form; memory O(N).
- **Brocard Point of a Triangle** (`D-Brocard-Point-Of-A-Triangle`): triangle side lengths and barycentric-style weights. Complexity: O(1) per triangle; memory O(1).
- **Cat Coat Colors** (`E-Cat-Coat-Colors`): probability enumeration over genotypes and gametes. Complexity: Constant time for the fixed gene model; memory O(number of colors).
  - Alternate: `solution_table.md` - Table Solution: Cat Coat Colors. Complexity: Constant time for the fixed gene model; memory O(number of colors).
- **Character Development** (`F-Character-Development`): combinatorics with powers of two. Complexity: O(N) big-integer multiplications in the checked-in loop; memory O(1) besides the big integer.
  - Alternate: `solution_formula.md` - Formula Solution: Character Development. Complexity: O(log N) style big-integer exponentiation as handled by Python; memory is the output integer size.
- **An Industrial Spy** (`G-An-Industrial-Spy`): permutation generation and primality testing. Complexity: Up to O(sum P(d,k) * sqrt(value)) per case; memory O(number of distinct values).
  - Alternate: `solution_sieve.md` - Sieve Solution: An Industrial Spy. Complexity: O(M log log M) sieve time plus permutation generation per test, where M is the maximum formed number; memory O(M).
- **Tomography** (`H-Tomography`): greedy Havel-Hakimi/Gale-Ryser style check. Complexity: O(m*n log n) due to sorting column sums for each row; memory O(m+n).
  - Alternate: `solution_gale_ryser.md` - Gale-Ryser Solution: Tomography. Complexity: O(m*n) after sorting; memory O(m+n).
- **Touchdown** (`I-Touchdown`): state simulation. Complexity: O(N) time and O(1) memory.
  - Alternate: `solution_prefix.md` - Prefix Solution: Touchdown. Complexity: O(N) time and O(N) memory for the position list.

## Main concepts covered
- geometry on polar street grid
- queue simulation on graph thresholds
- dynamic programming over grouped arrivals
- triangle side lengths and barycentric-style weights
- probability enumeration over genotypes and gametes
- combinatorics with powers of two
- permutation generation and primality testing
- greedy Havel-Hakimi/Gale-Ryser style check
- state simulation

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
