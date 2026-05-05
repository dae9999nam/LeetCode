# [#046]. Permutation

**Difficulty:** Medium

## Problem Description

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

```python
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
```

## Approach

1. **Define a Recursive Function**: Create a function (e.g., `backtrack`) that maintains the `current_path` of numbers chosen so far.

2. **Identify the Base Case**: When the length of your `current_path` equals the length of the input array `nums`, you have a complete permutation. Add a **copy** of this path to your results.

3. **Iterate and Filter**: Loop through every number in `nums`. If the number is not already in your current_path, it is a valid choice for the next position.

4. **Recursive Step (DFS)**: Add the chosen number to the `path` and call the function again to pick the next number.

5. **Backtrack**: After the recursive call returns, remove the last number added `pop()` so the loop can try the next available number for that same position.

## Complexity Analysis

- **Time Complexity:** O(`n*n!`)
- **Space Complexity:** O(`n*n!`)

## Tags

`Backtracking`, `Recursion`
