# Task 01: Minimum Distance to Nearest Well

## 🧠 Problem Description

Given a grid of size `m x n`, where each cell contains either:
- `'Y'`: a **well**, or
- other characters (representing locations),

This program calculates the **minimum distance from every cell to the nearest well** using a **multi-source BFS** approach.

## 🚀 Algorithm

- Treat all wells (`'Y'`) as sources and enqueue them in a queue.
- Use BFS to expand to all neighboring cells, updating the minimum distance at each step.
- Each cell stores the fewest steps required to reach any well.

## 🧩 Concepts Used

- 2D grid traversal
- Breadth-First Search (BFS)
- Multi-source BFS for simultaneous shortest path calculation

## 📦 Input Format

- First line: Two integers separated by space → `m n` (grid dimensions)
- Second line: Grid as a string, e.g.:
[[Y, N, N, Y, N]]

pgsql
Copy
Edit

⚠️ Note: Input format assumes a grid in a **stringified nested list** format.

## ✅ Example

**Input:**
1 5
[[Y, N, N, Y, N]]

makefile
Copy
Edit

**Output:**
[[0, 1, 1, 0, 1]]

markdown
Copy
Edit

**Explanation:**
- Distances to nearest `'Y'`:
  - Cell 0: already `'Y'` → distance 0
  - Cell 1: 1 step from left
  - Cell 2: 1 step from right
  - ...

## 🛠️ How to Run

```bash
python min_distance_to_well.py