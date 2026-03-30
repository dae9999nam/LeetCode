# [#226]. Invert Binary Tree

**Difficulty:** Easy

## Problem Description

Given the `root` of a binary tree, invert the tree, and return its root.

```python
Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:

Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
```

## Approach

Swap `root.right and root.left` and run for each subtrees until the subtree is None

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(H)

## Tags

`Binary Tree`, `Recursion`
