[![Python test](https://github.com/alejandro-kid/datamart-challenge/actions/workflows/python-test.yml/badge.svg)](https://github.com/alejandro-kid/datamart-challenge/actions/workflows/python-test.yml)

# Tech Datamart Challenge

The Tech Datamart Challenge is about solving a few problems using your knowledge. To demonstrate my seniority in Python I will solve these problems by adding an endpoint to each solution with its respective validations and tests in an API structure.

## Problem 1

Write a function called merge_arrays that accepts two sorted arrays of integers as parameters and returns a single sorted array containing all elements of both.

### Solution

#### Regular Solution

```python
def binary_insertion_sort_merge(list_1: list, list_2: list) -> tuple:
    merged_list = tuple(list_1 + list_2)
    for i in range(1, len(merged_list)):
        key = merged_list[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if merged_list[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        merged_list = merged_list[:left] + (key,) + merged_list[left:i] + \
                      merged_list[i+1:]
    return merged_list
```

One of the optimal solutions for this problem is to use the **binary insertion** algorithm, which has a complexity of $O(n log n)$ in ordered lists. Most of the ordered algorithms have the same complexity, but this solution has a spacial complexity of $O(1)$.

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
The main functions implemented by the author were the following: insert, minValueNode, maxValueNode, delete, find, and inorder.
For insertion, deletion, and search (includes minValueNode and maxValueNode) the complexity is **O(log n)**. Most of the methods or functions in a binary search tree have a low complexity of **O(log n)**, due to their characteristics such as well-known data structure, in such a way that unless the complete tree has to be returned (ordered or whatever way), it will not have to be traversed completely. However, traversing the tree in its entirety does not have a complexity greater than **O(n)**, with **n**, of course, being the number of nodes that make up the said tree. The deletion of an element is a special case of traversal of the entire tree in its worst case since it has to be re-ordered when a node is deleted, and in the best case, it has a constant complexity of **O(1)** when said node has no children or only 1 child.

## Problem 7

Write a function called remove_duplicates that accepts a list as a parameter and returns a new list with no duplicate elements.

### Solution

The solution here is simple, the author only uses a data structure of Python language. Sets are unordered collections of unique elements. So the only that we need to do is convert any list to a set.

```python
filtered_list = set(dirty_list)
```

## Problem 8

Given a list of numbers in ascending order and a target number, write a recursive function that finds whether the target number is in the list using a binary search.

### Regular Solution

This algorithm is a well-known algorithm, that works by splitting the list in half at each step and then comparing the target number to the number in the middle. If the target number is equal to the number in between, the function returns True. If the target number is less than the number in the middle, the function calls itself to find the number in the left half of the list. If the target number is greater than the number in the middle, the function calls itself to find the number in the right half of the list. The function continues to split the list in half and compare the target number with the number in the middle until it finds the target number or until it reaches the end of the list.

```python
def binary_search(ordered_list: list, element) -> bool:

  if len(ordered_list) == 0:
    return False

  medio = len(ordered_list) // 2
  if ordered_list[medio] == element:
    return True
  elif ordered_list[medio] > element:
    return binary_search(ordered_list[:medio], element)
  else:
    return binary_search(ordered_list[medio + 1:], element)
```

>Note: For the algorithm to work the list has to be ordered, this is not an implementation problem, it is a characteristic of binary search.

### Endpoint

Like the previous endpoints, in this one the input data is also validated, taking into account that for the algorithm to work it needs a list and an element to search for. As in the endpoint of **Problem 1**, if the list is not ordered, said logic makes sure to order the list before passing it to the algorithm.

## Parallelism Problem

The sequential search has a complexity of O(n) and the binary has a complexity of O(log n), which means that the bigger the search, the sequential will increase its inefficiency and will have an accelerated slope in a performance graph, while the binary will tend to stability growing slowly.
Because all the problems were solved wanting to give an API perspective, in this last solution about parallelism the workers are calculated from the environment variables defined by the user in the API deployment or simply calculated based on the CPU resources where said API is deployed.

```python
def map_function(list_1: list, list_2) -> dict:
    return dict(map(
        lambda elemento: (elemento, binary_search(list_1, elemento)), list_2
        ))

def map_function_workers(list_1: list, list_2: list) -> dict:

    pool = multiprocessing.Pool(workers)

    results = pool.starmap(binary_search,
                           [(list_1, elemento) for elemento in list_2])

    mapping_dict = {
        list_2[index]: element for index, element in enumerate(results)
    }

    pool.close()
    pool.join()

    return mapping_dict
```

Due to the author's previous analysis, it was decided to create a variant of the mapping function. Sometimes the same common functions cannot be parallelized due to their complexity. Complexity is understood as the way in which it is implemented, for which an exhaustive analysis of it must be done to make it work in a programming environment. parallel
