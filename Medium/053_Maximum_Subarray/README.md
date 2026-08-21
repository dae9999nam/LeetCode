# [053]. Maximum Subarray

**Difficulty:** Medium

## Problem Description

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

Example 1:

```python
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

Example 2:

```python
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

Example 3:

```python
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

Constraints:

`1 <= nums.length <= 10^5`
`-10^4 <= nums[i] <= 10^4`

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Approach

1. Use `Kadane's Algorithm`.

2. Main idea is to determine whether to use `current_sum` as 'new number of new subarray' or 'add to existing subarray'.

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Tags

`Kadane's algorithm`, `dynamic programming`, `divide and conquer`
