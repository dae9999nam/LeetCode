# [#025], Reverse Nodes in K-Group

**Difficulty:** Hard

## Problem Description

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

```python
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

Example 2:

```python
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

Constraints:

```python
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
```

## Approach

1. Get first k-th group nodes and connect it to dummy

2. Reverse the group nodes until `cur == groupnext`

3. Reconnect it to original linked list

## Complexity Analysis

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Tags

`Linked List`, `Recursion`, `Two Pointers`
