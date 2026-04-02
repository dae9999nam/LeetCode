# [#637]. Average of Levels in Binary Tree

**Difficulty:** Easy

## Problem Description

Given the `root` of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within `10^-5` of the actual answer will be accepted.

```python
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]


Constraints:

The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1
```

## Approach

BFS processes the tree level by level.

At each loop:

- `queue` contains exactly the nodes of the current level
- `level_size` tells us how many nodes belong to this level
- we sum their values
- divide by `level_size`

## Complexity Analysis

- **Time Complexity:** O(N^2)
- **Space Complexity:** O(M)

## Tags

`Breadth-First Search`, `Queue`, `Binary Tree`
