# [#108]. Convert Sorted Array to Binary Sear5ch Tree

**Difficulty:** Easy

## Problem Description

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

```python
Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
```

## Approach

1. Define a `root` node with middle element and build tree recursively

2. Build `root.left` with range `left and mid -1`

3. Build `root.right` with range `mid +1 and right`

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(logN)

## Tags

`Divide and Conquer`, `Recursion`, `Binary Tree`
