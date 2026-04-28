# [#70]. Climbing Stairs

**Difficulty:** Easy

## Problem Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

```python
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
```

## Approach

This is Fibonacci Sequence

If you are at step n, the last move must have been:

- from step `n-1` by taking `1` step
- or from step n-2 by taking `2` step

So the recurrence is :
`ways(n) = ways(n-1) + ways(n-2)`

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Tags

`Dynamic Programming`, `Recursion`
