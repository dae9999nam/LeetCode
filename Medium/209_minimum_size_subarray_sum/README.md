# [#209]. Minimum Size Subarray Sum

**Difficulty:** Medium

## Problem Description

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is **greater than or equal to** `target`. If there is no such subarray, return `0` instead.

Example 1:

```python
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

Example 2:

```python
Input: target = 4, nums = [1,4,4]
Output: 1
```

Example 3:

```python
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

Constraints:

```python
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
```

## Approach

1. Set `left` and `right` as the edge index of the array `nums`

2. Sum `nums[right]` and compare it with `target`

3. If the sum is greater than or equal to the `target`, then subtract `nums[left]` and increment `left` by `1`

4. return `0` if the length is `-inf` else return the length `right -left +1`

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Tags

`Sliding Window`, `Array`
