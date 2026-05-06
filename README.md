# CSCE 430 Kattis Problems - Spring 2026

This repository contains my CSCE 430 competitive programming work for Spring 2026. It is organized into two main sections:

- [`Problem Sets`](Problem%20Sets) for weekly assigned problem sets
- [`Labs`](Labs) for lab practice, solved-in-lab problems, and upsolves

Every solved problem folder is intended to include the original problem statement, Python solution code, sample input when available, and a plain-English explanation of the algorithm.

## Table of Contents

- [Repository Layout](#repository-layout)
- [Progress Summary](#progress-summary)
- [Problem Sets](#problem-sets)
- [Labs](#labs)
- [Documentation Format](#documentation-format)
- [Running Solutions Locally](#running-solutions-locally)
- [Notes](#notes)

## Repository Layout

```text
.
├── Problem Sets/
│   ├── Problem Set 14 - Computational Geometry/
│   ├── Problem Set 13 - Number Theory and Counting/
│   └── ...
├── Labs/
│   ├── Lab 13 - Mixed Contest Practice/
│   ├── Lab 12 - Placeholder Problems/
│   └── ...
└── README.md
```

Inside each weekly folder, each problem has its own folder. Most problem folders follow this shape:

```text
problem-name/
├── description.md
├── input.txt
├── solution.py
└── solution.md
```

Some folders also include alternate implementations such as `solution_slow.py`, `solution_formula.py`, or `efficient.py`. Those have matching explanation files, for example `solution_slow.md` or `efficient.md`.

## Progress Summary

| Section | Weeks/Folders | Solved | Total Problems | Alternate Implementations |
|---|---:|---:|---:|---:|
| Problem Sets | 14 | 58 | 63 | 7 |
| Labs | 9 | 56 | 68 | 8 |
| **Total** | **23** | **114** | **131** | **15** |

Solved means the folder has a non-empty `solution.py`. Empty solutions are kept in the repository, but marked as placeholders in their `solution.md` files.

## Problem Sets

The problem sets are listed in descending order, with the newest/highest-numbered set first.

| Week | Folder | Topics | Solved | Alternate solutions | Topic notes |
|---:|---|---|---:|---:|---|
| 14 | [Problem Set 14 - Computational Geometry](Problem%20Sets/Problem%20Set%2014%20-%20Computational%20Geometry) | Computational geometry: hulls, intersections, polygon simplification, distances | 5/5 | 5 | [topic.md](Problem%20Sets/Problem%20Set%2014%20-%20Computational%20Geometry/topic.md) |
| 13 | [Problem Set 13 - Number Theory and Counting](Problem%20Sets/Problem%20Set%2013%20-%20Number%20Theory%20and%20Counting) | Modular inverses, factorial logs, sieves, cycle detection, greedy scheduling | 5/5 | 1 | [topic.md](Problem%20Sets/Problem%20Set%2013%20-%20Number%20Theory%20and%20Counting/topic.md) |
| 12 | [Problem Set 12 - String Algorithms](Problem%20Sets/Problem%20Set%2012%20-%20String%20Algorithms) | Tries, rolling hashes, string matching, LIS reductions | 5/5 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2012%20-%20String%20Algorithms/topic.md) |
| 11 | [Problem Set 11 - Flow and Matching](Problem%20Sets/Problem%20Set%2011%20-%20Flow%20and%20Matching) | Time-expanded flow, max flow, bipartite matching | 3/4 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2011%20-%20Flow%20and%20Matching/topic.md) |
| 10 | [Problem Set 10 - Strong Connectivity](Problem%20Sets/Problem%20Set%2010%20-%20Strong%20Connectivity) | Strongly connected components and graph augmentation | 2/2 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2010%20-%20Strong%20Connectivity/topic.md) |
| 9 | [Problem Set 09 - Minimum Spanning Trees and Connectivity](Problem%20Sets/Problem%20Set%2009%20-%20Minimum%20Spanning%20Trees%20and%20Connectivity) | MSTs, bridges, articulation points, secure connectivity | 5/5 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2009%20-%20Minimum%20Spanning%20Trees%20and%20Connectivity/topic.md) |
| 8 | [Problem Set 08 - Graph Traversal and Dependencies](Problem%20Sets/Problem%20Set%2008%20-%20Graph%20Traversal%20and%20Dependencies) | Graph coloring, topological order, BFS layers, 0-1 BFS | 4/5 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2008%20-%20Graph%20Traversal%20and%20Dependencies/topic.md) |
| 7 | [Problem Set 07 - Search Optimization and Matrix Exponentiation](Problem%20Sets/Problem%20Set%2007%20-%20Search%20Optimization%20and%20Matrix%20Exponentiation) | Binary/ternary search, interactive narrowing, matrix exponentiation | 5/5 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2007%20-%20Search%20Optimization%20and%20Matrix%20Exponentiation/topic.md) |
| 6 | [Problem Set 06 - Dynamic Programming](Problem%20Sets/Problem%20Set%2006%20-%20Dynamic%20Programming) | Dynamic programming, expected value, interval DP, game-state reasoning | 5/5 | 1 | [topic.md](Problem%20Sets/Problem%20Set%2006%20-%20Dynamic%20Programming/topic.md) |
| 5 | [Problem Set 05 - Greedy Number Theory and Search](Problem%20Sets/Problem%20Set%2005%20-%20Greedy%20Number%20Theory%20and%20Search) | Greedy scheduling, number theory, constraints, backtracking, interval covering | 5/5 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2005%20-%20Greedy%20Number%20Theory%20and%20Search/topic.md) |
| 4 | [Problem Set 04 - Fenwick Trees and Range Queries](Problem%20Sets/Problem%20Set%2004%20-%20Fenwick%20Trees%20and%20Range%20Queries) | Fenwick trees, range queries, and placeholder data-structure problems | 2/5 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2004%20-%20Fenwick%20Trees%20and%20Range%20Queries/topic.md) |
| 3 | [Problem Set 03 - Union Find](Problem%20Sets/Problem%20Set%2003%20-%20Union%20Find) | Union-find and dynamic disjoint sets | 2/2 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2003%20-%20Union%20Find/topic.md) |
| 2 | [Problem Set 02 - Maps Binary Search and Stacks](Problem%20Sets/Problem%20Set%2002%20-%20Maps%20Binary%20Search%20and%20Stacks) | Maps, binary search, stack/queue/heap simulation, monotonic stacks | 4/4 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2002%20-%20Maps%20Binary%20Search%20and%20Stacks/topic.md) |
| 1 | [Problem Set 01 - Implementation and Simulation](Problem%20Sets/Problem%20Set%2001%20-%20Implementation%20and%20Simulation) | Implementation, simulation, base conversion, inversions, time arithmetic, prefix/suffix scans | 6/6 | 0 | [topic.md](Problem%20Sets/Problem%20Set%2001%20-%20Implementation%20and%20Simulation/topic.md) |

## Labs

The labs are also listed in descending order. Missing lab numbers simply were not present in this repository.

| Week | Folder | Topics | Solved | Alternate solutions | Topic notes |
|---:|---|---|---:|---:|---|
| 13 | [Lab 13 - Mixed Contest Practice](Labs/Lab%2013%20-%20Mixed%20Contest%20Practice) | Mixed contest practice: geometry, graph cascades, DP, genetics, tomography | 9/9 | 8 | [topic.md](Labs/Lab%2013%20-%20Mixed%20Contest%20Practice/topic.md) |
| 12 | [Lab 12 - Placeholder Problems](Labs/Lab%2012%20-%20Placeholder%20Problems) | Placeholder lab: problem folders exist, but checked-in solutions are empty | 0/9 | 0 | [topic.md](Labs/Lab%2012%20-%20Placeholder%20Problems/topic.md) |
| 11 | [Lab 11 - DSU BFS and MST](Labs/Lab%2011%20-%20DSU%20BFS%20and%20MST) | Reverse DSU, Collatz maps, DFS safety, BFS precomputation, MST | 6/8 | 0 | [topic.md](Labs/Lab%2011%20-%20DSU%20BFS%20and%20MST/topic.md) |
| 10 | [Lab 10 - Graph Search and Shortest Paths](Labs/Lab%2010%20-%20Graph%20Search%20and%20Shortest%20Paths) | BFS, Dijkstra, shortest paths, line simulation, dynamic programming | 8/8 | 0 | [topic.md](Labs/Lab%2010%20-%20Graph%20Search%20and%20Shortest%20Paths/topic.md) |
| 6 | [Lab 06 - DP Math and Fenwick Trees](Labs/Lab%2006%20-%20DP%20Math%20and%20Fenwick%20Trees) | Math cases, trading greedily, Euler tour plus Fenwick tree | 4/4 | 0 | [topic.md](Labs/Lab%2006%20-%20DP%20Math%20and%20Fenwick%20Trees/topic.md) |
| 5 | [Lab 05 - Greedy and Graph Components](Labs/Lab%2005%20-%20Greedy%20and%20Graph%20Components) | Greedy scans, component sums, union-find constraints, inheritance propagation | 8/8 | 0 | [topic.md](Labs/Lab%2005%20-%20Greedy%20and%20Graph%20Components/topic.md) |
| 4 | [Lab 04 - Simulation Strings and Prefix Checks](Labs/Lab%2004%20-%20Simulation%20Strings%20and%20Prefix%20Checks) | Short simulations, string scans, rational sequences, prefix checks | 5/6 | 0 | [topic.md](Labs/Lab%2004%20-%20Simulation%20Strings%20and%20Prefix%20Checks/topic.md) |
| 2 | [Lab 02 - Greedy and Upsolves](Labs/Lab%2002%20-%20Greedy%20and%20Upsolves) | Greedy balancing, paper construction, digit sums, heaps, grid reachability | 8/8 | 0 | [topic.md](Labs/Lab%2002%20-%20Greedy%20and%20Upsolves/topic.md) |
| 1 | [Lab 01 - Warmup Implementation](Labs/Lab%2001%20-%20Warmup%20Implementation) | Warmup implementation: sorting, simulation, grid rotation, greedy pairing | 8/8 | 0 | [topic.md](Labs/Lab%2001%20-%20Warmup%20Implementation/topic.md) |

## Documentation Format

Each `topic.md` summarizes the week's themes and problem list. Each `solution.md` explains the checked-in `solution.py` with:

- the goal of the problem
- the key idea
- a step-by-step algorithm
- an example walkthrough
- time and memory complexity
- implementation details worth remembering

When multiple implementations exist, each implementation gets its own markdown file. For example:

```text
Problem Set 14 - Computational Geometry/A-Board-Wrapping/
├── solution.py
├── solution.md
├── solution_slow.py
└── solution_slow.md
```

## Running Solutions Locally

From a problem folder, run a solution with standard input redirection:

```bash
python3 solution.py < input.txt
```

Example:

```bash
cd "Problem Sets/Problem Set 14 - Computational Geometry/A-Board-Wrapping"
python3 solution.py < input.txt
```

This mirrors how Kattis runs submitted programs: input comes from standard input, and output goes to standard output.

## Notes

- All submitted solutions are written in Python.
- `input.txt` files are for local testing only.
- Empty `solution.py` files are documented as missing implementations instead of being treated as solved.
- Some folders contain `solution_rankings.md`; those are separate comparison notes and are not counted as implementations.

## Author

Aarya Bookseller  
CSCE 430 - Texas A&M University
