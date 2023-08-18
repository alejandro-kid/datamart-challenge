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

The endpoint for this algorithm receives a JSON with two lists, no matter what kind of data is stored in these lists, the logic of the endpoint do validations to check the data is correct. After that, the endpoint checks if the lists are unordered and then sorts them using the **sorted** algorithm, this algorithm is more efficient than the **merge** algorithm in unordered lists.

## Problem 2

Write a function called find_median that accepts an array of integers as a parameter and returns the median of the array.

### Regular Solution

I am not going to reinvent the wheel, the median of a set of numbers is an operation well-known to all. Python through its **statistics** module (library) provides an implementation of this algorithm in its medium variant of the two in the middle, which has an algorithmic complexity of **O(n)** and is also efficient in terms of resource consumption.

### Endpoint

The endpoint to process the request does not have something weird. Checking if the list provided by the user is a number list is the only validation implemented.
