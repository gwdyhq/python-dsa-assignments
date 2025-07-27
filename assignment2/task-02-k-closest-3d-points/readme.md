# Task 02: K Closest 3D Points to Origin

## 🧠 Problem Description

Given a list of 3D coordinates, the goal is to return the `K` points that are closest to the origin `(0, 0, 0)` using **Euclidean distance**.

The program implements this logic manually using **heap sort** (max-heap) to sort the points based on their distance to the origin.

## 🚀 Input/Output

### Input

- `N`: Number of 3D points
- `K`: Number of closest points to find
- A list of N 3D points (e.g., `[[1, 2, 3], [-1, -2, -3], [4, 5, 6]]`)

### Output

- A list containing `K` closest points to the origin based on distance.

## 📦 Example

**Input:**
Number of 3D points: 3
Number of close points to be found: 2
list of all points: [[-6, -9, -4], [6, -2, 0], [-5, -4, 2]]

makefile
Copy
Edit

**Output:**
[[6, -2, 0], [-5, -4, 2]]

markdown
Copy
Edit

**Explanation:**
- Distance from origin:
  - [-6, -9, -4] → 133
  - [6, -2, 0] → 40
  - [-5, -4, 2] → 45
- Top 2 closest points: [6, -2, 0] and [-5, -4, 2]

## 🧩 Concepts Used

- Euclidean distance: `sqrt(x² + y² + z²)` (without `sqrt` for efficiency since we just compare magnitudes)
- Max-Heap logic to sort distances
- Manual heapify for sorting

## 🛠️ How to Run

```bash
python k_closest_points.py