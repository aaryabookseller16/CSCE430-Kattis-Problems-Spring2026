# Problem Set 11 Topics

Network flow and matching, plus SCC-style graph modeling. Some folders are placeholders with empty solutions.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Avoiding the Apocalypse** (`a`): time-expanded network flow with Dinic. Complexity: Let V=n(s+1) and E include all time-expanded roads; Dinic runs over that graph, with flow capped by the group size.
- **Problem Set 11 B** (`b`): No implemented primary solution. no implemented solution. Complexity: N/A for the checked-in file.
- **Club Representative Assignment** (`c`): max flow with party/person/club layers. Complexity: Dinic on O(parties + people + clubs) nodes and membership edges; memory O(E).
- **Gopher II** (`d`): bipartite matching. Complexity: O(n * E) with BFS augmenting paths in the checked-in implementation; memory O(E).

## Main concepts covered
- time-expanded network flow with Dinic
- no implemented solution
- max flow with party/person/club layers
- bipartite matching

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
