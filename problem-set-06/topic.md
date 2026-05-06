# Problem Set 6 Topics

Dynamic programming and game reasoning: interval DP, expected value, constrained path DP, and backward induction.

## How to use this folder
Read `topic.md` first for the map, then open each problem folder. The main explanation is `solution.md`. If the folder has extra Python implementations, each has its own matching markdown file.

## Problem guide
- **Assembly Line** (`assembly-line`): interval dynamic programming. Complexity: O(L^3*K^2) per query string; memory O(L^2*K).
  - Alternate: `efficient.md` - Efficient Solution: Assembly Line. Complexity: Still O(L^3*K^2) in the worst case, but often much faster when few result types are reachable; memory O(L^2*K).
- **Deceptive Dice** (`deceptive-die`): expected value dynamic programming. Complexity: O(k) time using arithmetic sums over die faces; memory O(1).
- **Narrow Art Gallery** (`narrow-art-gallery`): dynamic programming over rows and closure state. Complexity: O(n*k) time and O(k) memory.
- **Spiderman Workout** (`spidermans-workout`): height DP with parent reconstruction. Complexity: O(M*S) time and memory, where S is the total distance.
- **Uxuhul Voting System** (`the-uxhul-voting-system`): backward induction over game states. Complexity: O(m*8*3) time and O(8) memory.

## Main concepts covered
- interval dynamic programming
- expected value dynamic programming
- dynamic programming over rows and closure state
- height DP with parent reconstruction
- backward induction over game states

## Notes
These notes describe the code that is currently checked in. Empty `solution.py` files are marked as missing implementations rather than being explained as if they were solved.
