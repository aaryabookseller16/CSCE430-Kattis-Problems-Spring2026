# CSCE 430 — Problem Solving Strategies (Week 1)

This repository contains my **Week 1 solutions** for **CSCE 430**. The focus of this course is developing systematic problem-solving strategies through competitive programming–style problems.

All problems are solved using **Python** and are tested against the official **Kattis online judge**.

🔗 Kattis platform: https://open.kattis.com/

---

## Repository Structure

Each folder corresponds to **one problem** and contains:

- `description.md` — Clean Markdown version of the official problem statement
- `solution.py` — My implementation
- `input.txt` — Sample input used for local testing

```
week1/
├── 1d-frogger
├── alien-numbers
├── kindergarten-excursion
├── natrij
├── path-tracing
├── pivot
└── README.md
```

---

## Problems Included

### 1. 1D Frogger
- Simulates frog movement on a one-dimensional board
- Requires careful cycle detection and boundary checking
- Emphasizes simulation and state tracking

### 2. Alien Numbers
- Converts numbers between arbitrary alien numeral systems
- Reinforces base conversion and symbol mapping
- Focuses on careful parsing and representation

### 3. Kindergarten Excursion
- Rearranges a sequence using **minimum adjacent swaps**
- Equivalent to counting constrained inversions
- Highlights greedy reasoning and efficiency constraints

### 4. Natrij
- Computes the time difference between two clock times
- Includes wrap-around across midnight
- Focuses on edge cases and modular arithmetic

### 5. Path Tracing
- Traces a path given directional moves
- Outputs a bounded 2D map with strict formatting
- Emphasizes coordinate tracking and output precision

### 6. Pivot
- Identifies valid pivot elements after array partitioning
- Uses prefix maximums and suffix minimums
- Demonstrates linear-time reasoning on arrays

---

## Goals of This Repository

- Practice **systematic problem decomposition**
- Build intuition for **algorithmic patterns** (simulation, greedy, prefix/suffix scans)
- Improve comfort with **competitive programming I/O formats**
- Write clean, readable, and testable code

---

## Notes on Kattis Compatibility

- All solutions read input from **standard input (stdin)**
- All output formats strictly follow problem specifications
- No file paths are used in submitted solutions

Local `input.txt` files are included **only for debugging** and are not used on Kattis.

---

## Author

**Aarya Bookseller**  
CSCE 430 — Texas A&M University

---

This repository is intended for **educational use** as part of CSCE 430.
