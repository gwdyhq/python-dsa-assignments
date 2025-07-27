# Task 02: Custom Swap in Singly Linked List

## 🧠 Problem Description

This program implements a singly linked list and performs a custom swap operation on its elements.

The swap logic is as follows:
- For the **first half of the list**, if the **(index + 1)** is even, the element at that index is swapped with its **mirror** index from the end of the list.

## 🚀 Program Flow

1. The user inputs a list of space-separated integers.
2. A singly linked list is constructed using a `Node` class.
3. A custom `swap_list` function:
   - Converts the linked list to a list
   - Swaps elements according to the rule
   - Converts it back to a linked list
4. The resulting linked list is printed.

## 📦 Example

**Input:**
Enter the count of array elements: 6
Enter the array elements separated by spaces: 1 2 3 4 5 6

**Output:**
1 2 5 4 3 6