# Solution: Boggle

## Goal
Solve the problem with trie plus depth-first search with bitmasks. The implementation's main job is: Dictionary words are stored in a compact trie. For each 4x4 board, DFS follows neighboring cells while walking the trie, so dead prefixes stop early.

## Key idea
The solution is built around trie plus depth-first search with bitmasks. The key is to avoid unnecessary brute force by keeping the state described in the algorithm steps below. In other words: Dictionary words are stored in a compact trie. For each 4x4 board, DFS follows neighboring cells while walking the trie, so dead prefixes stop early.

## Step-by-step algorithm
1. Insert every dictionary word into a trie, ignoring words too long to be useful.
2. Precompute the valid neighboring cells for the fixed board size.
3. For each board, start a DFS from every cell whose letter is a trie child.
4. Carry the current trie node, board cell, visited-cell bitmask, and depth.
5. Whenever a terminal trie node is reached, count that word once for this board.
6. Stop a path when it reaches length 8 or no trie edge matches the next letter.
7. Compute score, longest word, and found-word count from the marked words.

## Example walkthrough
On a board containing C-A-T in adjacent cells, DFS reaches the trie node for CAT and counts it once.

In the walkthrough, trace the stored state after each important step. The answer comes from that state, not from guessing the output directly.

## Complexity
Per board, bounded by all length-at-most-8 board paths but heavily pruned by the trie; memory O(total dictionary letters).

## Important details
A seen marker per board prevents scoring the same word twice.
