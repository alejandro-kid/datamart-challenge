[![Python test](https://github.com/alejandro-kid/datamart-challenge/actions/workflows/python-test.yml/badge.svg)](https://github.com/alejandro-kid/datamart-challenge/actions/workflows/python-test.yml)

# Tech Datamart Challenge

The Tech Datamart Challenge is about solving a few problems using your knowledge. To demonstrate my seniority in Python I will solve these problems by adding an endpoint to each solution with its respective validations and tests in an API structure.

## Problem 1

Write a function called merge_arrays that accepts two sorted arrays of integers as parameters and returns a single sorted array containing all elements of both.

### Solution

#### Regular Solution

```python
def merge_array(list_1: list, list_2: list) -> list:
    return list(merge(list_1, list_2))
```

The optimal solution for this problem is to use the **merge** algorithm, this algorithm has a complexity of O(n log n) in ordered lists, has an efficient use of memory and is very quick.

#### Endpoint

The endpoint for this algorithm receives a JSON with two lists, no matter what kind of data is stored in these lists, the logic of the endpoint do validations to check the data is correct. After that, the endpoint checks if the lists are unordered and then sorts them using the **sorted** algorithm, this algorithm is more efficient than the **merge** algorithm in unordered lists. The algorithmic complexity of the function to determine if the list is ordered or not is **O(n)**. This is because the function loops through number_list twice, once to get the items from first to last, and again to get the items from second to last. Each iteration of the function takes **O(1)** time, so the total complexity of the function is **O(n)**.

## Problem 2

Write a function called find_median that accepts an array of integers as a parameter and returns the median of the array.

### Regular Solution

I am not going to reinvent the wheel, the median of a set of numbers is an operation well-known to all. Python through its **statistics** module (library) provides an implementation of this algorithm in its medium variant of the two in the middle, which has an algorithmic complexity of **O(n)** and is also efficient in terms of resource consumption.

### Endpoint

The endpoint to process the request does not have something weird. Checking if the list provided by the user is a number list is the only validation implemented.

## Problem 3

Write a class called BinaryTree that implements a binary search tree. The class must have methods to insert, find, and must be able to print the tree in ascending order. Analyze the computational complexity of each operation implemented in your solution.

### Solution

A binary tree is a non-linear data structure in which each node can point to one or at most two nodes. Binary search trees are a special type of binary tree whose characteristic lies in the ordered way of inserting its elements, thus facilitating the search for a particular node.
The main functions implemented by the author were the following: insert, minValueNode, maxValueNode, delete, find and inorder.
For insertion, deletion and search (includes minValueNode and maxValueNode) the complexity is **O(log n)**. To print the values of the tree, the complexity is **O(n)** where n is the number of nodes that the tree has.