# Task 01: Minimum Dust Refills to Reach Destination

## 🧠 Problem Description

This program determines the **minimum number of dust stops** (refueling stations) required to reach a destination using a greedy approach.

### Input

- **Destination Miles**: Total distance to the destination.
- **Available Dust**: Starting dust (like fuel).
- **Wells List**: A list of tuples/lists where each element represents:
  - Position of the dust well (in miles)
  - Amount of dust available at that well

### Objective

Reach the destination by making the **minimum number of dust collection stops**. If it is not possible to reach the destination, the function returns `-1`.

## 🚀 Example

**Input:**
Enter destination miles: 25
Enter dust available at start: 10
Enter the list of stop_count: [[10, 10], [14, 5], [20, 7]]

makefile
Copy
Edit

**Output:**
2

vbnet
Copy
Edit

**Explanation:**
- You start with 10 units of dust and travel to the first well at mile 10.
- Collect 10 dust → Continue to well at mile 14.
- Still need one more stop to reach 25 → Total 2 stops.

## 🛠️ How It Works

- The program simulates travel from start to destination.
- At each well, the dust amount is added to a **priority list**.
- If you cannot reach the next well or destination, you "backtrack" and pick the best dust stop (max dust from the priority list).
- Implements **manual max-heap** logic for learning purposes.

## 🧩 Concepts Used

- Greedy strategy
- Max-heap simulation
- Priority queue behavior using a list
- Manual heap sort (via recursive heapify)

## 🛠️ How to Run

```bash
python min_dust_stops.py