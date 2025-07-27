# Task 12: Maximum Flower Planting with Bitmask DP

## 🧠 Problem Description

Given a 2D grid representing a garden (`n` rows and `m` columns), where:
- `'1'` represents a **plantable** plot
- `'0'` represents a **blocked** plot

Determine the **maximum number of flowers** that can be planted such that:

- No two flowers are planted **next to each other horizontally** on the same row.
- No two flowers are planted in **adjacent columns across consecutive rows** (vertical adjacency or diagonals).
- You **cannot plant** on `'0'` plots.

## 💡 Key Concepts

- **Bitmasking**: Each possible arrangement of flowers on a row is represented as an integer.
- **Dynamic Programming (DP)**: Builds solutions row by row, considering valid configurations.
- **Adjacency Constraints**: Carefully handled using bitwise operations and masking.

## 📦 Input Format

The function takes as input:
- `grid`: A list of strings, each string of `'0'` or `'1'`
- `n`: Number of rows
- `m`: Number of columns

Example:
```python
grid = ['010', '101', '010']
n = 3
m = 3
🚀 Example Output
bash
Copy
Edit
Test case 1: grid=['010', '101', '010'], n=3, m=3 -> Max flowers: 5
Test case 2: grid=['111', '000', '111'], n=3, m=3 -> Max flowers: 3
Test case 3: grid=['0110', '1010', '0110'], n=3, m=4 -> Max flowers: 6
Test case 4: grid=['0', '1', '0', '1'], n=4, m=1 -> Max flowers: 2
Test case 5: grid=[''], n=0, m=0 -> Max flowers: 0
📌 Constraints
Only '0' and '1' are valid grid characters.

Invalid characters will raise a ValueError.

🧩 Techniques Used
Bitmask enumeration for all valid row states

DP state transition validation across adjacent rows

bin(state).count('1') to count flowers in a configuration

🛠️ How to Run
bash
Copy
Edit
python max_flowers_bitmask.py