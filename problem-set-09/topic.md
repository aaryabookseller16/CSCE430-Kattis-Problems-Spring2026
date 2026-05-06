# Problem Set 9 Topics

Minimum spanning trees and graph robustness: bridges, articulation points, modified MSTs, and complete-graph Prim.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Arctic Network** (`arctic-network`): minimum spanning tree. Complexity: O(P^2 log P) time and O(P^2) memory due to the complete graph.
- **Cave Exploration** (`cave-exploration`): bridge-finding with low-link DFS. Complexity: O(n+m) time and memory.
- **Eroding Pillars** (`eroding-pillars`): binary search over distances plus articulation points. Complexity: O(D * (n^2+n+m)) where D is log of the number of unique distances; memory O(n^2) for candidate graphs.
- **Landline Telephone Network** (`landline-telephone-network`): modified MST with special leaf nodes. Complexity: O(m log m) time and O(n+m) memory.
- **Lost Map** (`lost-map`): Prim MST on a complete distance table. Complexity: O(n^2) time and O(n^2) memory for the distance table.

## Main concepts covered
- minimum spanning tree
- bridge-finding with low-link DFS
- binary search over distances plus articulation points
- modified MST with special leaf nodes
- Prim MST on a complete distance table

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
