# CSCE 430 — Problem Solving Strategies (Week 1)

This repository contains my solutions for **CSCE 430**. The focus of this course is developing systematic problem-solving strategies through competitive programming–style problems.

All problems are solved using **Python** and are tested against the official **Kattis online judge**.

🔗 Kattis platform: https://open.kattis.com/

---

## Repository Contents

This repository contains:

- **Weekly problem solutions** assigned as part of CSCE 430
- **Weekly lab solutions**, when applicable
- **Upsolves** for problems that required revisiting after the initial attempt

Each problem is organized into its own folder.

---

## Folder Structure

Each problem folder contains:

- `description.md` — Markdown version of the official problem statement
- `solution.py` — Python solution implementation
- `input.txt` — Sample input used for local testing

Example structure:

```
week1/
├── problem-name/
│   ├── description.md
│   ├── input.txt
│   └── solution.py
└── README.md
```

---

## Running Solutions Locally

Each solution can be run locally using standard input redirection:

```bash
python solution.py < input.txt
```

This mirrors the execution environment used by the **Kattis** online judge.

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
