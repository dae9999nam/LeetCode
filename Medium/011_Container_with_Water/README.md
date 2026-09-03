# [#011]. Container with Most Water

**Difficulty:** Medium

## Problem Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount** of water a container can store.

Notice that you may not slant the container.

Example 1:

```python
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

Example 2:

```python
Input: height = [1,1]
Output: 1
```

Constraints:

```python
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
```

## Approach

1. Note that the area is decided by the smaller height.

2. Decide when to move which height, in this case, when the left height is smaller, then we move one to the right

3. If the right height is smaller, then we move the one to the left.

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Tags

`Two Pointers`, `Greedy`
