\# Task 01: Minimum Connections to Make Graph Connected



\## 🧠 Problem Description



Given `T` test cases, where each test case represents a graph with `n` vertices and `m` edges, this program calculates the \*\*minimum number of additional edges\*\* required to make the graph \*\*fully connected\*\*.



A graph is said to be connected if there is a path between every pair of vertices.



\## 🚀 How It Works



1\. For each test case:

&nbsp;  - A graph is created using adjacency lists.

&nbsp;  - A Depth-First Search (DFS) is performed to count the number of connected components.

&nbsp;  - The minimum edges required to connect all components is `components - 1`.



2\. The program also checks:

&nbsp;  - If the number of existing edges is insufficient to connect all nodes, it returns `-1`.



\## 🧮 Input Format



For each test case:

\- Line 1: Two integers `n m` — number of vertices and number of edges

\- Next `m` lines: Each line contains two integers `u v` representing an undirected edge



\## 📦 Example



\*\*Input:\*\*

Enter the number of test cases: 1

Enter the number of vertex and edges: 5 2

Enter the edge details:

1 2

3 4



makefile

Copy

Edit



\*\*Output:\*\*

2



markdown

Copy

Edit



\*\*Explanation:\*\*

\- Graph has 3 components: {1,2}, {3,4}, {5}

\- We need 2 additional edges to make the graph fully connected.



\## 🧩 Concepts Used



\- Graph traversal (DFS)

\- Connected components

\- Minimum spanning requirement (`components - 1`)

\- `defaultdict` for graph adjacency lists



\## 🛠️ How to Run



```bash

python min\_edges\_to\_connect.py

