# Task 03: Red-Black Tree and Pattern-Based Array Analysis

## 🧠 Problem Description

This assignment performs two major tasks:

### 1. Red-Black Tree Implementation

A custom Red-Black Tree is built from scratch in Python with full support for:

- Node insertion
- Deletion
- Tree rebalancing using left and right rotations
- Maintaining Red-Black Tree properties (e.g., balancing via colors)
- Retrieval of minimum, maximum, successor, and predecessor

This demonstrates the use of advanced self-balancing binary search trees.

### 2. Alternating Pattern Detection in an Array

After sorting an integer array:

- The program analyzes the array to detect alternating inequality patterns of the form:
  - If index is odd → `A[i] <= A[j]`
  - If index is even → `A[i] >= A[j]`

It counts how many values match this alternating pattern in a linear traversal.

## 🚀 Program Flow

1. A fixed or user-defined array is inserted into a Red-Black Tree.
2. The array is sorted using a basic bubble sort.
3. A pattern analysis loop scans for alternating inequalities and counts valid patterns.
4. The count is printed as output.

## 📦 Example

**Input array:**
```python
numarray = [1, 2, 3, 4, 5, 6, 6, 7, 8, 8]
Sorted array:

csharp
Copy
Edit
[1, 2, 3, 4, 5, 6, 6, 7, 8, 8]
Pattern match result:

makefile
Copy
Edit
Count: 1
🧩 Concepts Used
Red-Black Tree implementation and balancing

Tree-based data structures

Sorting (bubble sort)

Pattern recognition via conditional traversal

Alternating subsequence logic

🛠️ How to Run
bash
Copy
Edit
python rbtree_pattern_match.py