# [#128]. Longest Consecutive Sequence

**Difficulty:** Medium

## Problem Description

Given an unsorted array of integers `nums`, return the **length of the longest consecutive elements sequence**.

You must write an algorithm that runs in `O(n)` time.

Example 1:

```python
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

Example 2:

```python
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

Example 3:

```python
Input: nums = [1,0,1,2]
Output: 3
```

Constraints:

```python
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
```

## Approach

1. Sort the given array `nums`

2. count the length of consecutive numbers and compare it with `max_length`

3. if same number exist, pass

## Complexity Analysis

- **Time Complexity:** O(NlogN)
- **Space Complexity:** O(N)

## Tags

`Sorting`
