# [#100]. Same Tree

**Difficulty:** Easy

## Problem Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

```python
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

Example 2:

```python
Input: p = [1,2], q = [1,null,2]
Output: false
```

Example 3:

```python
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

Constraints:

```python
The number of nodes in both trees is in the range [0, 100].
-10**4 <= Node.val <= 10**4
```

## Approach

1. Check if both nodes are empty
2. one is empty and the other is not --> different, return `False`
3. current values are not equl --> return `False`
4. Check for `left` and `right` recursively.

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(H)

## Tags

`Recursion`, `Binary Tree`, `Depth-Frist-Search`
