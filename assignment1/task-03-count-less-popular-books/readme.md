# Task 03: Count Less Popular Books to the Right

## 🧠 Problem Description

Given a list of books with their popularity indices, the task is to determine, for each book, how many books **after it** are **less popular** (i.e., have a lower popularity index).

This is similar to the "count of smaller elements to the right" problem in algorithms.

## 🚀 How It Works

1. The user enters the number of books.
2. Then, they input the popularity index (space-separated) for each book.
3. For each book `i`, the program:
   - Looks at all books to the right (index `i+1` onward)
   - Counts how many of them have a lower index
4. Outputs these counts in order as a single line.

## 📦 Example

**Input:**
Enter number of books: 5
Enter the array elements separated by spaces: 4 3 2 5 1

makefile
Copy
Edit

**Output:**
3 2 1 1 0

markdown
Copy
Edit

**Explanation:**
- Book 0 (4): books 1, 2, 4 are less popular → count = 3  
- Book 1 (3): books 2, 4 are less popular → count = 2  
- Book 2 (2): book 4 is less popular → count = 1  
- Book 3 (5): book 4 is less popular → count = 1  
- Book 4 (1): no books to the right → count = 0  

## 🧩 Concepts Used

- List slicing
- Looping with conditions
- String building for output formatting

## 🛠️ How to Run

```bash
python book_popularity_counter.py