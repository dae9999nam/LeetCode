# [054] Spoiral Matrix

**Difficulty:** Medium

## Problem Description

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

## Approach

1. Set variables for top, bottom and left right

2. based on the values, index the elements of the matrix

3. Adjust the top, bottom and left, right values

## Complexity Analysis

- **Time Complexity:** O(M\*N)
- **Space Complexity:** O(1)

## Tags

`Array`
