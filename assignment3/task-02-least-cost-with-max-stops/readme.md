# Task 02: Least Cost Travel with Maximum Stops

## 🧠 Problem Description

Given a network of cities and train connections with travel costs, determine the **least possible cost** to travel from a start city to a destination city — **without exceeding a given number of stops**.

If no such route exists, return `-1`.

## 📌 Input Format

- Number of cities (`n`)
- List of routes as tuples: `(from_city, to_city, cost)`
- Start city
- Destination city
- Maximum allowed stops

## 🧮 Sample Input

Enter the number of cities to visit: 7
Enter visit details in order fromcity,tocity,cost: [[1, 2, 20], [1, 3, 10], [1, 6, 30], [2, 5, 40], [3, 4, 50], [4, 5, 60], [5, 6, 70], [0, 1, 22]]
Enter the start city: 1
Enter the destination city: 5
Enter the maximum stops: 3

makefile
Copy
Edit

**Output:**
60

markdown
Copy
Edit

## 🛠️ How It Works

- An adjacency list is created for all city connections.
- A modified Dijkstra's-like traversal is performed using a sorted queue to find the least cost path.
- Only paths within the allowed stop count are considered.

## ✅ Sample Output Explanations

- If a path exists within the given stop limit → returns **minimum cost**
- If no path exists within stop limit → returns `-1`
- If start and destination are the same → returns `0`

## 🧩 Concepts Used

- Graph traversal (similar to BFS + greedy cost)
- Priority queue simulation (using merge sort)
- Cost tracking using `(city, stops)` state representation

## 🚀 How to Run

```bash
python least_cost_path.py