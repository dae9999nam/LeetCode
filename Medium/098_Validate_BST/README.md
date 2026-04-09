# [#098]. Validate Binary Search Tree

**Difficulty:** Medium

## Problem Description

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys **strictly less than** the node's key.
The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
Both the left and right subtrees must also be binary search trees.

```python
Example 1:

Input: root = [2,1,3]
Output: true
Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
```

## Approach

1. Compare `node.val` with `node.left` and `low`, and `node.right` and `high` for each subtree

2. If `node.val` is not in range `low < node.val < high`, return `False`

3. If it reaches to the `leaf node`, return True

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(H)

## Tags

`Binary Tree`, `Recursion`
