# Task 03: Simulated Fibonacci Heap

## 🧠 Problem Description

This program simulates a simplified version of a **Fibonacci Heap** using a flat list structure in Python. It supports the following operations:

- `I value` – Insert a value
- `D` – Delete the minimum value
- `R old_value new_value` – Replace `old_value` with `new_value`

Finally, it outputs the total number of elements remaining in the heap, treated as **root nodes** (i.e., no actual tree structure is implemented).

## 🧩 Concepts Covered

- Heap operations (conceptual)
- Tracking minimum values efficiently using `np.argmin`
- Basic priority queue-like behavior

## 📌 Input Format

- First line: An integer `N` – number of operations
- Next `N` lines: One of the operations:
  - `I <value>` → Insert
  - `D` → Delete the minimum
  - `R <old_value> <new_value>` → Replace

## 📦 Example

**Input:**
5
I 10
I 5
I 20
D
R 10 3

makefile
Copy
Edit

**Output:**
2

markdown
Copy
Edit

**Explanation:**
- Insert 10 → [10]
- Insert 5 → [10, 5]
- Insert 20 → [10, 5, 20]
- Delete min (5) → [10, 20]
- Replace 10 with 3 → [3, 20]
- Final count = 2

## 🚀 How to Run

```bash
python fibonacci_heap_simulation.py