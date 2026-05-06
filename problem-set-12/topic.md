# Problem Set 12 Topics

String and sequence algorithms: tries, rolling hashes, isomorphic matching, LIS reductions, and subsequence dynamic programming.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Boggle** (`A-Boggle`): trie plus depth-first search with bitmasks. Complexity: Per board, bounded by all length-at-most-8 board paths but heavily pruned by the trie; memory O(total dictionary letters).
- **Buzzwords** (`B-Buzzwords`): double rolling hash for substring counting. Complexity: O(n^2) time per input line and O(n) memory per length.
- **Chasing Subs** (`C-Chasing-Subs`): isomorphic string matching with per-letter hash signatures. Complexity: O(26*n log 26) time, effectively linear with a small constant; memory O(26).
- **Prince and Princess** (`D-Prince-And-Princesses`): longest increasing subsequence after coordinate mapping. Complexity: O((p+q) log p) per test case; memory O(n^2) for the position array bound.
- **Train Sorting** (`E-Train-Sorting`): dynamic programming for increasing and decreasing subsequences. Complexity: O(n^2) time and O(n) memory.

## Main concepts covered
- trie plus depth-first search with bitmasks
- double rolling hash for substring counting
- isomorphic string matching with per-letter hash signatures
- longest increasing subsequence after coordinate mapping
- dynamic programming for increasing and decreasing subsequences

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
