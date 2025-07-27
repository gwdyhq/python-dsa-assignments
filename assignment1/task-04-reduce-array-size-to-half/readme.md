# Task 04: Reduce Array Size to Half

## 🧠 Problem Description

Given an integer array, the goal is to remove the fewest number of **unique elements** such that **at least half of the elements in the array are removed** (by removing all occurrences of the chosen elements).

## 🚀 Program Flow

1. Accept the number of elements.
2. Accept the array elements as space-separated integers.
3. Count the frequency of each number using `collections.Counter`.
4. Sort frequencies in descending order.
5. Continuously remove elements with the highest frequency until at least half of the array is removed.
6. Output the **minimum number of unique elements removed**.

## 📦 Example

**Input:**
Enter the count of array elements: 10
Enter the array elements separated by spaces: 1 1 1 2 2 3 3 3 4 5

makefile
Copy
Edit

**Output:**
2

markdown
Copy
Edit

**Explanation:**
- Frequencies: `{1:3, 2:2, 3:3, 4:1, 5:1}`
- Remove all 1s (3) and all 3s (3) → Total removed = 6 → Half of 10
- Minimum unique elements removed = 2

## 🧩 Concepts Used

- Frequency counting using `collections.Counter`
- Greedy approach using sorted frequencies
- Conditional logic for handling even/odd array lengths

## 🛠️ How to Run

```bash
python reduce_array_half.py
✅ Sample Output
For input 1 1 1 2 2 3 3 3 4 5:

Copy
Edit
2